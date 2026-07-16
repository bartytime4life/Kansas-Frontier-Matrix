<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/connectors-openstreetmap-tests-readme
title: connectors/openstreetmap/tests/ — OpenStreetMap Connector Test Boundary
type: readme
version: v0.2
status: draft
owners: OWNER_TBD — Connector steward · Source steward · OpenStreetMap steward · Roads-Rail-Trade steward · Settlements-Infrastructure steward · Spatial Foundation steward · Rights reviewer · Sensitivity reviewer · Privacy reviewer · Security steward · Data steward · Migration steward · Validation steward · CI steward · Docs steward
created: 2026-06-20
updated: 2026-07-15
policy_label: public-doctrine; test-boundary; no-network-by-default; no-live-core-services-in-default-ci; read-only-upstream; descriptor-gated; provider-profile-gated; fixture-governed; rights-gated; sensitivity-gated; privacy-minimized; anti-collapse; no-publication
current_path: connectors/openstreetmap/tests/README.md
truth_posture: CONFIRMED target README and tests path, connectors responsibility root, merged OpenStreetMap source-root README v0.2, merged package README v0.2, OpenStreetMap parent boundary, short-name osm alias lane, dedicated OpenStreetMap source-family standard, regional-extract product page, placeholder pyproject version 0.0.0, empty package initializer, bounded absence of conftest.py, fixtures/README.md, test_import_safety.py, test_descriptor_gates.py, test_service_use_guards.py, and test_fixture_metadata.py, and official OSMF API, raster-tile, vector-tile, Nominatim, attribution, copyright, and planet surfaces checked 2026-07-15 / CONFLICTED canonical naming and compatibility topology across connectors/openstreetmap and connectors/osm / UNKNOWN any additional uninspected test files, pytest configuration, test dependencies, approved fixtures, active SourceDescriptors, approved provider profiles, network-test opt-ins, package implementation, lane-specific coverage, CI enforcement depth, scheduled integration tests, emitted test reports, deployment, and downstream release state / NEEDS VERIFICATION owners, alias-resolution ADR or migration note, source activation, provider and endpoint allowlists, current provider terms, rights and attribution decisions, source-role bindings, privacy minimization rules, executable test contracts, fixture approval, schema bindings, correction propagation, deactivation, and rollback automation
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  visibility: public
  base_ref: main
  base_commit: 617ebd26fa362dfe3eeb501a155beebfae663914
  prior_blob: a05e3f8b03ad7332b90a92c1a2ce08f88e971b32
  related_repository_blobs:
    connectors_root_readme: bdd50032bed62ac36964c79f16cf5541b21759a6
    parent_connector_readme: d1337c71e8bc6b0d421b5778179129406df6e2dc
    source_root_readme: 8364bfb259a248ca0f4266f59d9bbfb045871396
    package_readme: ad6e8f539a504b5687f66518edafdf3f36fa82f7
    osm_alias_readme: 514dd57ee42ed18aa1615ae63dd50dbe2e8e914a
    source_family_readme: 3c3974c3cde209724058e0e9cd8af1087084dfbd
    regional_extracts_page: 947d2e6f915f385df1b1f4e3fd029a4bc418568f
    pyproject: db4ce6f276f31672c86d83df2fabaf06107960b7
    package_init: e69de29bb2d1d6434b8b29ae775ad8c2e48c5391
  bounded_path_checks:
    - connectors/openstreetmap/tests/conftest.py was not found
    - connectors/openstreetmap/tests/fixtures/README.md was not found
    - connectors/openstreetmap/tests/test_import_safety.py was not found
    - connectors/openstreetmap/tests/test_descriptor_gates.py was not found
    - connectors/openstreetmap/tests/test_service_use_guards.py was not found
    - connectors/openstreetmap/tests/test_fixture_metadata.py was not found
related:
  - ../README.md
  - ../pyproject.toml
  - ../src/README.md
  - ../src/openstreetmap/README.md
  - ../src/openstreetmap/__init__.py
  - ../../osm/README.md
  - ../../../docs/doctrine/directory-rules.md
  - ../../../docs/sources/catalog/openstreetmap/README.md
  - ../../../docs/sources/catalog/openstreetmap/regional-extracts.md
  - ../../../docs/sources/catalog/RIGHTS-AND-SENSITIVITY-MAP.md
  - ../../../docs/sources/SOURCE_DESCRIPTOR_STANDARD.md
  - ../../../docs/domains/roads-rail-trade/README.md
  - ../../../docs/domains/roads-rail-trade/SOURCES.md
  - ../../../docs/domains/roads-rail-trade/SOURCE_REGISTRY.md
  - ../../../docs/domains/settlements-infrastructure/README.md
  - ../../../docs/architecture/source-roles.md
  - ../../../data/registry/sources/
  - ../../../data/raw/
  - ../../../data/quarantine/
  - ../../../data/receipts/
  - ../../../data/proofs/
  - ../../../schemas/contracts/v1/source/
  - ../../../policy/rights/
  - ../../../policy/sensitivity/
  - ../../../release/
tags: [kfm, connectors, openstreetmap, osm, tests, pytest, no-network, no-live-default, fixtures, provider-profiles, regional-extracts, planet, replication, overpass, nominatim, raster-tiles, vector-tiles, volunteered-geographic-information, odbl, attribution, privacy, sensitivity, anti-collapse, deterministic-replay, raw, quarantine, receipts, rollback, no-publication, governance]
notes:
  - "v0.2 applies the KFM GitHub Repository Documentation Implementation Agent v3.1 test-boundary and connector profile."
  - "The merged source-root and package READMEs v0.2 define the implementation boundary that this test lane must prove."
  - "The test lane remains documentation-only at the bounded inspected paths: no conftest, fixture README, import-safety test, descriptor-gate test, service-use test, or fixture-metadata test was found."
  - "Dedicated OpenStreetMap source-family and regional-extract documentation exist; tests validate implementation behavior and do not own source doctrine."
  - "Default CI must remain no-network and must not use OSMF core services, third-party OSM providers, private sessions, or uncontrolled extracts."
  - "Any live check must be separately approved, opt-in, read-only, provider-profile-gated, resource-bounded, and incapable of publication or upstream mutation."
  - "Tests and fixtures are evidence about code behavior only; they are never source authority, legal advice, rights approval, EvidenceBundle closure, release approval, or publication authority."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# OpenStreetMap Connector Test Boundary

> Governed, deterministic, no-network-by-default test boundary for the OpenStreetMap connector package, proving import safety, provider-profile enforcement, source preservation, finite outcomes, rights and privacy gates, and anti-collapse behavior without contacting community services or manufacturing source authority.

<p>
  <img alt="Document status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Scope: connector tests" src="https://img.shields.io/badge/scope-connector__tests-blue">
  <img alt="Implementation: documentation only" src="https://img.shields.io/badge/implementation-documentation__only-lightgrey">
  <img alt="Network behavior: off by default" src="https://img.shields.io/badge/network-off__by__default-critical">
  <img alt="Fixtures: governed" src="https://img.shields.io/badge/fixtures-governed-orange">
  <img alt="Upstream behavior: read only" src="https://img.shields.io/badge/upstream-read__only-blue">
  <img alt="Authority: behavior evidence only" src="https://img.shields.io/badge/authority-behavior__evidence__only-purple">
  <img alt="Publication authority: denied" src="https://img.shields.io/badge/publication-DENIED-red">
</p>

`connectors/openstreetmap/tests/`

## Quick navigation

[Status](#status-and-evidence-boundary) · [Purpose](#purpose) · [Repository fit](#repository-fit-and-naming-topology) · [Current state](#confirmed-current-state) · [Authority](#test-authority-boundary) · [Strategy](#test-strategy) · [Default contract](#default-no-network-contract) · [Provider profiles](#provider-profile-test-matrix) · [Imports](#import-construction-and-package-safety-tests) · [Parsing](#source-native-parser-and-preservation-tests) · [Completeness](#completeness-truncation-and-staleness-tests) · [Identity](#identity-hashing-deduplication-and-replay-tests) · [Rights](#rights-attribution-privacy-and-sensitivity-tests) · [Anti-collapse](#anti-collapse-and-denial-tests) · [Outcomes](#finite-outcome-and-receipt-tests) · [Fixtures](#fixture-governance) · [Isolation](#determinism-isolation-and-resource-bounds) · [Live checks](#live-integration-checks) · [CI](#ci-coverage-and-reporting) · [Failures](#failure-diagnostics-and-safe-logging) · [Correction](#correction-deactivation-migration-and-rollback-tests) · [Directory map](#directory-map-and-smallest-sound-test-slice) · [Done](#definition-of-done) · [Open](#verification-backlog) · [Evidence](#evidence-basis)

---

## Status and evidence boundary

> [!IMPORTANT]
> **Document lifecycle:** `draft`  
> **Component maturity:** documentation boundary; no executable lane-specific suite established at the bounded inspected paths  
> **Owner:** `OWNER_TBD`  
> **Path:** `connectors/openstreetmap/tests/`  
> **Responsibility:** prove OpenStreetMap connector behavior without becoming source, policy, proof, or publication authority  
> **Default network posture:** denied  
> **Package metadata:** `kfm-connector-openstreetmap`, version `0.0.0`  
> **Topology:** `CONFLICTED / NEEDS VERIFICATION` because `connectors/openstreetmap/` and the README-only `connectors/osm/` alias coexist  
> **Truth posture:** this README, the merged source-root and package contracts, placeholder package metadata, empty initializer, source-family documents, regional-extract page, and selected absent test paths are confirmed. Executable tests, fixture inventory, pytest configuration, test dependencies, approved provider profiles, active descriptors, coverage, lane-specific CI enforcement, live-check controls, and emitted reports remain `UNKNOWN` or `NEEDS VERIFICATION`.

This README defines what the test lane must prove. It does not prove that any test currently runs, that the package imports successfully in supported environments, that a source is activated, that an upstream provider permits use, that rights are resolved, that OSM data is complete or authoritative, or that any derivative can be released.

### Truth labels used here

| Label | Meaning |
|---|---|
| `CONFIRMED` | Verified in this session from repository content, bounded path checks, merged artifacts, official upstream material, or generated validation evidence. |
| `PROPOSED` | A test, fixture, file path, marker, or implementation direction not established as current code. |
| `UNKNOWN` | Not proven by the inspected evidence. |
| `NEEDS VERIFICATION` | Checkable but unresolved for activation, testing, or release decisions. |
| `DENY` | Disallowed by this test boundary unless governing doctrine is deliberately changed. |

---

## Purpose

`connectors/openstreetmap/tests/` is the owning lane for connector-local tests that prove the behavior documented by:

- [`connectors/openstreetmap/README.md`](../README.md);
- [`connectors/openstreetmap/src/README.md`](../src/README.md);
- [`connectors/openstreetmap/src/openstreetmap/README.md`](../src/openstreetmap/README.md).

A mature suite may prove:

- import and package discovery are side-effect-free;
- network access is denied unless an explicit provider profile, descriptor, and opt-in are supplied;
- all upstream behavior is read-only;
- provider-specific restrictions are separated rather than collapsed into one generic OSM client;
- source-native nodes, ways, relations, tags, member order, geometry metadata, versions, timestamps, and provider context are preserved;
- truncation, timeout, stale state, replication gaps, and incomplete extracts cannot be presented as complete success;
- deterministic request, payload, metadata, fixture, and handoff digests are stable;
- rights, attribution, sensitivity, privacy, and source-role ambiguity fail closed;
- finite connector outcomes are explicit and receipt-ready;
- fixtures are minimized, attributable, safe, reproducible, and approved;
- OSM data cannot silently become official, cadastral, ownership, legal-access, route-safety, current-operation, surveyed-precision, or complete-inventory truth;
- connector code cannot publish, promote, close evidence, or directly serve public clients.

This lane must not become:

- an upstream integration runtime;
- an OSM editing client;
- a test-driven excuse to call public community services from default CI;
- a repository for uncontrolled extracts, tile archives, personal query histories, credentials, cookies, or private sessions;
- source-family or product doctrine;
- a source-descriptor or provider-profile authority;
- rights or sensitivity policy;
- fixture authority independent of review;
- a canonical schema or semantic-contract home;
- an `EvidenceBundle`, proof-pack, catalog, triplet, release, or publication authority;
- a public map, route, geocoder, search, API, UI, dashboard, export, automation, or AI-answer surface.

---

## Repository fit and naming topology

Directory Rules assign test code to the test responsibility surface and source-specific implementation to `connectors/`. This existing connector-local test lane is compatible with that split: package code lives below `src/`, while its focused tests live below `tests/`.

```text
connectors/
├── README.md
├── openstreetmap/
│   ├── README.md
│   ├── pyproject.toml                 # confirmed placeholder: 0.0.0
│   ├── src/
│   │   ├── README.md                  # merged v0.2 source-root contract
│   │   └── openstreetmap/
│   │       ├── README.md              # merged v0.2 package contract
│   │       └── __init__.py            # confirmed empty
│   └── tests/
│       └── README.md                  # this file
└── osm/
    └── README.md                      # short-name alias boundary; no parallel test suite
```

### Placement determination

| Question | Determination |
|---|---|
| Is `connectors/openstreetmap/tests/` the correct lane for package-local connector tests? | `CONFIRMED` as an existing test boundary under the connector package. |
| Does this path activate OpenStreetMap? | No. Test-path presence is not source activation. |
| May `connectors/osm/` grow a duplicate test suite? | `DENY` unless an accepted migration deliberately moves the canonical package and tests. |
| Do tests own fixtures as source truth? | No. Fixtures are governed test inputs, not source authority. |
| Does passing a test authorize network use or publication? | No. Activation, provider approval, rights, policy, evidence, and release remain separate. |
| Are new test-file names below this existing lane automatically confirmed? | No. Proposed files remain `PROPOSED` until created and reviewed. |

> [!WARNING]
> Do not split package tests, fixtures, provider profiles, or source identity across `connectors/openstreetmap/` and `connectors/osm/`. A future naming migration must move code and tests together, preserve stable references, and include a rollback path.

---

## Confirmed current state

At base commit `617ebd26fa362dfe3eeb501a155beebfae663914`:

| Surface | Status | Evidence proves | Evidence does not prove |
|---|---:|---|---|
| `connectors/openstreetmap/tests/README.md` | `CONFIRMED` | Test-boundary documentation exists. | Executable tests, fixtures, markers, or coverage. |
| `connectors/openstreetmap/src/README.md` | `CONFIRMED v0.2` | Source-tree behavior and placement boundaries are documented. | Implemented modules or import success. |
| `connectors/openstreetmap/src/openstreetmap/README.md` | `CONFIRMED v0.2` | Detailed package, provider-profile, rights, privacy, lifecycle, and rollback contract exists. | Working client, parser, provider approval, or source activation. |
| `connectors/openstreetmap/pyproject.toml` | `CONFIRMED placeholder` | Project name and version `0.0.0` are present. | Build backend, dependencies, optional test dependencies, pytest configuration, or installability. |
| `connectors/openstreetmap/src/openstreetmap/__init__.py` | `CONFIRMED empty` | Import namespace placeholder exists. | Public API, imports, or implementation. |
| `connectors/osm/README.md` | `CONFIRMED alias boundary` | Short-name lane is documentation-only. | Accepted final naming or migration decision. |
| OpenStreetMap source-family standard | `CONFIRMED draft document` | OSM source-role, rights, sensitivity, and anti-collapse doctrine is documented. | Activation or legal clearance. |
| Regional-extract product page | `CONFIRMED draft document` | Bulk extract posture and lifecycle are documented. | Approved provider, cadence, endpoint, or current ingest. |
| `conftest.py` | `NOT FOUND at bounded path` | The expected shared test-configuration file was absent when checked. | No differently named helper exists elsewhere. |
| `fixtures/README.md` | `NOT FOUND at bounded path` | No fixture-governance README was found at the proposed path. | No fixtures exist anywhere else. |
| `test_import_safety.py` | `NOT FOUND at bounded path` | No expected import-safety test was found. | Import behavior itself. |
| `test_descriptor_gates.py` | `NOT FOUND at bounded path` | No expected descriptor-gate test was found. | Descriptor enforcement elsewhere. |
| `test_service_use_guards.py` | `NOT FOUND at bounded path` | No expected provider-policy test was found. | Provider restrictions elsewhere. |
| `test_fixture_metadata.py` | `NOT FOUND at bounded path` | No expected fixture-metadata test was found. | Fixture validation elsewhere. |
| Lane-specific pytest markers and CI | `UNKNOWN` | No lane-specific configuration was verified. | General repository CI may still inspect documentation or broad contracts. |

> [!NOTE]
> Search absence and bounded `404` checks are not a complete recursive tree proof. Before implementation, generate or inspect a complete tree listing at the selected branch and reconcile every existing file.

---

## Test authority boundary

Tests provide evidence about code behavior under controlled inputs. They do not create truth about the external world.

```text
TESTS MAY PROVE:
  import behavior
  deterministic parsing
  provider-profile enforcement
  bounded request construction
  finite outcome mapping
  fixture validation
  source-native field preservation
  rights/privacy/sensitivity flag propagation
  anti-collapse denials
  receipt candidate construction
  correction and rollback mechanics

TESTS MUST NOT CLAIM:
  source activation
  provider permission
  current endpoint health
  legal clearance
  ODbL compliance as a final legal conclusion
  government authority
  legal access or ownership
  route safety
  completeness on the ground
  catalog or triplet closure
  EvidenceBundle closure
  release approval
  publication
  public API or UI readiness
```

A fixture can show that a parser handles a sample. It cannot show that the sample is representative, current, complete, licensed for every use, safe to expose, or authoritative.

---

## Test strategy

Use layered tests so failures identify the broken boundary instead of producing one broad, ambiguous integration result.

| Layer | Default network | Primary purpose | Authority limit |
|---|---:|---|---|
| Static/documentation checks | none | README links, metadata, path and policy references. | Does not test Python behavior. |
| Import-safety tests | none | Prove import and discovery have no side effects. | Does not prove provider access or parsing. |
| Pure unit tests | none | Parsers, digests, identities, validators, finite outcomes. | Fixture-bound behavior only. |
| Contract/schema tests | none | Validate handoff envelopes and receipt candidates against accepted contracts. | Shape is not semantic or release approval. |
| Fixture integration tests | none | Exercise multi-module flow over approved local fixtures. | Fixture is not source authority. |
| Replay tests | none | Reproduce outcomes from pinned bytes, metadata, and configuration. | Reproduces implementation, not external current state. |
| Property/fuzz tests | none | Check parser invariants and denial behavior over generated inputs. | Generated input is synthetic. |
| Live provider checks | explicit opt-in only | Narrow connectivity or policy-profile verification. | Not default CI, not admission, not publication. |
| Downstream release tests | outside this lane | Verify processed/catalog/release behavior. | Connectors must not own them. |

### First-slice order

The smallest useful test implementation should proceed in this order:

1. import safety and empty-package baseline;
2. fixture metadata and safe-loading contract;
3. finite result and denial enums or equivalents;
4. provider-profile validation with no network;
5. source-native element/tag/relation preservation;
6. completeness, truncation, stale-state, and replication-gap tests;
7. rights, attribution, privacy, and sensitivity propagation;
8. anti-collapse denials;
9. receipt and deterministic replay tests;
10. separately reviewed live checks, only when justified.

---

## Default no-network contract

Default local tests and default CI must operate without network access.

Required behavior:

- DNS and socket use are blocked or made observable during import and unit tests;
- HTTP clients are replaced with deterministic fakes, transports, or recorded local fixtures;
- no OSMF API, Overpass, Nominatim, raster-tile, vector-tile, planet mirror, extract provider, or third-party OSM service is contacted;
- no credentials, tokens, cookies, OAuth state, private sessions, or personal contact values are required;
- no editing API calls, changesets, automated website forms, or upstream writes are possible;
- no test downloads full extracts, planet files, tile pyramids, POI inventories, or broad query results;
- no test relies on provider availability, current rate limits, mutable search results, or current OSM edits;
- no fixture refresh happens implicitly;
- no lifecycle store outside an isolated temporary directory is written;
- no test publishes artifacts, calls governed public APIs, or mutates release state;
- any attempted unexpected network call fails the test with a safe diagnostic.

> [!CAUTION]
> “No credentials required” is not enough. Tests must also prevent anonymous network access, tile scraping, unauthenticated geocoding, and uncontrolled third-party calls.

### Network denial test expectations

A proposed network-denial test should prove:

- package import opens no sockets;
- parser construction opens no sockets;
- loading a fixture opens no sockets;
- provider-profile validation opens no sockets;
- an unapproved endpoint is denied before request construction;
- a missing descriptor is denied before request construction;
- a generic provider profile cannot silently default to a public OSMF service;
- retry logic cannot run when network permission is absent;
- failed network attempts do not leak request contents or secrets.

---

## Provider-profile test matrix

OSM-related services have different purposes and policies. Tests must not collapse them into one generic “OSM endpoint” configuration.

Official OSMF surfaces were checked on **2026-07-15**. Current policy values are version-sensitive and belong in reviewed provider-profile fixtures, not timeless test constants.

| Profile class | Default test posture | Required negative tests |
|---|---|---|
| Regional extract or approved bulk snapshot | Local minimized fixture or content-addressed pointer. | Missing provider identity, source date, extent, digest, terms, or completeness state must fail closed. |
| Planet snapshot | Metadata-only or tiny synthetic fixture. | Full download, unbounded parsing, absent source date, or missing integrity evidence must be denied. |
| Replication diffs | Synthetic ordered sequence fixtures. | Gap, duplicate sequence, out-of-order sequence, missing base snapshot, or unknown continuity must not report complete success. |
| Main OSM editing API | No live calls; read-only contract tests only. | Edit, changeset, automated website form, bulk-read backend, spoofed identity, or unbounded request behavior must be denied. |
| Overpass-compatible provider | Provider-specific offline fixture. | Generic endpoint assumptions, unbounded query, truncation ignored, timeout treated as empty success, or provider terms absent must fail. |
| Public Nominatim | No live default; policy fixture only. | Autocomplete, systematic grid queries, POI enumeration, repeated uncached queries, generic geocoder exposure, or personal/confidential inputs must be denied. |
| OSMF raster tiles | No live default; request-policy fixture only. | Bulk/offline prefetch, no-cache headers, missing attribution, generic identity, or cache bypass must be denied. |
| OSMF vector tiles | No live default; request-policy fixture only. | Bulk archive generation, no-cache behavior, hard-coded unreviewed provider dependency, missing attribution, or identity evasion must be denied. |
| Third-party OSM provider | Explicit provider fixture and reviewed terms. | Inheriting OSMF terms, endpoints, quotas, attribution, or redistribution rights by analogy must fail. |
| Governed synthetic fixture | Preferred for parser and denial tests. | Synthetic input must be visibly labeled and must never acquire external source authority. |

### Editing API policy tests

The current OSMF API policy describes the core API as the data-editing API, not a read-only bulk backend. Tests should therefore prove:

- upstream mutation is impossible from this package boundary;
- read-heavy or bulk use cannot silently route to the editing API;
- application identification fields are explicit and validated;
- impersonated or library-default identity is rejected by the provider profile;
- current policy limits are supplied through an access-dated profile;
- bulk use routes to an approved extract, planet, mirror, or other reviewed provider;
- personal or confidential material is excluded from requests and logs;
- policy-change state can disable a profile without a code release.

### Nominatim policy tests

The current public Nominatim policy is specific to the public OSMF instance. Tests should prove:

- public Nominatim is never selected by a generic “geocoder” default;
- autocomplete is denied;
- systematic enumeration and area-wide POI harvesting are denied;
- periodic or bulk jobs require another approved service or self-hosted instance;
- request repetition uses reviewed caching behavior;
- switching providers does not require changing parser semantics;
- query fixtures are minimized and contain no personal or confidential information;
- current policy values are fixture/profile data rather than scattered constants.

### Raster and vector tile policy tests

Tests should prove:

- tile services are not data-ingest sources by default;
- bulk, offline, pre-seed, archive, cache-warmer, or headless viewport-scanning behavior is denied;
- server cache metadata is preserved and no-cache behavior is rejected;
- provider identity is stable and explicit;
- attribution requirements survive handoff;
- raster and vector services remain separate profiles;
- a provider outage or block does not trigger uncontrolled fallback to another service;
- public tile availability is never treated as source activation or publication permission.

---

## Import, construction, and package-safety tests

The source-root and package READMEs require safe imports. The tests must make that requirement executable.

### Import safety

A proposed `test_import_safety.py` should verify that importing:

- `openstreetmap`;
- each public submodule;
- package metadata helpers;
- parser modules;
- provider-profile modules;
- receipt and outcome modules;

does not:

- open network connections;
- read environment secrets or credential stores;
- read private sessions or cookies;
- write caches, temp files, lifecycle data, receipts, or logs outside controlled test locations;
- register scheduled work;
- start threads or subprocesses;
- mutate global provider configuration;
- import optional heavy/geospatial dependencies unexpectedly;
- issue warnings containing sensitive values;
- contact upstream services;
- create public artifacts.

### Constructor safety

Constructing clients, parsers, adapters, or provider profiles should:

- be pure or explicitly local;
- reject missing required configuration before network use;
- accept dependency-injected transports;
- avoid mutable process-wide singletons;
- avoid implicit default endpoints;
- avoid fetching schema or policy files remotely;
- avoid logging full queries, tokens, cookies, or personal input;
- produce deterministic representations suitable for hashing and replay.

### Public import discipline

Tests should also prove that:

- `__init__.py` exports only reviewed public names;
- private implementation details are not accidentally re-exported;
- the `openstreetmap` namespace does not conflict with an installed unrelated package;
- no duplicate `osm` Python namespace is introduced by the alias lane;
- public names have stable semantics or explicit deprecation notices;
- import errors are finite and actionable without exposing sensitive configuration.

---

## Source-native parser and preservation tests

Parser tests must preserve OSM-native evidence before downstream interpretation.

### Element identity

For nodes, ways, and relations, fixtures should exercise preservation of:

- element type;
- numeric or source-native identifier;
- version;
- timestamp;
- changeset identifier when present and permitted;
- visibility/deletion state when present;
- user or contributor fields only when necessary, policy-permitted, and minimized;
- tags, including unknown tags;
- node references for ways;
- ordered relation members;
- member type, reference, and role;
- bounds or envelope metadata;
- payload format and schema/version indicator;
- provider and distribution identity;
- source date and retrieval date;
- response or extract digest.

### Lossless handling

Tests should reject silent behavior that:

- drops unknown tags;
- normalizes tag keys without a recorded transform;
- reorders relation members;
- converts identifiers through floating-point types;
- removes null/absent distinctions needed by the source format;
- converts closed ways into polygons without an explicit rule;
- converts route or restriction relations into domain truth;
- assumes a CRS without recording it;
- simplifies geometry without a transform receipt;
- merges duplicate-looking elements without version-aware identity;
- treats a derived geometry as raw source geometry.

### Geometry tests

Geometry tests should cover:

- point, line, polygon candidate, and collection representations;
- incomplete ways with missing node references;
- self-intersections and invalid rings;
- antimeridian or bounds edge cases where applicable;
- empty geometry versus missing geometry;
- topology warnings;
- coordinate-order mistakes;
- precision preservation;
- reprojection metadata;
- simplification/generalization flags;
- exact-location sensitivity propagation.

---

## Completeness, truncation, and staleness tests

A connector must distinguish an empty result from an incomplete or failed result.

| Condition | Required result |
|---|---|
| Valid complete empty response | Explicit complete-empty outcome with provider and query evidence. |
| Timeout before completion | Retryable failure or quarantine; never complete empty. |
| Provider truncation indicator | Partial/incomplete outcome with continuation evidence. |
| Unknown truncation state | Quarantine or denial. |
| Extract missing expected metadata | Quarantine. |
| Extract source date older than approved threshold | Stale or quarantine outcome. |
| Replication sequence gap | Incomplete/repair-required outcome. |
| Duplicate replication sequence | Idempotent no-op or explicit duplicate, not double admission. |
| Out-of-order sequence | Denial or held replay until continuity is restored. |
| Provider outage | Failure/unknown state, never evidence that no features exist. |
| Parser drops unsupported object | Explicit unsupported/quarantine outcome, not silent success. |
| Incomplete way or relation members | Preserve incompleteness and prevent domain promotion. |

### Completeness invariants

Tests should prove:

- record count alone is not completeness proof;
- HTTP success alone is not completeness proof;
- an empty list after a timeout is not success;
- a provider-side cap must be represented;
- bounds and query scope are preserved;
- pagination or continuation state is exhausted or explicitly incomplete;
- replication continuity is tied to a known base snapshot;
- current-state claims require downstream temporal validation;
- absence in OSM is never converted into absence on the ground.

---

## Identity, hashing, deduplication, and replay tests

Deterministic behavior is required for auditable source admission.

### Identity layers

Tests should distinguish:

- provider-profile identity;
- source descriptor reference;
- request/query identity;
- distribution or extract identity;
- OSM element identity;
- element-version identity;
- response/payload identity;
- normalized candidate identity;
- fixture identity;
- run/attempt identity;
- correction or supersession identity.

### Digest tests

Digest tests should prove:

- identical canonical inputs produce identical digests;
- irrelevant process-local values do not change digests;
- meaningful query, bounds, provider, media type, source date, sequence, or payload changes do change digests;
- raw-byte and normalized-content digests are not conflated;
- digest algorithm and canonicalization version are recorded;
- line-ending or map-order normalization happens only where the contract allows it;
- secrets and transient authorization values are excluded from persisted request fingerprints;
- redaction changes are represented by a transform or derivative digest;
- a fixture digest mismatch fails before parsing.

### Deduplication and replay

Tests should cover:

- same payload retrieved twice;
- same element/version from two approved providers;
- same query with a changed provider profile;
- corrected upstream element version;
- replay from raw bytes with network disabled;
- replay under changed parser version;
- replay under changed policy profile;
- superseded or quarantined prior outcome;
- partial run resumed after interruption;
- no-op receipt when nothing new is admitted.

Replay must reproduce the historical result only when the pinned code, configuration, policy inputs, and fixture bytes match. Otherwise, tests should produce an explicit drift or non-equivalent replay result.

---

## Rights, attribution, privacy, and sensitivity tests

These tests verify propagation and fail-safe behavior. They do not issue legal conclusions.

### Rights and attribution

Tests should prove:

- OSM attribution is present in any candidate that may flow toward public use;
- the rights-review state is explicit;
- unknown rights block public-release candidates;
- ODbL and derivative-database review state is preserved;
- provider-specific terms are distinct from the OSM database license;
- tile style/service terms are not treated as identical to database terms;
- third-party extract terms are not inherited from OSMF by assumption;
- attribution survives normalization and handoff;
- collective or derivative database decisions remain external to the connector;
- an internal test fixture does not become approved redistribution material.

The OSMF attribution guideline states that OSM data is distributed under ODbL and that public use requires attribution. Tests may encode the presence and propagation of reviewed fields, but legal interpretation remains outside this lane.

### Privacy minimization

Tests should reject:

- credentials, cookies, OAuth tokens, or private session material in fixtures;
- personal or confidential search inputs;
- full contributor histories when not necessary;
- request logs containing precise user-originated queries without minimization;
- raw IP addresses or device identifiers;
- embedded contact data not approved for repository storage;
- screenshots or payloads containing unrelated personal information;
- exact high-risk locations not approved for fixture use.

When source-native user or changeset fields are needed for parser coverage, fixtures should be synthetic or minimized and explicitly document why those fields are necessary.

### Sensitivity

Tests should cover:

- exact archaeological points;
- culturally sensitive corridors;
- critical infrastructure;
- rare-species locations;
- living-person-associated places;
- sensitive facilities;
- precise location joins across domains.

Expected behavior should be one of:

- deny;
- quarantine;
- redact;
- generalize;
- stage for restricted access;
- require manual review.

A successful parser must not bypass sensitivity policy.

---

## Anti-collapse and denial tests

Negative tests are load-bearing because OSM data is broad, community-edited, and easy to overinterpret.

| Collapse risk | Required denial |
|---|---|
| OSM as official government record | Do not assign official or regulatory authority from OSM presence. |
| OSM as cadastral truth | Do not infer parcel boundaries or legal ownership. |
| `access=*` as legal permission | Do not claim lawful public access from tags alone. |
| `operator=*` or `owner=*` as verified ownership | Preserve as source-native tags, not verified identity. |
| Highway tags as route safety | Do not produce safe-route or emergency-route claims. |
| Feature presence as current operation | Do not claim a business, road, bridge, facility, or service is currently operating. |
| Feature absence as real-world absence | Preserve completeness caveats. |
| Community geometry as surveyed precision | Do not claim survey-grade accuracy. |
| Imported tag as upstream authority | Resolve and cite the authoritative upstream source directly when needed. |
| OSM relation as KFM semantic object | Require downstream contracts and transform receipts. |
| Parser success as source activation | Activation remains registry/governance work. |
| Test pass as rights clearance | Rights review remains separate. |
| Fixture as EvidenceBundle | Fixture is controlled test input only. |
| Connector receipt as proof closure | Receipt records behavior, not final claim support. |
| Tile availability as ingest permission | Service availability does not authorize scraping or publication. |
| Nominatim result as canonical address truth | Geocoder output remains provider-specific context. |
| Generic `osm` alias as second implementation | Deny duplicate package, tests, fixtures, or descriptors. |
| Outage or timeout as empty result | Preserve unknown/failure state. |
| Stale extract as current state | Require explicit source date and freshness evaluation. |

These denials should be executable and fail with finite, reviewable outcomes.

---

## Finite outcome and receipt tests

The exact accepted enum remains `NEEDS VERIFICATION`, but tests should require a finite outcome model rather than exceptions or booleans alone.

### Proposed outcome classes

- admitted candidate;
- quarantined candidate;
- denied;
- no-op;
- duplicate;
- stale;
- partial/incomplete;
- unsupported;
- deferred;
- retryable failure;
- terminal failure;
- rate-limited;
- policy drift;
- schema drift;
- provider-profile drift;
- replay mismatch;
- correction/supersession required.

### Outcome invariants

Tests should prove:

- every run ends in one finite result;
- ambiguous results do not default to admitted;
- error classes are safe to log;
- raw exception text does not leak secrets or personal queries;
- retryable and terminal failures are distinguishable;
- timeout is not complete empty;
- partial is not admitted complete;
- quarantine carries reason codes and review requirements;
- no-op still creates sufficient traceability where required;
- denial does not mutate upstream or lifecycle state;
- correction and supersession preserve prior identity.

### Receipt candidates

Receipt tests should verify preservation of:

- attempt/run identity;
- source descriptor reference;
- provider-profile identity and version;
- request or distribution fingerprint;
- retrieval or evaluation time;
- source date;
- response status or local-file state;
- cache/validator metadata when applicable;
- payload and metadata digests;
- completeness state;
- rights, sensitivity, privacy, and source-role posture;
- finite outcome and reason;
- retry/supersession links;
- code/configuration version;
- fixture identity in tests.

A receipt candidate is not an `EvidenceBundle` and does not authorize promotion.

---

## Fixture governance

Fixtures are repository artifacts with provenance, rights, safety, and maintenance obligations.

### Allowed fixture classes

| Fixture class | Default posture |
|---|---|
| Pure synthetic | Preferred for parser, denial, and edge-case tests. |
| Generated fuzz seed | Allowed when deterministic and free of external source claims. |
| Minimized/redacted upstream snapshot | Requires explicit approval, provenance, digest, rights, and redaction note. |
| Approved regional-extract fragment | Requires provider, source date, extent, extraction method, and redistribution review. |
| Approved query response | Requires provider profile, query fingerprint, retrieval time, minimization, and policy review. |
| Metadata-only distribution fixture | Preferred for large-file and provider-manifest tests. |
| Full uncontrolled extract or tile archive | `DENY` in the repository test lane. |
| Private session or authenticated payload | `DENY`. |
| High-risk exact-location sample | `DENY` unless specifically approved, minimized, and access-controlled outside a public fixture lane. |

### Required fixture metadata

Every non-trivial fixture should resolve to metadata containing:

- stable fixture identifier;
- purpose and covered tests;
- fixture class;
- synthetic versus external origin;
- provider/distribution profile when external;
- source URL or controlled reference when permitted;
- source date and retrieval date;
- geographic scope;
- query fingerprint or extraction method;
- original and stored digests;
- media type and format/schema version;
- rights and attribution posture;
- ODbL/derivative review status;
- sensitivity and privacy review;
- minimization, redaction, or generalization transforms;
- expected completeness state;
- expected parser/outcome behavior;
- approval/reviewer state;
- correction or supersession reference;
- safe-removal and regeneration instructions.

### Fixture handling rules

- Fixtures are immutable after approval; corrections create new fixture versions.
- Large upstream bytes should be represented by approved external references or minimized fragments.
- Regeneration must be explicit and reviewed.
- Fixture refreshes must not happen in normal test execution.
- Digests are checked before parsing.
- Redacted fixtures must not retain hidden original values in comments, filenames, or metadata.
- Test failures must not print entire sensitive fixtures.
- Fixture removal must preserve the reason and affected-test inventory.
- A fixture may be retired without rewriting historical test reports.

---

## Determinism, isolation, and resource bounds

Tests should be deterministic across supported environments.

### Isolation

Use isolated temporary paths and dependency injection for:

- filesystems;
- clocks;
- randomness;
- HTTP transport;
- DNS/socket access;
- environment access;
- provider profiles;
- descriptors;
- policy decisions;
- cache state;
- logging;
- process/thread creation.

### Determinism

Tests should pin or control:

- timezone;
- locale;
- encoding;
- line endings where relevant;
- JSON/XML ordering assumptions;
- floating-point comparison policy;
- coordinate precision policy;
- hash/canonicalization versions;
- fixture bytes;
- parser version;
- provider-profile version;
- source descriptor fixture;
- policy fixture;
- clock and retry schedule.

### Resource safety

Tests should include explicit bounds for:

- maximum fixture size;
- maximum element/member count in unit fixtures;
- parser recursion/depth;
- decompression expansion;
- XML/JSON nesting;
- relation cycles;
- request/query length;
- log output;
- retry attempts;
- in-memory buffers;
- test execution time.

The bound values must be reviewed configuration, not guessed universal constants.

### Malicious and malformed input

Test:

- oversized or compressed-bomb candidates;
- deeply nested structures;
- cyclic relations;
- invalid UTF-8 or malformed XML/JSON/PBF metadata;
- duplicate identifiers with conflicting versions;
- path traversal in archive names;
- unexpected media types;
- HTML error pages returned as data;
- truncated payloads;
- invalid numeric coordinates;
- NaN/infinite values where parsers allow numeric input;
- malicious tag content intended for logs, Markdown, HTML, SQL, shell, or UI injection.

Failures must remain finite and safe.

---

## Live integration checks

Default CI must not run live OSM checks.

A live check, if ever justified, must satisfy all of the following:

- separate workflow or explicitly selected test marker;
- manual or steward-approved trigger;
- active source descriptor;
- approved provider profile;
- current service terms checked and recorded;
- read-only behavior;
- bounded request scope;
- stable, identifying application configuration;
- no credentials in logs;
- no personal or confidential queries;
- no editing API mutation;
- no tile bulk/offline behavior;
- no Nominatim autocomplete, systematic enumeration, or generic geocoder exposure;
- no uncontrolled fallback provider;
- no lifecycle admission, publication, or release mutation;
- explicit timeout and circuit breaker;
- safe receipt/report output;
- no retry storm;
- cancellation support;
- automatic disablement on policy or schema drift.

### What a live check may establish

At most, a live check may establish that:

- an approved endpoint responded;
- expected headers or a small schema signature were observed;
- the provider profile may need review;
- a narrowly scoped request path remains technically reachable.

It does not establish:

- source completeness;
- ongoing availability;
- source activation;
- rights clearance;
- current real-world truth;
- release readiness;
- public-service suitability;
- SLA.

---

## CI, coverage, and reporting

### CI posture

The lane should eventually have explicit CI evidence for:

- import safety;
- no-network enforcement;
- fixture metadata validation;
- provider-profile validation;
- parser preservation;
- completeness/truncation;
- deterministic hashes and replay;
- rights/privacy/sensitivity propagation;
- anti-collapse denials;
- finite outcomes and receipts;
- safe logging;
- correction and rollback behavior.

### Coverage

Coverage percentages are not currently established. Do not invent a target or claim completeness from a high percentage.

Meaningful coverage reporting should separate:

- package/module coverage;
- branch coverage;
- denial-path coverage;
- provider-profile coverage;
- fixture class coverage;
- format/media-type coverage;
- source-object coverage;
- malformed-input coverage;
- rights/privacy/sensitivity gate coverage;
- correction/replay coverage.

Critical denials should be listed explicitly, not hidden behind an aggregate percentage.

### Test reports

A future report should record:

- commit/ref;
- package and test configuration;
- Python/platform versions;
- selected test groups and markers;
- network-denial state;
- fixture manifest digest;
- provider-profile fixture versions;
- source descriptor fixture versions;
- policy fixture versions;
- passed, failed, skipped, and quarantined tests;
- nondeterminism/retry count;
- generated artifacts and digests;
- known exclusions;
- open verification items.

Reports are validation evidence, not release authority.

### CI failure posture

- No-network violation: hard fail.
- Fixture digest mismatch: hard fail.
- Missing required fixture metadata: hard fail.
- Rights/privacy/sensitivity ambiguity in a public-path test: hard fail or quarantine test data.
- Provider policy drift: fail closed and require review.
- Optional dependency unavailable: explicit skip only when the feature is truly optional and the skip is visible.
- Live endpoint unavailable: live-check failure only; must not invalidate deterministic offline tests.
- Repository-wide unrelated prerequisite: report separately from lane-specific failures.

---

## Failure diagnostics and safe logging

Test diagnostics should be useful without leaking sensitive data.

Required behavior:

- redact credentials, cookies, authorization headers, private URLs, and personal queries;
- log request fingerprints rather than raw sensitive requests;
- truncate large payload excerpts;
- identify fixture by stable ID and digest;
- identify provider profile and version;
- identify parser/outcome code;
- preserve reason codes;
- show completeness and quarantine state;
- avoid printing exact sensitive coordinates;
- escape untrusted tag content;
- avoid embedding full upstream responses in CI annotations;
- separate assertion failure from provider/network failure;
- preserve enough information for deterministic replay.

Snapshot or golden-file tests must review untrusted content before commit and avoid normalizing away meaningful source differences.

---

## Correction, deactivation, migration, and rollback tests

Governed correction paths must be testable before activation.

### Correction tests

Cover:

- corrected OSM element version;
- corrected fixture metadata;
- corrected provider profile;
- corrected source descriptor fixture;
- changed rights or sensitivity decision;
- parser bug that produced a different normalized candidate;
- replay mismatch after code or policy change;
- previously admitted candidate moved to quarantine;
- superseded receipt candidate.

Expected behavior:

- prior identity remains traceable;
- corrections create new immutable records or versions;
- old outcomes are not silently overwritten;
- affected downstream references can be enumerated;
- reason and reviewer state are preserved.

### Deactivation tests

Prove that deactivation:

- blocks new live requests;
- does not delete historical raw data or receipts;
- disables retries and schedules;
- prevents fallback to another unapproved provider;
- leaves deterministic fixture tests usable;
- surfaces affected provider profiles and descriptors;
- returns explicit denied/deactivated outcomes.

### Naming migration tests

If `openstreetmap` and `osm` naming is resolved, tests must prove:

- only one active Python package and test suite remains;
- import compatibility is explicit and time-bounded;
- no duplicate fixtures or descriptors exist;
- inbound references are updated or redirected;
- test reports retain historical paths;
- rollback restores the prior import and test routing without history rewriting.

### Rollback tests

A rollback drill should verify:

- the prior package/test version can be selected;
- provider profiles can be restored or disabled;
- fixtures remain content-addressable;
- corrected outcomes are not confused with historical outcomes;
- no public artifact is silently republished by connector rollback;
- rollback itself emits a reviewable record outside this test lane when required.

---

## Directory map and smallest sound test slice

The owning root is `connectors/openstreetmap/tests/`. Proposed files below that existing lane are responsibility-aligned but remain `PROPOSED` until created.

```text
connectors/openstreetmap/
├── pyproject.toml
├── src/
│   ├── README.md
│   └── openstreetmap/
│       ├── README.md
│       └── __init__.py
└── tests/
    ├── README.md
    ├── conftest.py                         # PROPOSED: no-network/isolation fixtures
    ├── fixtures/
    │   ├── README.md                       # PROPOSED: fixture-governance contract
    │   ├── manifest.yaml                   # PROPOSED: stable fixture metadata index
    │   ├── synthetic/
    │   ├── extracts/
    │   ├── replication/
    │   ├── queries/
    │   └── malformed/
    ├── test_import_safety.py               # PROPOSED
    ├── test_fixture_metadata.py            # PROPOSED
    ├── test_descriptor_gates.py            # PROPOSED
    ├── test_provider_profiles.py            # PROPOSED
    ├── test_service_use_guards.py          # PROPOSED
    ├── test_element_preservation.py        # PROPOSED
    ├── test_relation_member_order.py        # PROPOSED
    ├── test_geometry_preservation.py        # PROPOSED
    ├── test_completeness.py                 # PROPOSED
    ├── test_replication_continuity.py       # PROPOSED
    ├── test_identity_and_digests.py         # PROPOSED
    ├── test_replay.py                       # PROPOSED
    ├── test_rights_attribution.py           # PROPOSED
    ├── test_privacy_sensitivity.py          # PROPOSED
    ├── test_anti_collapse.py                # PROPOSED
    ├── test_finite_outcomes.py              # PROPOSED
    ├── test_receipt_candidates.py           # PROPOSED
    ├── test_safe_logging.py                 # PROPOSED
    └── test_correction_rollback.py          # PROPOSED
```

> [!IMPORTANT]
> This tree is a design map, not repository fact. Before creating files, inspect the complete current tree, test conventions, package manager configuration, schema locations, fixture conventions, `CODEOWNERS`, workflows, and accepted contracts.

### Smallest sound implementation slice

The recommended first PR for executable tests should be limited to:

1. test dependency and pytest configuration in the accepted package configuration;
2. `conftest.py` with enforced no-network and isolated temporary state;
3. synthetic fixture manifest plus fixture-governance README;
4. import-safety test;
5. fixture-metadata test;
6. provider-profile validation test;
7. anti-collapse denial test;
8. CI invocation proving those tests run offline.

It should not add live tests, full extracts, tile archives, or broad parser implementation in the same change.

---

## Definition of done

### Documentation boundary

- [x] Existing `doc_id` and `created` metadata are preserved.
- [x] Version and update date reflect a substantive revision.
- [x] Current path, responsibility, evidence limits, and authority boundaries are explicit.
- [x] The merged source-root and package v0.2 contracts are linked.
- [x] The dedicated OSM source-family and regional-extract documents are linked.
- [x] The `openstreetmap` / `osm` compatibility conflict is surfaced.
- [x] Current implementation depth is bounded to inspected evidence.
- [x] Default no-network and read-only-upstream requirements are explicit.
- [x] Provider-specific test profiles are separated.
- [x] Fixture governance, deterministic replay, completeness, rights, privacy, sensitivity, anti-collapse, finite outcomes, receipts, live-check controls, CI, correction, and rollback are documented.
- [x] Test success is explicitly denied source, proof, rights, release, and publication authority.

### Executable test lane

- [ ] Owners are confirmed and `OWNER_TBD` is replaced through repository-approved evidence.
- [ ] The complete tests tree and all related root-level tests are inventoried.
- [ ] Test dependencies and pytest configuration are accepted.
- [ ] Default test execution blocks network, secrets, private sessions, upstream writes, and external lifecycle writes.
- [ ] Fixture governance and a machine-checkable fixture manifest exist.
- [ ] Every external fixture has approved provenance, digest, rights, privacy, sensitivity, and minimization metadata.
- [ ] Import-safety tests prove no side effects.
- [ ] Descriptor and provider-profile tests fail closed before request construction.
- [ ] Regional extract, replication, editing API, Overpass, Nominatim, raster-tile, vector-tile, third-party, and synthetic profiles remain distinct.
- [ ] Parser tests preserve source-native element, tag, relation, member, geometry, time, provider, and completeness fields.
- [ ] Tests reject timeout-as-empty, outage-as-absence, stale-as-current, and partial-as-complete.
- [ ] Deterministic identity, hashing, deduplication, and replay are tested.
- [ ] Rights, attribution, privacy, sensitivity, and source-role ambiguity fail closed.
- [ ] Anti-collapse denials cover official, cadastral, ownership, legal-access, route-safety, operation, precision, and completeness claims.
- [ ] Finite outcomes and receipt candidates use accepted contracts.
- [ ] Logs and reports redact sensitive values.
- [ ] Live checks, if any, are separate, opt-in, approved, read-only, bounded, and non-publishing.
- [ ] Correction, deactivation, naming migration, supersession, and rollback are exercised.
- [ ] CI proves the lane runs no-network tests and reports skipped/denied/live checks visibly.
- [ ] No tests or fixtures exist under the `connectors/osm/` alias lane without an accepted migration.

---

## Verification backlog

| Verification item | Evidence that would settle it | Status |
|---|---|---:|
| Complete current tests tree | Recursive tree listing at the implementation ref. | `NEEDS VERIFICATION` |
| Current owners and reviewers | `CODEOWNERS`, team records, or approved assignment. | `NEEDS VERIFICATION` |
| Pytest and test dependency configuration | Accepted `pyproject.toml` or equivalent package config. | `NEEDS VERIFICATION` |
| Existing package implementation | Source files, imports, dependency graph, and tests. | `NEEDS VERIFICATION` |
| Existing fixture inventory | Fixture tree, manifest, digests, and approvals. | `NEEDS VERIFICATION` |
| No-network enforcement | Executable test harness plus failure fixture. | `NEEDS VERIFICATION` |
| Active SourceDescriptors | Canonical registry records and activation decisions. | `NEEDS VERIFICATION` |
| Approved provider profiles | Reviewed provider/endpoint profiles with access dates and policy evidence. | `NEEDS VERIFICATION` |
| Accepted source-role bindings | Current contracts, schemas, validators, and negative tests. | `NEEDS VERIFICATION` |
| Rights and attribution decisions | Policy review and source activation records. | `NEEDS VERIFICATION` |
| Privacy and sensitivity rules | Accepted policy rules and fixture denials. | `NEEDS VERIFICATION` |
| Fixture redistribution permission | Rights review per external fixture. | `NEEDS VERIFICATION` |
| Outcome and receipt contracts | Accepted semantic contracts and schemas. | `NEEDS VERIFICATION` |
| Parser preservation behavior | Code, fixtures, and passing tests. | `NEEDS VERIFICATION` |
| Replication continuity behavior | Sequence fixtures and gap/replay tests. | `NEEDS VERIFICATION` |
| Lane-specific CI invocation | Workflow code and current run logs. | `NEEDS VERIFICATION` |
| Coverage and critical-denial matrix | Coverage report plus explicit denial inventory. | `NEEDS VERIFICATION` |
| Live-check governance | Separate workflow, approval, provider profile, and safe reports. | `NEEDS VERIFICATION` |
| `openstreetmap` / `osm` final topology | Accepted ADR or migration note. | `NEEDS VERIFICATION` |
| Correction and rollback exercise | Recorded drill with immutable prior/new outcomes. | `NEEDS VERIFICATION` |
| Downstream dependency inventory | Catalog/proof/release lineage query or reviewed manifest. | `NEEDS VERIFICATION` |

---

## Evidence basis

| Evidence | Role | Status | Supports | Does not prove |
|---|---|---:|---|---|
| [`Directory Rules` v1.4](../../../docs/doctrine/directory-rules.md) | Placement doctrine | `CONFIRMED` repository document | Responsibility-root separation and governed lifecycle placement. | Executable test suite or source activation. |
| [`connectors/README.md`](../../README.md) | Connector-root contract | `CONFIRMED` repository document | Source admission, finite outcomes, RAW/QUARANTINE/receipt boundary, and no publication. | Child implementation completeness. |
| [`connectors/openstreetmap/README.md`](../README.md) | Parent connector boundary | `CONFIRMED draft` | OSM connector scope and anti-collapse posture. | Working package or accepted provider. |
| [`connectors/openstreetmap/src/README.md`](../src/README.md) | Source-root contract | `CONFIRMED v0.2` | Import discovery, module placement, provider routing, no-network, correction, and rollback boundaries. | Implemented modules or tests. |
| [`connectors/openstreetmap/src/openstreetmap/README.md`](../src/openstreetmap/README.md) | Package contract | `CONFIRMED v0.2` | Detailed provider profiles, parser preservation, completeness, rights/privacy, finite outcomes, testing, and rollback requirements. | Executable connector behavior. |
| [`connectors/openstreetmap/pyproject.toml`](../pyproject.toml) | Package metadata | `CONFIRMED placeholder` | Project name and version `0.0.0`. | Dependencies, pytest config, or installability. |
| [`connectors/openstreetmap/src/openstreetmap/__init__.py`](../src/openstreetmap/__init__.py) | Import namespace | `CONFIRMED empty` | Namespace placeholder exists. | Public imports or side-effect safety. |
| [`connectors/osm/README.md`](../../osm/README.md) | Alias boundary | `CONFIRMED draft` | Alias lane must not become duplicate implementation. | Accepted final topology. |
| [`docs/sources/catalog/openstreetmap/README.md`](../../../docs/sources/catalog/openstreetmap/README.md) | Source-family standard | `CONFIRMED draft` | Source-role, rights, sensitivity, temporal, and anti-collapse doctrine. | Activation, legal clearance, or current provider behavior. |
| [`regional-extracts.md`](../../../docs/sources/catalog/openstreetmap/regional-extracts.md) | Product page | `CONFIRMED draft` | Bulk-extract lifecycle and metadata posture. | Approved provider, endpoint, cadence, or current data. |
| [OSMF API Usage Policy](https://operations.osmfoundation.org/policies/api/) | Official external policy | `CONFIRMED` checked 2026-07-15 | Editing-API purpose, identification, bulk alternatives, privacy, and policy-change risk. | Repository activation or provider approval. |
| [OSMF Tile Usage Policy](https://operations.osmfoundation.org/policies/tiles/) | Official external policy | `CONFIRMED` checked 2026-07-15 | Attribution, identification, caching, no-bulk/offline behavior, privacy, and best-effort service posture. | Permission for KFM to use the service. |
| [OSMF Vector Tile Usage Policy](https://operations.osmfoundation.org/policies/vector/) | Official external policy | `CONFIRMED` checked 2026-07-15 | Vector-service attribution, identity, cache, no-bulk, version, privacy, and change requirements. | A stable timeless profile or activation. |
| [OSMF Nominatim Usage Policy](https://operations.osmfoundation.org/policies/nominatim/) | Official external policy | `CONFIRMED` checked 2026-07-15 | Public-instance restrictions, no autocomplete/systematic enumeration, caching, identity, privacy, and provider-switch posture. | Self-hosted or third-party Nominatim terms. |
| [OSMF Licence/Attribution Guidelines](https://osmfoundation.org/wiki/Licence/Attribution_Guidelines) | Official external guidance | `CONFIRMED` checked 2026-07-15 | ODbL context and public attribution requirements. | Final legal advice or KFM rights approval. |
| [OpenStreetMap copyright page](https://www.openstreetmap.org/copyright) | Official source notice | `CONFIRMED` checked 2026-07-15 | Current project licensing and attribution reference surface. | Derivative-database decision for KFM. |
| [Planet OSM](https://planet.openstreetmap.org/) | Official bulk distribution | `CONFIRMED` checked 2026-07-15 | Bulk snapshot and replication distribution surface. | Approved KFM provider profile or fixture rights. |
| Bounded absent-path checks | Current implementation evidence | `CONFIRMED for named paths` | Expected conftest, fixture README, and selected tests were not found. | No differently named tests or fixtures exist elsewhere. |

---

## Status summary

`connectors/openstreetmap/tests/` is the governed test boundary for the OpenStreetMap connector package.

It may prove deterministic, import-safe, no-network, read-only, provider-profile-gated, source-preserving, rights-aware, privacy-minimized, sensitivity-aware, finite, replayable connector behavior using governed fixtures.

It is not OpenStreetMap source authority, provider approval, legal advice, rights clearance, source activation, government truth, cadastral truth, ownership truth, legal-access truth, route-safety truth, current-operation truth, completeness proof, schema authority, policy authority, fixture authority, `EvidenceBundle` closure, catalog/triplet authority, release authority, public map/API/UI/search behavior, or publication evidence by itself.

**Tests prove bounded implementation behavior. They do not promote source material or authorize publication.**

<p align="right"><a href="#top">Back to top</a></p>
