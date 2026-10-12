<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/connectors-gbif-src-readme
title: connectors/gbif/src/ — GBIF Connector Source Root
type: readme
version: v0.2
status: draft
owners: OWNER_TBD — Connector steward · GBIF source steward · Biodiversity steward · Flora steward · Fauna steward · Habitat steward · Taxonomy steward · Rights reviewer · Privacy/sensitivity reviewer · Security reviewer · Packaging steward · Validation steward · Docs steward
created: 2026-06-18
updated: 2026-07-11
policy_label: public-doctrine; source-root; greenfield; per-dataset-rights; geoprivacy-gated; product-specific-roles; source-first; no-live-by-default; no-secrets; no-persistence-default; raw-or-quarantine-candidate-only; no-publication
proposed_path: connectors/gbif/src/README.md
truth_posture: CONFIRMED source root with README plus one package-shaped GBIF scaffold / executable behavior ABSENT / packaging incomplete / package-local public sensitivity placeholder INVALID / plants child COMPATIBILITY-ONLY / product descriptors and activation ABSENT / executable tests ABSENT / live testing NOT APPROVED / CI UNKNOWN
related:
  - ../README.md
  - ../pyproject.toml
  - ../plants/README.md
  - ../tests/README.md
  - gbif/README.md
  - gbif/__init__.py
  - gbif/fetch.py
  - gbif/descriptor.yaml
  - ../../../docs/sources/catalog/gbif/README.md
  - ../../../docs/sources/catalog/gbif/occurrence-api.md
  - ../../../docs/sources/catalog/gbif/async-download.md
  - ../../../docs/sources/catalog/gbif/dataset-metadata.md
  - ../../../docs/sources/catalog/gbif/backbone-taxonomy.md
  - ../../../docs/sources/catalog/gbif.md
  - ../../../docs/domains/fauna/README.md
  - ../../../docs/domains/flora/README.md
  - ../../../docs/domains/flora/CANONICAL_PATHS.md
  - ../../../docs/domains/habitat/README.md
  - ../../../data/registry/sources/
  - ../../../data/raw/fauna/
  - ../../../data/raw/flora/
  - ../../../data/raw/habitat/
  - ../../../data/quarantine/fauna/
  - ../../../data/quarantine/flora/
  - ../../../data/quarantine/habitat/
  - ../../../schemas/contracts/v1/source/
  - ../../../policy/sensitivity/
  - ../../../policy/rights/
  - ../../../release/
tags: [kfm, connectors, gbif, source-root, python, biodiversity, darwin-core, dwca, occurrence, specimen, taxonomy, backbone, rights, geoprivacy, source-admission, raw, quarantine, governance]
notes:
  - "Repository inspection confirms connectors/gbif/src/ contains this README and one package directory named gbif. That package contains an expanded v0.2 README, an empty __init__.py, a one-line fetch.py placeholder, and a placeholder descriptor.yaml."
  - "The adjacent pyproject.toml records only project name kfm-connector-gbif and version 0.0.0. No build backend, package discovery, supported Python version, dependencies, entry points, test configuration, install evidence, or stable import API is proved."
  - "The package-local descriptor has role and rights set to TBD and sensitivity_floor set to public. GBIF rights are dataset-specific and occurrence sensitivity can be elevated, so the public value is an unsafe placeholder, not authority or a public-safe default."
  - "Occurrence API, async download, dataset metadata, Backbone Taxonomy, aggregate products, and modeled assets are distinct product surfaces with different role, rights, replay, versioning, completeness, and validation requirements."
  - "The plants child is a documentation-only compatibility pointer. Shared GBIF source access and product behavior belong in the common package; Flora-, Fauna-, and Habitat-specific interpretation belongs downstream."
  - "No accepted product-specific SourceDescriptor, SourceActivationDecision, current access contract, executable fixture suite, live-test approval, or passing CI evidence is proved."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# GBIF Connector Source Root

> Evidence-grounded source-code boundary for a possible Global Biodiversity Information Facility connector package. The current root is a greenfield scaffold, not an operational integration. It does **not** prove installability, supported imports, current endpoint compatibility, rights enforcement, Darwin Core parsing, taxonomy replayability, sensitivity handling, lifecycle persistence, or publication capability.

<p>
  <img alt="Status: greenfield draft" src="https://img.shields.io/badge/status-greenfield__draft-yellow">
  <img alt="Implementation: placeholder only" src="https://img.shields.io/badge/implementation-placeholder__only-lightgrey">
  <img alt="Import: unsupported and unproved" src="https://img.shields.io/badge/import-unsupported__and__unproved-orange">
  <img alt="Rights: per dataset" src="https://img.shields.io/badge/rights-per__dataset-orange">
  <img alt="Sensitivity: fail closed" src="https://img.shields.io/badge/sensitivity-fail__closed-critical">
  <img alt="Network: off by default" src="https://img.shields.io/badge/network-off__by__default-critical">
  <img alt="Lifecycle: RAW or QUARANTINE candidates only" src="https://img.shields.io/badge/lifecycle-RAW%20%7C%20QUARANTINE%20candidates-orange">
  <img alt="Publication: forbidden" src="https://img.shields.io/badge/publication-forbidden-critical">
</p>

`connectors/gbif/src/`

> [!IMPORTANT]
> **Confirmed state:** this source root contains this README and one package-shaped directory, `gbif/`. The package contains an expanded v0.2 README, an empty `__init__.py`, a one-line `fetch.py` placeholder, and a placeholder `descriptor.yaml`. No implemented configuration model, product dispatcher, HTTP transport, async-job worker, dataset-metadata reader, Darwin Core or DwC-A parser, Backbone resolver, rights adapter, sensitivity detector, handoff builder, finite error contract, executable package test, or passing CI evidence is confirmed.

> [!CAUTION]
> `gbif/descriptor.yaml` contains `role: TBD`, `rights: TBD`, and `sensitivity_floor: public`. GBIF records inherit rights from originating datasets and may carry restricted-use, obscured, rare-species, culturally sensitive, or precise-location concerns. **The local `public` value is an unsafe placeholder. Source-root or package code must not load it as authority, use it as a permissive default, inherit it into domain records, authorize RAW admission from it, or encode it as an accepted test result.**

**Quick jumps:** [Purpose](#purpose) · [Verified repository state](#verified-repository-state) · [Evidence ledger](#evidence-ledger) · [Source-root authority boundary](#source-root-authority-boundary) · [Blocking drift](#blocking-drift) · [Source-root invariants](#source-root-invariants) · [Placement contract](#placement-contract) · [Shared package and plants child](#shared-package-and-plants-child) · [Product decomposition](#product-decomposition) · [Source-role boundary](#source-role-boundary) · [Access and input posture](#access-and-input-posture) · [Configuration and secret boundary](#configuration-and-secret-boundary) · [Rights license and citation](#rights-license-and-citation) · [Sensitivity and geoprivacy](#sensitivity-and-geoprivacy) · [Taxonomic anchoring and drift](#taxonomic-anchoring-and-drift) · [Temporal replay and correction boundaries](#temporal-replay-and-correction-boundaries) · [Darwin Core and metadata preservation](#darwin-core-and-metadata-preservation) · [Transport pagination jobs and archive bounds](#transport-pagination-jobs-and-archive-bounds) · [Packaging and import contract](#packaging-and-import-contract) · [Proposed source tree](#proposed-source-tree) · [Finite outcomes](#finite-outcomes) · [Lifecycle and handoff boundary](#lifecycle-and-handoff-boundary) · [Testing relationship](#testing-relationship) · [Responsibility separation](#responsibility-separation) · [Implementation sequence](#implementation-sequence) · [Activation gates](#activation-gates) · [Review and rollback](#review-and-rollback) · [Definition of done](#definition-of-done) · [Verification backlog](#verification-backlog)

---

## Purpose

`connectors/gbif/src/` is the source-code root for one possible shared GBIF connector package. Its purpose is to organize narrowly scoped, side-effect-free source-admission code without turning a provider integration into biodiversity truth, domain interpretation, policy, or publication authority.

When implementation exists, code below this root may:

- expose a small, reviewed Python API;
- accept explicit configuration rather than discover accounts, credentials, caches, or source files;
- require accepted product- and dataset-specific SourceDescriptors plus activation decisions before consequential behavior;
- dispatch one explicitly identified GBIF product at a time;
- accept synthetic fixtures, supplied API captures, supplied metadata documents, supplied Backbone metadata, or supplied DwC-A archives by default;
- support separately approved live transport only after source, rights, security, retention, logging, testing, and rollback review;
- preserve dataset, publisher, institution, license, citation, DOI, source-role, taxonomic-version, temporal, spatial, uncertainty, restriction, and completeness metadata;
- enforce bounded requests, pagination, polling, downloads, retries, redirects, archive extraction, row processing, memory, and execution time;
- detect unknown rights, additional restrictions, sensitive or obscured records, product-role conflicts, schema drift, taxonomy drift, partial captures, and unsafe lifecycle targets;
- return finite blocked, denied, abstained, held, error, RAW-candidate, or QUARANTINE-candidate results under accepted contracts;
- remain fully testable offline with synthetic fixtures.

This source root must never become:

- canonical occurrence, specimen, population, current-presence, absence, range, conservation-status, habitat, or taxonomic truth;
- a plant-only, animal-only, or habitat-only fork of GBIF source access;
- a mechanism for recovering withheld, obscured, rounded, or sensitive locations;
- source-registry, rights, sensitivity, policy, evidence, catalog, release, or publication authority;
- a store for payloads, private datasets, credentials, restricted records, temporary archives, caches, or lifecycle data;
- a direct writer to WORK, PROCESSED, CATALOG, TRIPLET, PROOF, RECEIPT, RELEASE, PUBLISHED, public API, map, graph, report, search, or generated-answer surfaces.

[Back to top ↑](#top)

---

## Verified repository state

The following scaffold is confirmed on the repository's default branch at the time of this update:

```text
connectors/gbif/
├── README.md                         # parent connector contract; earlier draft
├── pyproject.toml                    # project name + version 0.0.0 only
├── plants/
│   └── README.md                     # v0.2 documentation-only compatibility pointer
├── src/
│   ├── README.md                     # this source-root contract
│   └── gbif/
│       ├── README.md                 # v0.2 package contract
│       ├── __init__.py               # empty file
│       ├── descriptor.yaml           # role/rights TBD; unsafe public floor
│       └── fetch.py                  # one-line greenfield placeholder
└── tests/
    └── README.md                     # documentation-only test contract; earlier draft
```

### Current maturity

| Surface | Confirmed content | Maturity |
|---|---|---:|
| `src/README.md` | This source-root boundary. | **DOCUMENTED** |
| `src/gbif/README.md` | Evidence-grounded v0.2 package contract. | **DOCUMENTED** |
| `src/gbif/__init__.py` | Empty file. | **IMPORT-SHAPED / BEHAVIOR ABSENT** |
| `src/gbif/fetch.py` | Comment-only greenfield placeholder. | **PLACEHOLDER / NON-EXECUTABLE** |
| `src/gbif/descriptor.yaml` | `name: gbif`, `role: TBD`, `rights: TBD`, `sensitivity_floor: public`. | **PLACEHOLDER / UNSAFE DEFAULT** |
| `pyproject.toml` | Project name `kfm-connector-gbif` and version `0.0.0` only. | **INCOMPLETE** |
| Build backend | None confirmed. | **ABSENT** |
| `src/` package discovery | None confirmed. | **ABSENT** |
| Supported Python versions | None confirmed. | **ABSENT** |
| Runtime and development dependencies | None confirmed. | **ABSENT** |
| Console scripts or entry points | None confirmed. | **ABSENT** |
| Stable public import API | None confirmed. | **ABSENT** |
| Product dispatcher | None confirmed. | **ABSENT** |
| Occurrence API transport | None confirmed. | **ABSENT** |
| Async-download worker | None confirmed. | **ABSENT** |
| Dataset metadata and license handling | Documentation exists; implementation absent. | **PROPOSED / UNBOUND** |
| Darwin Core and DwC-A parsing | None confirmed. | **ABSENT** |
| Backbone version handling | Documentation exists; implementation absent. | **PROPOSED / UNBOUND** |
| Sensitivity/geoprivacy detection | Doctrine exists; implementation absent. | **PROPOSED / UNBOUND** |
| `plants/` child | README-only compatibility pointer. | **DOCUMENTED / NONCANONICAL IMPLEMENTATION PATH** |
| Connector-local executable tests | None confirmed. | **ABSENT** |
| Accepted product-specific SourceDescriptors | None found or verified. | **ABSENT / NEEDS VERIFICATION** |
| Source activation | No approved activation evidence found. | **NOT ACTIVATED** |
| Live tests | None confirmed or approved. | **ABSENT / NOT APPROVED** |
| Passing CI evidence | None confirmed. | **UNKNOWN / ABSENT** |

> [!CAUTION]
> A `src/` directory, empty initializer, source catalog, compatibility pointer, or detailed README can make this connector look mature. None proves that a build succeeds, imports are supported, endpoints still match documentation, rights are enforced, archives are safe, taxonomy is replayable, sensitivity controls work, tests pass, or the source is activated.

[Back to top ↑](#top)

---

## Evidence ledger

| Evidence | Status | What it supports | What it does not support |
|---|---:|---|---|
| `connectors/gbif/src/README.md` | **CONFIRMED** | A source-root documentation boundary exists. | Executable behavior or installability. |
| `connectors/gbif/src/gbif/README.md` | **CONFIRMED v0.2** | Package-level product, role, access, rights, sensitivity, taxonomy, replay, archive, packaging, testing, and handoff requirements are documented. | Implemented enforcement. |
| `src/gbif/__init__.py` | **CONFIRMED empty** | A package namespace was scaffolded. | Stable API, supported imports, or import safety. |
| `src/gbif/fetch.py` | **CONFIRMED placeholder** | A future source-input responsibility was anticipated. | Approved network access, retries, pagination, jobs, downloads, parsing, or persistence. |
| `src/gbif/descriptor.yaml` | **CONFIRMED unsafe placeholder** | Package-local metadata was anticipated. | Canonical descriptor authority, resolved roles/rights, safe sensitivity, or activation. |
| `connectors/gbif/pyproject.toml` | **CONFIRMED placeholder** | Distribution name and version are recorded. | Build backend, discovery, dependencies, Python support, installation, or tests. |
| `connectors/gbif/plants/README.md` | **CONFIRMED v0.2 compatibility pointer** | Plant-specific source access remains shared in the GBIF parent/package under the current posture. | Implemented plant filtering or active Flora ingestion. |
| `connectors/gbif/tests/README.md` | **CONFIRMED documentation** | Offline, rights, provenance, version, parser, and boundary-test intentions exist. | Executable tests, accepted live-test variables, passing results, or CI enforcement. |
| GBIF source-family and product pages | **CONFIRMED draft documentation** | Occurrence API, async download, dataset metadata, and Backbone are distinct products with different trust, replay, role, rights, and version properties. | Current endpoint compatibility or accepted runtime contracts. |
| `docs/sources/catalog/gbif.md` | **CONFIRMED draft source profile** | GBIF is an occurrence aggregator and taxonomic crosswalk with per-dataset rights and sensitivity gates. | Source activation or implemented policy. |
| Flora canonical-path documentation | **CONFIRMED doctrine-derived register** | `connectors/gbif/` is the shared source connector; domain interpretation belongs downstream. | Final taxonomy authority ordering or active Flora routes. |
| Package/source-root inventory | **CONFIRMED for inspected state** | The source root contains documentation and one behaviorless package scaffold. | Permanent absence of future implementation. |

[Back to top ↑](#top)

---

## Source-root authority boundary

```text
THIS SOURCE ROOT MAY EVENTUALLY CONTAIN:
  one reviewed shared GBIF Python package
  side-effect-free configuration and typed result models
  closed product definitions and product dispatch
  bounded supplied-input readers
  replaceable bounded transport helpers
  deterministic Darwin Core and DwC-A parsers
  dataset-metadata and Backbone-version preservation helpers
  connector-local validation and drift detection
  finite redacted error helpers
  RAW or QUARANTINE candidate-envelope builders

THIS SOURCE ROOT MUST NOT CONTAIN:
  canonical SourceDescriptors or activation decisions
  rights, sensitivity, taxonomy, or release policy authority
  source payloads, private datasets, credentials, caches, or lifecycle stores
  domain-specific canonical Flora, Fauna, or Habitat mapping authority
  exact-location recovery or public geoprivacy transforms
  EvidenceBundles, catalog records, graph/triplet records, or release artifacts
  public APIs, maps, reports, search indexes, or generated answers
```

An importable module is not source activation. A parsed source record is not biodiversity truth. A license string is not a release decision. A taxon key is not a final domain identity. A query result is not replay-stable evidence merely because it has a digest.

[Back to top ↑](#top)

---

## Blocking drift

Executable work must expose unresolved blockers rather than hide them behind permissive defaults, fixtures, aliases, or mocks.

| Blocker | Confirmed gap or conflict | Required source-root posture |
|---|---|---|
| Packaging | No build backend, discovery, Python support, dependencies, entry points, or stable API. | Do not claim installability or supported imports. |
| Local descriptor | Role and rights are `TBD`; sensitivity floor is `public`. | Reject as authority; require accepted external product/dataset descriptors. |
| Source registry topology | Canonical GBIF descriptor and per-dataset placement remain unresolved. | Require one accepted descriptor reference; do not select a path by convenience. |
| Product identity | Occurrence API, async download, metadata, Backbone, aggregates, and modeled assets differ materially. | Require explicit closed product dispatch; no umbrella parser or provider-wide activation. |
| Product source roles | Occurrences, specimens, metadata, taxonomy, aggregates, and modeled assets use different roles. | Require product/dataset-specific roles; reject family-wide defaults and role upgrades. |
| Per-dataset rights | GBIF aggregates independently licensed and sometimes additionally restricted datasets. | Preserve rights at actual dataset/record granularity; unknown or conflicting rights fail closed. |
| Occurrence API replay | Synchronous results can change and do not inherently supply a Download DOI. | Preserve query, pagination, retrieval, response, and dataset evidence; do not claim publication-grade replayability. |
| Async download | Authentication, predicate, polling, terminal-state, retention, checksum, DOI, and archive behavior is unimplemented. | No live job submission; supplied/synthetic archive tests first. |
| Dataset metadata | License, citation, publisher, DOI, restrictions, and update semantics are unimplemented. | No release-bound candidate without complete source context. |
| Darwin Core / DwC-A | Field, encoding, delimiter, archive, extension-table, and version behavior is unverified. | No best-effort parsing; schema and archive drift remain visible. |
| Backbone version | Snapshot discovery, rotation, taxon-key stability, and correction behavior are unimplemented. | Require explicit version context; never silently resolve against latest. |
| Taxonomy authority order | GBIF, ITIS, USDA PLANTS, NatureServe, and local authorities can disagree. | Preserve identifiers independently; keep tie-breaking downstream. |
| Sensitive records | Rare, protected, obscured, steward-controlled, cultural, or precise-location records require policy. | Preserve restrictions and fail closed; no exact-location release transform here. |
| Join-induced sensitivity | Public metadata can become harmful when joined with roads, parcels, access, ownership, infrastructure, or cultural-use context. | Do not perform cross-source joins in the connector. |
| `plants/` child | The child is README-only and explicitly compatibility-oriented. | Keep implementation, descriptors, activation, tests, fixtures, and credentials in shared parent/owning lanes. |
| Handoff contract | No binding connector-result or RAW/QUARANTINE envelope is selected. | Do not invent an authoritative envelope or write lifecycle stores. |
| Tests | Test lane contains documentation only. | Do not claim parser, rights, sensitivity, replay, archive, or boundary coverage. |
| Live tests | No marker, variable, credential mode, endpoint contract, or approval exists. | No live-test implementation or command. |
| CI | No connector-specific workflow or passing run is confirmed. | No passing badge or merge-enforcement claim. |

These blockers are safety and evidence requirements, not inconveniences to bypass for a green demonstration.

[Back to top ↑](#top)

---

## Source-root invariants

Any future code below this root must preserve all of these invariants:

1. **Source code only.** Payloads, credentials, canonical descriptors, policy, evidence, release records, and lifecycle data stay outside this root.
2. **No import side effects.** Import performs no network access, DNS, account discovery, secret reads, filesystem writes, logging configuration, environment mutation, cache initialization, registry mutation, policy evaluation, or activation.
3. **No live behavior by default.** Synthetic fixtures or explicit supplied captures are the default paths until live access is independently approved.
4. **One product at a time.** Product identity is explicit and closed; no URL-, filename-, extension-, content-type-, first-row-, or field-guess dispatch.
5. **Descriptor-driven activation.** Code consumes accepted source authority; it never creates, infers, or self-activates it.
6. **Product roles remain fixed.** Parsing cannot upgrade administrative taxonomy, aggregate counts, or modeled ranges into observed occurrences.
7. **Per-dataset rights remain attached.** A provider-wide license assumption is forbidden.
8. **Rights, sensitivity, source role, evidence, and release remain separate gates.** Clearing one never clears another.
9. **Source obscuration remains intact.** Code never reverses, enriches, or guesses withheld coordinates or fields.
10. **No sensitive logging.** Exact sensitive coordinates, restricted fields, collector contacts, credentials, private predicates, and payload excerpts stay out of logs and errors.
11. **No source-root-owned credentials.** Passwords, tokens, sessions, cookies, API keys, account files, and keychain access remain external.
12. **No taxonomy sovereignty.** Code preserves taxonomic evidence and versions but does not decide the final KFM taxon.
13. **No biological absence inference.** Empty or filtered results do not prove absence or survey non-detection.
14. **No current-presence inference from specimens.** Historical collection evidence retains its event date and `basisOfRecord` meaning.
15. **No cross-source joins.** Taxonomy, conservation status, parcel, access, infrastructure, cultural-use, and ownership joins are downstream responsibilities.
16. **No publication transform.** Redaction, generalization, aggregation, evidence closure, release, correction, and rollback remain downstream.
17. **Finite outcomes only.** Every operation ends in a bounded, reviewable result; no silent partial success or best-effort acceptance.
18. **RAW or QUARANTINE candidate only.** Source-root code does not persist lifecycle stores.
19. **No false replayability claim.** A query hash or response digest does not equal a citable GBIF Download DOI.
20. **No false public-safety claim.** Public availability, a license string, coordinate rounding, or a taxon name does not automatically make a record safe to release.
21. **No consumer-domain fork.** Flora, Fauna, and Habitat consume lineage-preserving candidates from one shared GBIF source package.
22. **No false secure-erasure claim.** Code may minimize retention and request cleanup but must not promise memory or filesystem erasure beyond proved runtime and storage controls.

[Back to top ↑](#top)

---

## Placement contract

### Allowed below `src/`

Future accepted source-code content may include:

- the reviewed shared import package;
- package-level README files;
- side-effect-free configuration and typed result models;
- closed product definitions and dispatch;
- bounded supplied-input readers;
- replaceable bounded HTTP/download transport;
- deterministic occurrence-API, metadata, Backbone, Darwin Core, and DwC-A handling;
- connector-local checksum, completeness, pagination, job-state, archive, role, rights-metadata, sensitivity-flag, and drift checks;
- finite redacted errors;
- handoff-candidate builders that target only accepted RAW or QUARANTINE contracts;
- tiny non-sensitive package resources only when packaging review approves them;
- source-code tests only if the repository standard explicitly colocates them, which is not the current documented posture.

### Forbidden below `src/`

| Do not place here | Correct authority or handling |
|---|---|
| Canonical SourceDescriptors or activation decisions | Accepted source registry and activation workflow. |
| Rights, sensitivity, geoprivacy, taxonomy tie-breaker, or release rules | `policy/`, domain doctrine, and release authority. |
| JSON Schema or semantic contract authority | `schemas/` and `contracts/`. |
| Source API responses, DwC-A archives, metadata snapshots, Backbone mirrors, or private datasets | Approved lifecycle storage or quarantine, never source control. |
| Rare, protected, obscured, private-property, culturally sensitive, or precise-location fixtures | Governed fixture authority only after review; default is synthetic. |
| Passwords, tokens, cookies, sessions, account state, API keys, or keychain data | Secret and credential-management systems. |
| Temporary source caches, extracted archives, retry queues, or download staging | Explicit restricted runtime storage with retention and cleanup controls. |
| Source registry, policy, proof, catalog, receipt, release, or public data | Owning responsibility roots. |
| Canonical Flora, Fauna, or Habitat objects and crosswalk decisions | Domain packages, pipelines, contracts, schemas, policy, and review. |
| Public maps, biodiversity claims, taxon conclusions, absence claims, reports, search payloads, or generated answers | Governed downstream evidence, policy, release, and application surfaces. |

[Back to top ↑](#top)

---

## Shared package and plants child

The current repository posture supports one source-first GBIF implementation package and a documentation-only plant-consumer pointer.

| Surface | Current role | Must not become |
|---|---|---|
| `connectors/gbif/src/gbif/` | Shared GBIF package boundary for provider-level products and source semantics. | Flora-, Fauna-, or Habitat-specific fork, policy engine, or publisher. |
| `connectors/gbif/plants/` | Compatibility pointer and plant-consumer warning surface. | Client, parser, descriptor, activation, credential, fixture, test, or lifecycle authority. |
| `connectors/gbif/tests/` | Shared connector-local offline tests when implemented. | Plant-only transport suite or domain truth test root. |
| Flora/Fauna/Habitat packages and pipelines | Downstream source-to-domain mapping, crosswalks, validation, sensitivity routing, and derivatives. | Duplicate GBIF source downloads or inherit activation from package adjacency. |

Plant relevance, animal relevance, or habitat relevance determines downstream consumers; it does not create a new source identity or duplicate transport.

Any future proposal to split provider behavior by consumer domain requires an accepted ADR or migration decision covering:

- package and ownership boundaries;
- product dispatch and shared code;
- descriptors and activation;
- credential and transport ownership;
- fixtures and tests;
- RAW/QUARANTINE routing;
- data migration and lineage;
- backlinks and compatibility paths;
- correction, rollback, and deprecation.

[Back to top ↑](#top)

---

## Product decomposition

GBIF is one source family with multiple materially different products. The labels below are descriptive documentation terms, not accepted runtime enum values.

| Product surface | Source meaning | Minimum future source-root behavior | Forbidden shortcut |
|---|---|---|---|
| Synchronous occurrence API | Query-time, paginated occurrence search; mutable over time and not inherently DOI-pinned. | Preserve normalized query, retrieval time, pagination evidence, response digests, product identity, and dataset metadata references. | Treating a current API response as replay-stable publication evidence. |
| Asynchronous occurrence download | Predicate-defined bulk subset with job lifecycle, downloadable archive, and download citation identity when supplied. | Preserve request digest, job states, Download DOI, checksum, size, archive structure, dataset composition, and completion evidence. | Treating job submission as capture completion or ignoring failed/partial terminal states. |
| Dataset metadata | Publisher, institution, license, citation, DOI, rights holder, restrictions, update, and provenance context. | Consume or retrieve metadata before release-bound admission; preserve conflicts and missing fields. | Treating metadata as an occurrence or assuming one license covers every row. |
| Backbone Taxonomy | Versioned administrative taxonomic anchor and international crosswalk. | Preserve concept identity, snapshot/version, taxon keys, accepted-name references, status, and drift. | Emitting Backbone rows as occurrences or silently resolving against latest. |
| Aggregate occurrence product | Roll-up over a named spatial and temporal unit. | Preserve aggregation unit, time window, method, counts, source composition, and role. | Downscaling an aggregate into point or site-level truth. |
| Modeled range or suitability asset | Model-derived geographic context hosted or referenced through a GBIF-related surface. | Preserve modeled role, model identity, run/version reference, uncertainty, and source asset identity. | Upgrading a model to observed presence. |
| Unknown or combined surface | Product identity, rights, roles, formats, and replay guarantees are unresolved. | Reject, hold, or quarantine with an actionable unsupported-product result. | Best-effort parsing or provider-wide activation. |

Every product requires independent review of source role, authority, access method, rights, sensitivity, versioning, completeness, fixtures, tests, and activation.

[Back to top ↑](#top)

---

## Source-role boundary

The provider family may be described as an aggregator, but KFM's canonical source-role value must be assigned to the specific admitted artifact.

| Artifact | Expected role posture | Required distinction |
|---|---|---|
| Preserved specimen record | Usually `observed`, subject to accepted descriptor. | Collection evidence at collection time, not current presence. |
| Field or community observation | Usually `observed`, subject to accepted descriptor and source caveats. | Preserve identification confidence, verification state, and source quality. |
| Dataset metadata | `administrative`. | Describes a dataset; not occurrence evidence. |
| Backbone Taxonomy | `administrative`. | Taxonomic anchor/crosswalk with no event or locality. |
| Aggregated counts or cells | `aggregate`. | Aggregation unit and time scope are mandatory. |
| Modeled range or suitability | `modeled`. | Model/run evidence and uncertainty remain attached. |
| Unresolved record or product | Blocked or candidate under an accepted contract. | No permissive default. |

Future source-root code must:

- require accepted product- and dataset-specific SourceDescriptors;
- preserve the exact assigned role and role authority;
- reject absent, ambiguous, umbrella, or incompatible roles;
- never upgrade or downcast roles during parsing, validation, handoff, or downstream promotion;
- distinguish source observation, specimen, administrative metadata, taxonomic anchor, aggregate, and model output;
- preserve `basisOfRecord`, occurrence status, identification qualifiers, source caveats, aggregation scope, and model references where supplied;
- require a reviewed descriptor revision or correction record for a role correction;
- prohibit a generic `gbif -> observed` constant.

A Backbone row is not an occurrence. An aggregate cell is not a point record. A modeled range is not an observation. A specimen is not proof of current presence.

[Back to top ↑](#top)

---

## Access and input posture

### Current safe posture

The package has no implemented client and no approved live access contract.

```text
network access: disabled
GBIF account access: disabled
credential discovery: forbidden
background polling or download jobs: forbidden
input: explicit synthetic fixture, supplied response, supplied metadata, or supplied archive
persistence: none by default
output: finite blocked/held/error result or accepted RAW/QUARANTINE candidate
```

`gbif/fetch.py` is a placeholder filename, not an architecture decision or evidence that fetching is implemented or permitted.

### Future access modes

A reviewed implementation may support separately activated modes such as:

- supplied occurrence-API response;
- supplied DwC-A archive;
- supplied dataset-metadata document;
- supplied Backbone snapshot metadata;
- approved synchronous API transport;
- approved asynchronous download transport;
- approved metadata and Backbone lookup transport.

Each live mode requires explicit product identity, SourceDescriptor, activation, host allowlisting, current terms review, credential architecture where needed, limits, retention, logging controls, fixtures, tests, and rollback.

### Prohibited access behavior

- guessed or undocumented endpoints;
- implicit environment-variable credential reads;
- home-directory, browser, keychain, or config-file account discovery;
- provider-wide crawling;
- unbounded pagination or polling;
- hidden retries or fallback to another product surface;
- automatic fixture refresh;
- accepting a URL, DOI, dataset key, or provider label as activation evidence;
- treating HTTP success as rights, sensitivity, completeness, or publication approval;
- importing source data during package import, test collection, or documentation build;
- hidden persistence, caches, retry queues, or temporary archives.

[Back to top ↑](#top)

---

## Configuration and secret boundary

Once binding contracts are selected, a package operation should require explicit values equivalent to:

- canonical source descriptor reference;
- SourceActivationDecision reference;
- exact product key;
- source family and source ID;
- access mode: supplied fixture/capture or separately approved live transport;
- request, query, or predicate specification plus normalized digest where applicable;
- dataset allowlist or explicit dataset scope;
- domain route candidates such as Flora, Fauna, Habitat, or another accepted consumer;
- source role and role authority from the accepted descriptor;
- rights, license, citation, and additional-restriction requirements;
- sensitivity and restricted-record handling reference;
- Backbone concept and snapshot/version reference where applicable;
- expected content type, format, encoding, compression, and schema/version;
- expected checksum, content length, page count, record count, or archive manifest where known;
- timeout, retry, redirect, rate-limit, pagination, polling, job-duration, download-size, archive, row, memory, and processing limits;
- an external credential-provider reference for approved modes, never raw credentials in configuration;
- temporary-storage and cleanup instructions owned by orchestration/runtime;
- intended lifecycle target of QUARANTINE or, only when every admission gate closes, RAW.

Required behavior:

- reject missing or ambiguous product, source, role, dataset, rights, version, or lifecycle identity;
- reject missing descriptor or activation evidence for live or real-input paths;
- reject unknown, mixed, unsupported, or non-admitted products;
- reject product/role/authority mismatches;
- reject release-bound candidates with missing dataset citation or rights context;
- keep synthetic and test configuration unable to fall through to live access;
- never dispatch from URL, filename, extension, first row, content type, or provider label alone;
- document no endpoint, environment-variable name, credential convention, marker, or live command as accepted until implementation and review establish it.

Secrets, tokens, account state, and credentials remain outside this source root. The package may accept an opaque credential-provider capability only after the access mode is approved.

[Back to top ↑](#top)

---

## Rights, license, and citation

GBIF aggregates records from many originating datasets. Rights must remain attached at the actual source granularity.

Future code should preserve, where supplied:

- dataset key, title, publisher, and publishing organization;
- originating institution and collection;
- rights holder;
- raw license value and normalized license interpretation;
- citation and attribution text;
- dataset DOI or citation identifier;
- GBIF Download DOI for a bulk subset;
- source references and distribution identity;
- additional use restrictions, embargoes, withholding, or restricted-use notes;
- rights-review state and external policy-decision reference;
- retrieval time and terms snapshot reference when required by the accepted descriptor.

Source-root posture:

| Rights condition | Required behavior |
|---|---|
| License and citation complete | Preserve them; continue only when descriptor and policy references permit. |
| Attribution required | Preserve exact source attribution and dataset citation. |
| Share-alike or derivative conditions present | Flag for downstream release review; do not interpret compatibility locally. |
| Additional dataset-specific restrictions present | Preserve and elevate them; generic license parsing cannot override them. |
| License missing, unknown, conflicting, or unparseable | `DENY`, `ABSTAIN`, `HOLD`, or QUARANTINE candidate. |
| Dataset identity or publisher missing | No release-bound candidate. |
| Per-record and dataset-level rights disagree | Preserve both and route to review. |

Source-root code may parse and carry rights metadata. It does not decide legal sufficiency, fair use, redistribution, derivative compatibility, or public release.

[Back to top ↑](#top)

---

## Sensitivity and geoprivacy

Public availability does not make every GBIF record safe to redistribute, combine, or publish.

### Sensitive or restricted classes

- rare, imperiled, protected, or steward-controlled taxa;
- nest, den, roost, hibernaculum, spawning, breeding, collection, seed-source, or small-population locations;
- records already obscured, rounded, generalized, withheld, embargoed, or marked sensitive upstream;
- culturally or sovereignty-sensitive plant, animal, habitat, or traditional-use knowledge;
- collector, observer, contact, permit, landowner, or private-property context;
- exact locations joined with parcels, roads, trails, access points, infrastructure, ownership, or harvesting/use information;
- records whose sensitivity status cannot be evaluated;
- products where individually ordinary fields combine into actionable location intelligence.

### Required source-root posture

1. Preserve upstream obscuration, uncertainty, withholding, and precision exactly as received.
2. Never attempt to recover exact coordinates from an obscured or withheld record.
3. Route unresolved sensitivity to denial, abstention, hold, or quarantine.
4. Keep exact sensitive geometry out of source control, fixtures, package data, logs, errors, metrics, and ordinary outputs.
5. Emit restricted/sensitive flags and external policy references; do not perform public redaction or generalization locally.
6. Never rely on map styling, hidden layers, client filters, opacity, or zoom thresholds as sensitivity controls.
7. Recalculate sensitivity downstream after joins.
8. Preserve cultural, sovereignty, stewardship, and source-specific restrictions even when ordinary metadata is public.
9. Keep generated summaries, vector indexes, embeddings, and AI responses subordinate to the same restrictions.
10. Require correction and rollback support for released derivatives whose sensitivity posture later changes.

Hashing, rounding, coordinate removal, or a public license does not by itself establish anonymization or public safety.

[Back to top ↑](#top)

---

## Taxonomic anchoring and drift

This source root preserves taxonomic evidence; it does not choose final domain taxonomy.

Repository documentation currently identifies several relevant authority surfaces:

- GBIF Backbone as a versioned international crosswalk;
- ITIS as a U.S.-oriented taxonomic anchor in existing biodiversity doctrine;
- USDA PLANTS as a proposed Flora-specific taxonomic backbone;
- NatureServe, state authorities, herbaria, museums, and local accepted sources as additional evidence;
- domain-level crosswalk and tie-breaker policy as downstream responsibilities.

Required posture:

- preserve source `scientificName`, verbatim names, taxon keys, accepted-name references, rank, status, and issue flags where supplied;
- preserve the exact Backbone concept and snapshot/version context used during resolution;
- keep GBIF, ITIS, USDA PLANTS, NatureServe, state, institutional, and local identifiers independently inspectable;
- do not silently replace source names with a preferred domain name;
- do not discard synonyms, unresolved names, higher-rank matches, or disagreement evidence;
- treat taxon merges, splits, synonym changes, rank changes, and deprecations as taxonomy drift;
- require downstream `TaxonCrosswalk` or `FloraTaxonCrosswalk` evidence for canonical identity;
- abstain or route to review when no accepted anchor resolves;
- never resolve against “latest Backbone” when a replayable snapshot is required;
- never implement a Flora/Fauna/Habitat tie-breaker policy inside the shared connector.

A taxon key without its applicable Backbone version is incomplete replay evidence.

[Back to top ↑](#top)

---

## Temporal, replay, and correction boundaries

Keep these time and replay concepts distinct:

| Concept | Meaning | Source-root guardrail |
|---|---|---|
| Event or collection time | When an organism was observed, collected, or sampled. | Preserve source precision and uncertainty; do not replace with retrieval time. |
| Identification time | When a record was identified or reidentified. | Reidentification is not a new biological event. |
| Source-record modification time | When the upstream record changed. | Preserve separately from event time. |
| Dataset publication/update time | When the dataset or distribution changed. | Preserve for staleness and version review. |
| API retrieval time | When a synchronous response was obtained. | Required; API results can change between calls. |
| Async job submission/completion time | When a bulk request entered and left the source job lifecycle. | Preserve both; submission does not equal successful capture. |
| Download DOI or subset identity | Citation identity for a completed bulk subset when supplied. | Preserve independently from Backbone DOI and dataset citations. |
| Backbone snapshot/version time | Taxonomic frame used for resolution. | Version drift is taxonomy drift, not occurrence time. |
| KFM release time | When a downstream derivative was released. | Outside connector authority. |
| Correction/supersession time | When source or KFM evidence was corrected or replaced. | Never silently overwrite prior evidence. |

### Synchronous API replay posture

A synchronous API response is not inherently replay-stable. Future capture metadata should include:

- normalized request/query specification and digest;
- retrieval timestamp;
- requested and received page ranges;
- response and page digests;
- ETag or Last-Modified when supplied;
- total, count, and end-of-records indicators where supplied;
- duplicate, gap, partial, retry, and ordering evidence;
- dataset composition and metadata references;
- Backbone snapshot/version context;
- explicit product/source-surface identity.

A cached response or digest documents what KFM received. It does not mint a GBIF Download DOI or independently authorize publication.

### Correction posture

- upstream record changes produce new source states rather than silent mutation;
- dataset withdrawal or license change remains visible;
- Backbone rotation does not invalidate prior receipts by rewriting them;
- material changes to coordinates, taxon identity, rights, sensitivity, or dataset membership trigger downstream review and possible invalidation;
- source-root code may emit correction or drift references but does not update released artifacts itself.

[Back to top ↑](#top)

---

## Darwin Core and metadata preservation

Parsers must preserve source meaning before downstream normalization.

### Source and product minimum

- canonical source ID and SourceDescriptor reference;
- product surface and access mode;
- SourceActivationDecision reference;
- source role and role authority;
- dataset key, title, publisher, institution, collection, and citation identity;
- download key and GBIF Download DOI where applicable;
- Backbone concept and snapshot/version reference;
- request/query/predicate identity and digest where applicable;
- retrieval/import timestamp, checksum, and connector/parser version;
- license, attribution, rights-holder, restriction, and review state;
- intended domain route and lifecycle target;
- drift, partial, restricted, obscured, quarantined, and review flags.

### Occurrence and specimen minimum

Preserve where supplied and permitted:

- source occurrence identifier;
- `basisOfRecord` or equivalent source class;
- institution, collection, and catalog identifiers;
- event/collection date and temporal precision;
- scientific name, verbatim name, taxon keys, accepted-name reference, rank, and taxonomic status;
- identification qualifier, confidence, verification status, issues, and source caveats;
- occurrence status, establishment means, life stage, sex, behavior, and cultivation/captive qualifiers without inference;
- individual count or quantity with units and semantics;
- locality and jurisdiction fields;
- decimal coordinates, geodetic datum, coordinate uncertainty, precision, georeference remarks, and issue flags;
- source-obscured, withheld, generalized, or restricted status;
- collector/observer fields only under accepted privacy handling;
- source field names, code values, null/unknown semantics, and unsupported-field evidence.

### Dataset and capture minimum

- dataset metadata retrieval state;
- expected and received pages, files, archive members, extension tables, rows, or records where available;
- accepted, rejected, quarantined, duplicate, and unresolved counts;
- archive manifest and extraction state;
- checksum and content-size verification;
- partial, truncated, interrupted, stale, or superseded state;
- unknown field, type, encoding, delimiter, code-list, schema, and taxonomic-version drift evidence.

Unknown fields may be preserved only through an accepted restricted passthrough contract. They must not be silently dropped, guessed into KFM semantics, or exposed publicly.

[Back to top ↑](#top)

---

## Transport, pagination, jobs, and archive bounds

Any future transport or supplied-input reader must be bounded and replaceable.

### HTTP and transport controls

- explicit host and scheme allowlist;
- explicit connect, read, total, and idle timeouts;
- bounded retries with documented retryable conditions;
- bounded redirects with host revalidation;
- response-size and decompression limits;
- content-type, encoding, and compression validation;
- rate-limit and backoff handling without infinite waits;
- redacted request and response errors;
- no credential values in URLs, logs, exceptions, metrics, or receipts;
- injectable transport for offline tests;
- no automatic persistence of response bodies.

### Occurrence API pagination controls

- explicit page size and maximum pages/records;
- stable normalized query across pages;
- expected offset or cursor progression;
- duplicate occurrence-ID detection;
- gap and inconsistent-total detection;
- end-of-records validation where supplied;
- page digest and retrieval evidence;
- no partial success when required pages fail;
- bounded recovery from rate limits and transient errors;
- drift outcome when pagination semantics change.

### Async-job controls

- explicit predicate and product descriptor;
- bounded submission and polling duration;
- bounded poll frequency and retry count;
- explicit terminal-state vocabulary under an accepted contract;
- no assumption that a job key means success;
- Download DOI or citation identity, size, checksum, and completion metadata required before capture success;
- failed, cancelled, expired, inaccessible, or inconsistent jobs return finite outcomes;
- no background daemon or unbounded polling in the package;
- credentials remain external and scoped to the approved action.

### DwC-A and archive controls

Required negative handling includes:

- archive larger than accepted byte limit;
- expanded size or compression ratio above limit;
- excessive member count or nesting;
- traversal paths, absolute paths, symlinks, hardlinks, devices, or special files;
- duplicate or conflicting member names;
- missing or malformed metadata/manifest files;
- unexpected delimiter, quote, escape, encoding, line ending, or field count;
- missing core table or broken extension-table references;
- checksum mismatch or truncated stream;
- unsupported archive or compression format;
- unknown required fields or incompatible schema version;
- formula-like, script-like, HTML, or executable content treated as active material;
- partial table success after another required table fails.

Source bytes remain inert data. Code must never execute archive contents, formulas, macros, scripts, or imported source material.

[Back to top ↑](#top)

---

## Packaging and import contract

The current project metadata is not sufficient to build, install, or publish a supported package.

Before this source root is described as installable or importable in a supported sense:

- declare a build backend;
- declare package discovery for the `src/` layout;
- declare supported Python versions;
- declare runtime and development dependencies;
- define versioning beyond `0.0.0`;
- define package-data policy and prevent automatic authority-loading from `descriptor.yaml`;
- define the narrow public API exported from `gbif/__init__.py`;
- add clean-environment source-distribution, wheel, installation, and import tests;
- verify built artifacts exclude real fixtures, source payloads, credentials, restricted records, caches, and canonical registry data;
- ensure imports perform no network, DNS, secret, filesystem, logging, environment, cache, registry, policy, or activation side effects;
- ensure optional transport and parser dependencies are not imported until needed;
- ensure source catalog documentation is not packaged as runtime authority;
- define stable errors and result types only after the connector-result contract is accepted.

The package-local descriptor must not be imported automatically. It should be removed, converted into an unmistakable non-authoritative pointer or invalid fixture, or guarded by a reviewed packaging decision that makes runtime consumption impossible.

[Back to top ↑](#top)

---

## Proposed source tree

The confirmed source tree is minimal:

```text
src/
├── README.md
└── gbif/
    ├── README.md
    ├── __init__.py        # empty
    ├── descriptor.yaml    # placeholder, not authority
    └── fetch.py           # one-line placeholder
```

A future shared product-oriented source tree might use a structure like:

```text
src/
├── README.md
└── gbif/
    ├── README.md
    ├── __init__.py
    ├── config.py
    ├── products.py
    ├── transport.py
    ├── occurrence_api.py
    ├── async_download.py
    ├── dataset_metadata.py
    ├── backbone.py
    ├── dwc.py
    ├── dwca.py
    ├── rights_refs.py
    ├── sensitivity_flags.py
    ├── validate.py
    ├── handoff.py
    └── errors.py
```

This tree is **PROPOSED**, not implementation evidence. Do not create it mechanically. A module should exist only when its responsibility, contract, product descriptor, owner, fixtures, tests, and review posture are accepted.

| Future module | Responsibility | Must not become |
|---|---|---|
| `config.py` | Explicit side-effect-free configuration and bounded limits. | Secret discovery, activation authority, or live fallback. |
| `products.py` | Closed product identifiers and product-specific requirements. | SourceDescriptor authority or consumer-domain routing policy. |
| `transport.py` | Replaceable bounded HTTP/download transport. | Parsing policy, rights decisions, or hidden credentials. |
| `occurrence_api.py` | Query normalization, bounded pagination, and response-capture metadata. | Publication evidence authority or biological absence logic. |
| `async_download.py` | Bounded job lifecycle and archive retrieval under approved access. | Background daemon, unbounded polling, or release authority. |
| `dataset_metadata.py` | Preserve dataset, publisher, license, citation, DOI, and restrictions. | Legal decision engine. |
| `backbone.py` | Preserve Backbone concept/snapshot identity and taxonomic drift. | Final taxonomy tie-breaker. |
| `dwc.py` | Deterministic Darwin Core field parsing and source-shape preservation. | Canonical domain-object mapping. |
| `dwca.py` | Bounded archive, manifest, core-table, and extension-table reading. | Arbitrary archive extraction or lifecycle storage. |
| `rights_refs.py` | Carry rights metadata and external decision references. | Policy or legal authority. |
| `sensitivity_flags.py` | Detect source restriction/obscuration flags and return bounded findings. | Public redaction, de-obscuration, or release classification. |
| `validate.py` | Connector-local product, version, completeness, checksum, role, and drift checks. | Domain truth, taxonomy authority, or release approval. |
| `handoff.py` | Build accepted finite results and RAW/QUARANTINE candidates. | Direct persistence, downstream promotion, or publication. |
| `errors.py` | Small deterministic redacted error taxonomy. | Payload excerpts or unbounded exception detail. |

[Back to top ↑](#top)

---

## Finite outcomes

Future package APIs and tests should use a small accepted result vocabulary. Exact names remain unbound until a connector-result contract is selected.

| Condition | Required safe behavior |
|---|---|
| Package behavior absent | Clear unavailable/not-implemented result; never false success. |
| Build or supported import contract absent | Do not claim package readiness or import coverage. |
| Canonical source or product descriptor missing | Activation blocked. |
| Package-local `sensitivity_floor: public` encountered | Hard placeholder-validation failure. |
| Activation decision missing | `ABSTAIN` or activation-blocked result. |
| Product identity missing, unknown, or mixed | Validation failure, `HOLD`, or QUARANTINE candidate. |
| Source role missing or conflicted | Activation block; no permissive default. |
| Dataset identity, publisher, citation, or rights context missing | Hold or quarantine; no release-bound candidate. |
| License or additional terms unknown or conflicting | `DENY`, `ABSTAIN`, `HOLD`, or QUARANTINE candidate. |
| Network requested under default configuration | Bounded disabled outcome. |
| Credential discovery or unsafe credential handling attempted | Hard security failure. |
| API pagination incomplete, duplicated, or inconsistent | Incomplete-capture quarantine. |
| API response lacks replay evidence required by contract | `ABSTAIN`, `HOLD`, or non-release-bound candidate. |
| Async job not terminal-successful or download metadata incomplete | Finite failed/incomplete outcome. |
| Download checksum or content-size mismatch | Incomplete-capture quarantine. |
| Archive unsafe, malformed, oversized, or structurally incomplete | Reject or quarantine. |
| Dataset metadata unavailable | Rights/provenance block. |
| Backbone snapshot/version absent where anchoring occurs | Taxonomy-review or quarantine outcome. |
| Taxon key/name/rank/version drift | Reviewable taxonomy-drift result; no silent rewrite. |
| Sensitive, obscured, or restricted record detected | Restrict, hold, deny, or quarantine; never public-safe by default. |
| Attempt to recover exact withheld geometry | Hard sensitivity-boundary failure. |
| Aggregate emitted as point occurrence | Hard source-role failure. |
| Modeled asset emitted as observed occurrence | Hard source-role failure. |
| Specimen emitted as current presence | Hard temporal/semantic failure. |
| Empty result interpreted as biological absence | Hard evidence-boundary failure. |
| Sensitive value enters log, error, metric, snapshot, or ordinary output | Hard privacy failure. |
| Intended target beyond RAW or QUARANTINE | Hard authority-boundary failure. |
| Direct lifecycle or public write attempted | Hard failure. |
| Taxonomic, conservation-status, absence, range, legal, safety, or release determination requested | Refuse and route to governed domain/reviewer processes. |

Every error must be deterministic, finite, actionable, safe to log, and free of unnecessary source content.

[Back to top ↑](#top)

---

## Lifecycle and handoff boundary

The source root participates only at the source-admission edge and performs no lifecycle write by itself.

```mermaid
flowchart TD
    I[Explicit synthetic fixture supplied capture or approved GBIF product request] --> D{Product descriptor and activation approved?}
    D -- No --> X[ABSTAIN / DENY / activation blocked]
    D -- Yes --> P{Role rights product version and domain route pinned?}
    P -- No --> H[HOLD / QUARANTINE candidate]
    P -- Yes --> T[Bounded supplied-input reader or approved transport]
    T --> V[Validate completeness metadata rights sensitivity and drift]
    V --> S{Restricted obscured partial or conflicting?}
    S -- Yes --> Q[DENY / HOLD / QUARANTINE candidate]
    S -- No --> O{Accepted handoff target?}
    O -- QUARANTINE --> Q2[QUARANTINE candidate envelope]
    O -- RAW --> R[RAW candidate envelope]
    O -- downstream or public --> F[Hard source-root boundary failure]
    R --> G[Governed Flora Fauna or Habitat processing outside source root]
    Q2 --> G
    G --> E[Domain mapping policy evidence catalog release correction rollback]

    C[connectors/gbif/plants compatibility pointer]:::hold
    C -. no runtime split .-> G

    L[Local descriptor public floor]:::deny
    L -. invalid placeholder .-> X

    classDef deny fill:#fee,stroke:#b30000,color:#7f1d1d;
    classDef hold fill:#fff8c5,stroke:#9a6700,color:#5c4400;
    class X,F,L deny;
    class H,Q,Q2,C hold;
```

The diagram defines responsibility boundaries. It does not prove transport, parsing, rights evaluation, sensitivity policy, taxonomy resolution, RAW storage, quarantine storage, domain pipelines, evidence closure, release, or cleanup.

KFM lifecycle discipline remains:

```text
RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED
```

Source-root code may eventually construct an accepted candidate envelope. It must not persist source payloads or perform later transitions.

[Back to top ↑](#top)

---

## Testing relationship

Connector-local tests belong under `connectors/gbif/tests/`. That directory currently contains documentation only.

No test dependency, executable test module, fixture set, collection configuration, accepted local command, live-test marker, environment-variable convention, CI job, coverage result, or passing status is confirmed.

> [!CAUTION]
> `KFM_ALLOW_LIVE_GBIF_TESTS` appears in the current test README as an illustrative convention. It is **not accepted** by this source-root contract. No live-test variable, marker, credential mode, account, endpoint, command, or CI job is approved.

Future tests should prove at least:

### Build and import safety

- clean source distribution and wheel creation;
- installation and import from a fresh environment;
- resolved distribution and import names;
- import performs no network, DNS, secret reads, filesystem writes, logging mutation, environment mutation, cache initialization, registry mutation, policy evaluation, or activation;
- `__init__.py` exports only the reviewed API;
- local descriptor YAML cannot activate or classify the source;
- the unsafe `public` floor is rejected.

### Product, descriptor, and role behavior

- missing descriptors and activation block real or live inputs;
- product dispatch is explicit and closed;
- API, async download, metadata, Backbone, aggregate, and modeled products remain separate;
- unknown and mixed products fail closed;
- roles cannot be upgraded during parsing or handoff;
- fixture configuration cannot fall through to live behavior.

### Rights, sensitivity, and taxonomy

- missing, unknown, conflicting, or restricted rights produce finite deny/abstain/hold/quarantine behavior;
- dataset and per-record rights conflicts remain visible;
- obscured or sensitive locations cannot be reconstructed or publicly emitted;
- source restrictions and coordinate uncertainty remain attached;
- Backbone snapshot/version is required where anchoring occurs;
- taxonomy disagreements and version drift remain visible;
- no connector test declares final taxonomy or public safety.

### Transport, pagination, jobs, and archives

- network is blocked by default and transport is injectable;
- pagination gaps, duplicates, changed totals, and partial page failures close safely;
- async jobs require accepted terminal-success and complete DOI/checksum/size evidence;
- timeouts, rate limits, retries, redirects, and response sizes are bounded;
- archives reject traversal, special files, excessive expansion, broken manifests, missing core tables, and partial required-table success;
- source bytes, formulas, macros, scripts, and HTML remain inert.

### Semantic and lifecycle boundaries

- specimens cannot become current-presence claims;
- empty results cannot become absence claims;
- aggregates and models cannot become observations;
- no exact sensitive geometry, collector contact, credentials, private predicates, or payload excerpts leak through logs/errors/metrics/snapshots;
- only finite outcomes and accepted RAW/QUARANTINE candidates are possible;
- every attempted WORK, PROCESSED, CATALOG, TRIPLET, PROOF, RECEIPT, RELEASE, PUBLISHED, API, map, graph, report, search, or generated-answer write fails;
- the `plants/` compatibility path cannot create a second package, descriptor, fixture, test, or activation path.

Fixtures must be synthetic, minimized, purpose-specific, clearly labeled, and free of real sensitive locations, collector contact data, restricted dataset rows, credentials, or private source material.

A future command such as:

```bash
python -m pytest connectors/gbif/tests
```

remains **PROPOSED** until packaging, dependencies, tests, fixtures, and the repository-standard runner exist and are demonstrated.

[Back to top ↑](#top)

---

## Responsibility separation

| Surface | Responsibility | Must not do |
|---|---|---|
| `connectors/gbif/src/` | Organize the possible shared source package and document source-code boundaries. | Store data, establish authority, fork by domain, or publish. |
| `connectors/gbif/src/gbif/` | Explicit configuration, supplied-input/transport handling, product dispatch, parsing, metadata preservation, local checks, finite outcomes, and candidate envelopes. | Decide final taxonomy, own policy, persist lifecycle data, or publish. |
| `connectors/gbif/pyproject.toml` | Build and dependency metadata after review. | Encode activation, rights, sensitivity, or policy defaults. |
| `connectors/gbif/plants/` | Compatibility pointer and plant-consumer warnings. | Fetch, parse, activate, test runtime behavior, or store data. |
| `connectors/gbif/tests/` | Shared offline connector tests. | Use real sensitive locations by default or become domain/policy/release authority. |
| Source registry | Canonical source/product/dataset identity, role, rights, access, cadence, sensitivity, and activation. | Store source payloads or infer domain truth. |
| Rights and sensitivity policy | Decide permitted use, restrictions, geoprivacy, obligations, and allowed transforms. | Fetch or parse source material. |
| Taxonomy/domain authority | Resolve GBIF, ITIS, USDA PLANTS, NatureServe, state, institutional, and local crosswalks. | Control source transport or activation. |
| Flora/Fauna/Habitat pipelines | Downstream source-to-domain mapping, object candidates, validation, joins, restricted processing, and derivatives. | Duplicate source capture or inherit activation from package adjacency. |
| Evidence and catalog surfaces | Close provenance, citations, taxonomy versions, rights, transformations, and review. | Treat connector output as proof automatically. |
| Release surfaces | Approve publication, correction, supersession, withdrawal, and rollback. | Treat public source availability, redaction, aggregation, or DOI presence as release by itself. |

One GBIF source capture may support multiple domains through lineage-preserving projections. Domain relevance must not trigger duplicate source retrieval or independent activation by convenience.

[Back to top ↑](#top)

---

## Implementation sequence

Implement in dependency order:

1. **Reconcile connector documentation**
   - align parent, source-root, package, plants-pointer, and test READMEs;
   - keep the plant child documentation-only unless an ADR says otherwise.
2. **Resolve source registry and descriptor authority**
   - select canonical descriptor topology;
   - create product- and dataset-scoped descriptors where required;
   - remove or neutralize package-local descriptor authority;
   - make the unsafe public floor impossible to consume.
3. **Define product identities and roles**
   - independently specify occurrence API, async download, metadata, Backbone, aggregate, modeled, and unsupported products;
   - pin source roles, authority, version, rights, sensitivity, and completeness requirements.
4. **Resolve rights and restricted-use posture**
   - define per-dataset license and citation requirements;
   - preserve additional restrictions;
   - select external rights-decision interfaces.
5. **Resolve taxonomy and sensitivity boundaries**
   - define Backbone snapshot/version behavior;
   - preserve ITIS, USDA PLANTS, NatureServe, state, institutional, and local disagreements;
   - define restricted/obscured-record flags and downstream handoff.
6. **Complete packaging**
   - add build backend, discovery, Python support, dependencies, versioning, package-data policy, and narrow API;
   - prove clean build/install/import behavior.
7. **Select connector-result and handoff contracts**
   - define finite outcomes;
   - settle RAW versus QUARANTINE candidate requirements;
   - prohibit source-root persistence and direct downstream writes.
8. **Approve fixture governance**
   - create synthetic API pages, metadata documents, Backbone versions, and DwC-A archives;
   - include negative rights, sensitivity, pagination, archive, and drift cases;
   - prohibit real sensitive or restricted source rows.
9. **Implement import safety and explicit configuration**
   - no network, secrets, cache, registry, policy, or activation side effects;
   - bounded limits and no live fallback.
10. **Implement supplied-input product slices first**
    - dataset metadata;
    - Backbone metadata/version handling;
    - small synthetic occurrence pages;
    - synthetic DwC-A archive parsing.
11. **Add transport only after offline behavior passes**
    - bounded synchronous API transport;
    - bounded async job/download transport;
    - external credential provider where approved.
12. **Add rights, sensitivity, and drift references**
    - preserve external decisions and source signals;
    - do not implement policy or public transforms locally.
13. **Add accepted candidate handoff**
    - only after storage, lifecycle, rights, sensitivity, and cleanup review;
    - reject direct lifecycle and public writes.
14. **Integrate CI last**
    - prove clean local offline build and test commands first;
    - retain reviewable, sensitive-data-free run evidence;
    - do not upgrade badges, maturity, or activation claims prematurely.
15. **Consider live smoke testing only after explicit approval**
    - isolate it from the default suite;
    - keep it narrow, non-persistent, and independently reviewed.

[Back to top ↑](#top)

---

## Activation gates

No real GBIF input or live behavior should run until all applicable gates close:

- [ ] Parent, source-root, package, plants-pointer, and test documentation are aligned.
- [ ] Canonical GBIF source ID and source-registry topology are accepted.
- [ ] Product-specific and dataset-scoped SourceDescriptors exist where required.
- [ ] SourceActivationDecisions exist for every enabled product and scope.
- [ ] Package-local descriptor authority is removed or explicitly neutralized.
- [ ] The unsafe `sensitivity_floor: public` placeholder cannot affect runtime, package data, tests, or admission.
- [ ] Product-specific source roles and role authorities are accepted and covered by anti-collapse tests.
- [ ] Occurrence API, async download, dataset metadata, Backbone, aggregate, and modeled surfaces have independent contracts.
- [ ] Current source endpoints/access methods, terms, authentication needs, rate limits, and automation permissions are reviewed.
- [ ] Per-dataset rights, citation, attribution, additional restrictions, and conflict handling are accepted.
- [ ] Backbone concept/snapshot identity, rotation, taxon-key drift, and correction behavior are accepted.
- [ ] Taxonomy authority ordering and crosswalk responsibility remain downstream and documented.
- [ ] Rare, protected, obscured, steward-controlled, cultural, and exact-location handling is accepted and tested.
- [ ] Join-induced sensitivity and cross-domain routing contracts are accepted.
- [ ] Binding connector-result and RAW/QUARANTINE handoff contracts are selected.
- [ ] Temporary-file, cache, logging, metrics, retention, deletion, cleanup, and incident-response controls are defined.
- [ ] HTTP, pagination, polling, retry, redirect, download-size, archive, row, time, memory, and decompression limits are defined.
- [ ] Packaging metadata and clean build/install/import behavior are verified from a fresh environment.
- [ ] Synthetic no-network fixtures and executable tests pass.
- [ ] No credentials, private datasets, restricted locations, or real sensitive records are committed.
- [ ] Connector, source registry, rights, sensitivity, taxonomy, domain pipeline, evidence, catalog, and release responsibilities remain separate.
- [ ] Correction, derivative invalidation, withdrawal, rollback, cache invalidation, payload cleanup, and incident procedures are documented.
- [ ] CI evidence is reviewable before activation or maturity claims are upgraded.

Until then, this source root remains a documentation-plus-placeholder scaffold and real/live behavior remains inactive.

[Back to top ↑](#top)

---

## Review and rollback

Review every change below `connectors/gbif/src/` as a source-role, per-dataset-rights, taxonomy-version, geoprivacy, archive-security, packaging, and lifecycle-boundary change.

A reviewer should confirm:

- implementation claims match the actual tree, package metadata, tests, and run evidence;
- imports remain side-effect free;
- source and activation authority remain external;
- package-local YAML cannot activate or classify the source;
- the unsafe public floor is rejected;
- product identity and source roles are explicit and closed;
- API, async download, metadata, Backbone, aggregate, and modeled surfaces remain distinct;
- dataset-level rights, citation, institution, and restrictions remain attached;
- synchronous API replay limits remain visible;
- Backbone snapshot/version and taxonomy disagreements remain visible;
- source obscuration and coordinate uncertainty remain intact;
- specimens are not current-presence claims and empty results are not absence claims;
- no sensitive coordinates, collector contacts, credentials, predicates, or payload excerpts leak through logs or errors;
- no connector code decides public redaction, final taxonomy, or release;
- output stops at finite results and accepted RAW/QUARANTINE candidates;
- the plants child remains documentation-only under the current posture;
- live testing remains absent unless separately approved.

Rollback is required if a change:

- claims implementation, installation, activation, rights clearance, sensitivity clearance, test coverage, live compatibility, or CI without evidence;
- adds import-time or default network, secret, filesystem, logging, environment, cache, registry, policy, or activation behavior;
- uses package-local descriptor YAML as canonical authority;
- accepts `sensitivity_floor: public` as valid;
- introduces provider-wide or consumer-domain-wide activation;
- flattens product roles or dataset rights;
- silently resolves taxonomy against the latest Backbone;
- treats API responses as DOI-pinned evidence;
- weakens pagination, polling, checksum, archive, or partial-capture controls;
- reconstructs or exposes sensitive locations;
- turns specimens into current presence, aggregates/models into observations, or empty results into absence;
- stores or logs sensitive coordinates, private fields, credentials, source rows, or restricted metadata;
- writes directly beyond an accepted RAW/QUARANTINE candidate boundary;
- emits public claims, maps, reports, graphs, search payloads, or generated answers;
- creates a duplicate plant-specific package, descriptor, fixture, test, or activation path.

Rollback procedure:

1. Revert the unsafe or misleading source-root change.
2. Restore the last verified no-network, no-secret, no-persistence, and no-public-write posture.
3. Remove or quarantine unapproved payloads, fixtures, logs, caches, package data, credentials, sensitive locations, or restricted records and assess repository-history exposure.
4. Revoke or rotate exposed credentials through the owning security system.
5. Move legitimate rights, sensitivity, taxonomy, domain, lifecycle, evidence, catalog, or release work to its correct responsibility lane.
6. Repair descriptors, activation decisions, package metadata, product mappings, configuration, workflows, test fixtures, documentation links, and generated templates.
7. Record source-role, rights, taxonomy, sensitivity, schema, packaging, test, or path drift in the appropriate register.
8. Trigger governed correction, invalidation, withdrawal, cleanup, and rollback for every affected downstream artifact.
9. Re-run the last verified clean offline build and test commands when they exist.
10. Correct README badges and maturity claims to match evidence.

[Back to top ↑](#top)

---

## Definition of done

This source root is not complete merely because its boundary is documented.

- [x] The current source-root and package scaffold is documented accurately.
- [x] Empty `__init__.py`, placeholder `fetch.py`, placeholder `descriptor.yaml`, and incomplete `pyproject.toml` are distinguished from implementation.
- [x] The local `public` sensitivity floor is identified as unsafe.
- [x] Shared source-first package placement and the plant compatibility pointer are explicit.
- [x] Occurrence API, async download, dataset metadata, Backbone, aggregate, modeled, and unsupported products are separated.
- [x] Product-specific source-role boundaries are explicit.
- [x] Per-dataset rights, citation, and restriction preservation is explicit.
- [x] Rare/sensitive location, obscuration, and join-induced sensitivity boundaries are explicit.
- [x] Taxonomy anchoring, version, replay, and drift boundaries are explicit.
- [x] Pagination, job, archive, and completeness requirements are explicit.
- [x] RAW/QUARANTINE-candidate-only source-code authority is explicit.
- [x] Source-root, package, plants pointer, tests, registry, policy, taxonomy, domain, evidence, catalog, and release responsibilities are separated.
- [ ] Parent connector and test READMEs are updated to the same verified v0.2 posture.
- [ ] Canonical source-registry topology and product descriptors are accepted.
- [ ] Package-local descriptor is removed, neutralized, or converted to a reviewed non-authoritative pointer.
- [ ] Current access methods, endpoints, terms, credentials, rates, and automation permissions are reviewed.
- [ ] Product roles, authority, formats, versions, stable identifiers, and drift behavior are accepted.
- [ ] Rights, restricted-use, sensitivity, and geoprivacy decision interfaces are accepted.
- [ ] Backbone snapshot/version and taxon-correction behavior is accepted.
- [ ] Taxonomy authority ordering and domain crosswalk contracts are accepted.
- [ ] Build metadata and a stable side-effect-free import API exist.
- [ ] Configuration, product dispatch, transport, metadata, DwC/DwC-A, Backbone, validation, finite error, and handoff code exists.
- [ ] Synthetic fixture governance and fixture files exist.
- [ ] Executable build, import, product, rights, pagination, async-job, archive, taxonomy, sensitivity, logging, drift, and handoff tests exist and pass.
- [ ] A clean repository-standard build/test command is documented and reproducible.
- [ ] CI wiring and passing evidence exist.
- [ ] Any live smoke test is separately approved, isolated, non-persistent, reversible, and excluded from default execution.
- [ ] No source-root API creates canonical biodiversity truth, public-safety decisions, taxonomy conclusions, absence claims, or release artifacts.

[Back to top ↑](#top)

---

## Verification backlog

| Item | Status | Needed evidence |
|---|---:|---|
| Confirm the complete source-root/package inventory, including empty or generated files not visible to code search. | **NEEDS CONTINUOUS VERIFICATION** | Repository tree inspection. |
| Update parent GBIF connector and test READMEs to verified scaffold state. | **NEEDS FOLLOW-UP** | Documentation reconciliation. |
| Confirm the plants child remains documentation-only or ratify a different disposition. | **OPEN DECISION** | ADR or accepted migration decision. |
| Resolve canonical source-registry topology. | **CONFLICTED / NEEDS VERIFICATION** | Registry ADR or migration note. |
| Create and approve product-specific and dataset-scoped SourceDescriptors. | **BLOCKED** | Source, role, rights, sensitivity, and steward review. |
| Create SourceActivationDecisions for every enabled product and scope. | **BLOCKED** | Accepted descriptors and activation workflow. |
| Remove or neutralize package-local descriptor authority. | **BLOCKED** | Packaging and source-authority decision. |
| Remove or safely replace `sensitivity_floor: public`. | **CRITICAL BLOCKER** | Rights/sensitivity review and descriptor update. |
| Resolve source roles for occurrence API, async downloads, metadata, Backbone, aggregates, and modeled assets. | **NEEDS VERIFICATION / BLOCKED** | Product descriptors, role review, fixtures, and anti-collapse tests. |
| Confirm current occurrence API surface, pagination semantics, limits, and replay behavior. | **NEEDS VERIFICATION** | Current source documentation, terms, source review, and transport tests. |
| Confirm current async-download access, authentication, predicate, job-state, polling, DOI, checksum, and retention behavior. | **NEEDS VERIFICATION** | Current source documentation, security review, fixtures, and tests. |
| Confirm current dataset-metadata fields, licenses, citations, restrictions, and update semantics. | **NEEDS VERIFICATION** | Pinned source docs, rights policy, fixtures, and parser tests. |
| Confirm current Darwin Core and DwC-A versions, fields, encodings, archive structure, extension tables, and drift behavior. | **NEEDS VERIFICATION** | Pinned source docs, synthetic archives, parser tests, and archive tests. |
| Confirm GBIF Download DOI, dataset DOI/citation, and Backbone concept/snapshot preservation. | **NEEDS VERIFICATION** | Handoff contract, receipts, fixtures, and evidence tests. |
| Confirm Backbone snapshot discovery, taxon-key stability, synonym, merge, split, deprecation, and rotation behavior. | **NEEDS VERIFICATION** | Versioned fixtures, taxonomy tests, and correction contract. |
| Resolve GBIF, ITIS, USDA PLANTS, NatureServe, state, institutional, and local authority ordering. | **OPEN / ADR-CLASS** | Domain taxonomy decision and crosswalk contract. |
| Confirm rare, protected, obscured, steward-controlled, cultural, and exact-location handling. | **NEEDS VERIFICATION / DEFAULT DENY** | Policy, negative fixtures, reviewer decisions, and release tests. |
| Confirm join-induced sensitivity for parcels, roads, trails, access, facilities, ownership, infrastructure, and cultural-use context. | **NEEDS VERIFICATION / DEFAULT DENY** | Cross-lane policy, tests, receipts, and review workflow. |
| Complete `pyproject.toml` and select build backend, discovery, Python versions, dependencies, and package-data policy. | **OPEN DECISION** | Packaging review and clean build/install evidence. |
| Define the narrow public package API. | **OPEN DECISION** | Connector contract and import tests. |
| Decide whether `fetch.py` is removed, renamed, or retained as a transport facade. | **OPEN DECISION** | Access architecture and migration review. |
| Select connector-result and RAW/QUARANTINE envelope contracts. | **NEEDS VERIFICATION** | Contracts, schemas, validators, and tests. |
| Confirm fixture authority, metadata convention, and safe synthetic-generation rules. | **NEEDS VERIFICATION** | Fixture-root decision, sensitivity review, and reproducibility evidence. |
| Add executable negative-first test modules. | **ABSENT / BLOCKED BY IMPLEMENTATION** | Implemented package slices, fixtures, and reviewed contracts. |
| Confirm no-network and no-live-fallback guard mechanisms. | **NEEDS VERIFICATION** | Test configuration and passing evidence. |
| Confirm executable local build/test commands. | **NEEDS VERIFICATION** | Package/test configuration and clean output. |
| Remove or ratify every `KFM_ALLOW_LIVE_GBIF_TESTS` reference. | **NOT APPROVED** | Source, security, rights, test, and CI decision. |
| Define a live-test policy only if a real need is approved. | **NOT APPROVED** | Source, rights, security, sensitivity, retention, and CI review. |
| Confirm CI integration and source-root boundary enforcement. | **UNKNOWN** | Workflow configuration, branch policy, and successful runs. |
| Confirm no generated template recreates the unsafe descriptor, duplicate plant implementation, real-data fixtures, or an unapproved live client/test path. | **NEEDS VERIFICATION** | Repository-wide template and skeleton review. |

---

## Maintainer note

Keep this source root small, shared, explicit, and difficult to misuse. Resolve product identities, dataset rights, source roles, taxonomy versions, sensitivity, storage, packaging, and test authority before adding behavior. Prefer synthetic or explicitly supplied captures; keep network and credentials off; reject the local public-sensitivity placeholder; preserve Darwin Core and source meaning without inventing domain truth; retain dataset citations and source restrictions; preserve obscuration and uncertainty; route unresolved or high-risk material to denial or quarantine; and stop every source-code path before lifecycle persistence, cross-source joining, evidence closure, release, or publication.

[Back to top ↑](#top)
