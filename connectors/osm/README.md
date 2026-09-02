<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/connectors-osm-readme
title: connectors/osm/ — Governed OpenStreetMap Short-Name Compatibility Boundary
type: readme
version: v0.2
status: draft; repository-grounded; readme-only; compatibility-alias; no-active-implementation-established
owners: OWNER_TBD — Connector steward · Source steward · OpenStreetMap steward · Roads-Rail-Trade steward · Settlements-Infrastructure steward · Spatial Foundation steward · Rights reviewer · Sensitivity reviewer · Privacy reviewer · Security steward · Data steward · Migration steward · Validation steward · CI steward · Docs steward
created: 2026-06-20
updated: 2026-07-15
supersedes: v0.1
policy_label: public-doctrine; compatibility-alias; openstreetmap; osm; source-admission-only; read-only-upstream; no-network; no-package; no-source-tree; no-tests; no-descriptors; no-receipts; no-publication; migration-gated
current_path: connectors/osm/README.md
truth_posture: CONFIRMED target README and README-only short-name lane, connectors responsibility root, governed connectors/openstreetmap parent boundary v0.2, governed OpenStreetMap source root v0.2, governed OpenStreetMap package boundary v0.2, governed OpenStreetMap test boundary v0.2, dedicated OpenStreetMap source-family standard and regional-extract product page, canonical-lane placeholder package metadata version 0.0.0, empty canonical-lane package initializer, bounded absence of osm pyproject/src/tests paths, and current alias references / PROPOSED transitional compatibility class, one-way alias resolution to connectors/openstreetmap, no-new-files enforcement, canonical identifier and descriptor normalization, migration/tombstone procedure, CI guardrails, correction propagation, and rollback requirements / CONFLICTED final osm versus openstreetmap naming disposition because no accepted ADR or migration note was verified / UNKNOWN exhaustive recursive alias-lane inventory, active SourceDescriptors, approved provider profiles, executable OpenStreetMap behavior, alias consumers, generated links, CI enforcement, source activation, emitted receipts, deployment, and downstream release state / NEEDS VERIFICATION owners, accepted alias class, import and package namespace guarantees, source-id normalization, consumer references, current rights and provider terms, validator wiring, correction sweep, deactivation, and rollback automation
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  repository_id: "1059091169"
  visibility: public
  base_ref: main
  base_commit: 0f2333a34ffa25bc90a509c24b39d2a622cc0d3e
  prior_blob: 514dd57ee42ed18aa1615ae63dd50dbe2e8e914a
  related_repository_blobs:
    directory_rules: 2affb080e6f0043867c64c7f06c1ca52030fbd55
    connectors_root_readme: bdd50032bed62ac36964c79f16cf5541b21759a6
    canonical_connector_readme: 3d25e61152a147f2eede4c5add2c5c996fd245cb
    canonical_source_root_readme: 8364bfb259a248ca0f4266f59d9bbfb045871396
    source_family_readme: 3c3974c3cde209724058e0e9cd8af1087084dfbd
    canonical_pyproject: db4ce6f276f31672c86d83df2fabaf06107960b7
    canonical_package_init: e69de29bb2d1d6434b8b29ae775ad8c2e48c5391
  direct_lane_files_confirmed:
    - connectors/osm/README.md
  checked_absent_paths:
    - connectors/osm/pyproject.toml
    - connectors/osm/src/README.md
    - connectors/osm/tests/README.md
  bounded_search_result: repository code search surfaced this README and references from canonical OpenStreetMap and roads/source documentation; no separate osm package, source root, or tests lane was established
related:
  - ../README.md
  - ../openstreetmap/README.md
  - ../openstreetmap/pyproject.toml
  - ../openstreetmap/src/README.md
  - ../openstreetmap/src/openstreetmap/README.md
  - ../openstreetmap/tests/README.md
  - ../../docs/doctrine/directory-rules.md
  - ../../docs/sources/catalog/openstreetmap/README.md
  - ../../docs/sources/catalog/openstreetmap/regional-extracts.md
  - ../../docs/sources/SOURCE_DESCRIPTOR_STANDARD.md
  - ../../docs/sources/catalog/RIGHTS-AND-SENSITIVITY-MAP.md
  - ../../docs/domains/roads-rail-trade/README.md
  - ../../docs/domains/roads-rail-trade/SOURCES.md
  - ../../docs/domains/roads-rail-trade/CANONICAL_PATHS.md
  - ../../docs/domains/settlements-infrastructure/README.md
  - ../../docs/architecture/source-roles.md
  - ../../data/registry/sources/
  - ../../data/raw/
  - ../../data/quarantine/
  - ../../data/receipts/
  - ../../data/proofs/
  - ../../schemas/contracts/v1/source/
  - ../../policy/rights/
  - ../../policy/sensitivity/
  - ../../release/
notes:
  - "v0.2 replaces a brief alias note with a commit-pinned compatibility boundary aligned to the merged OpenStreetMap parent, source-root, package, and test contracts."
  - "The bounded alias lane is README-only. It has no pyproject, source root, test root, package namespace, provider profile, SourceDescriptor family, fixture lane, receipt emitter, or release path."
  - "connectors/openstreetmap/ is the repository-present implementation/documentation lane. This README does not make that naming choice permanent; final disposition remains ADR or migration-note work."
  - "The alias resolves one way: osm means OpenStreetMap. It must not create reverse authority, duplicate implementation, split source identity, or independent policy."
  - "OpenStreetMap source-family and regional-extract documentation now exist; this alias must link to them rather than restating source doctrine."
  - "This revision changes documentation only and creates no code, source activation, network behavior, descriptor, fixture, test, receipt, proof, policy decision, or release object."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Governed OpenStreetMap Short-Name Compatibility Boundary

`connectors/osm/`

> README-only compatibility boundary for the short name **OSM**. The repository-present OpenStreetMap connector lane is [`connectors/openstreetmap/`](../openstreetmap/README.md). This path may explain the alias and migration posture; it must not become a second connector, package, source tree, test lane, descriptor family, receipt path, or publication authority.

<p>
  <img alt="Document status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Scope: compatibility alias" src="https://img.shields.io/badge/scope-compatibility__alias-blue">
  <img alt="Inventory: README only" src="https://img.shields.io/badge/inventory-README__only-lightgrey">
  <img alt="Canonical implementation lane: openstreetmap" src="https://img.shields.io/badge/implementation__lane-openstreetmap-blue">
  <img alt="Network behavior: none" src="https://img.shields.io/badge/network-none-critical">
  <img alt="New implementation files: denied" src="https://img.shields.io/badge/new__implementation-DENIED-red">
  <img alt="Publication authority: denied" src="https://img.shields.io/badge/publication-DENIED-red">
</p>

**Quick navigation:** [Status](#status-and-evidence-boundary) · [Purpose](#purpose) · [Authority](#authority-and-anti-collapse) · [Repository fit](#repository-fit-and-naming-topology) · [Current state](#confirmed-current-state) · [Alias contract](#compatibility-alias-contract) · [Canonical lane](#relationship-to-connectorsopenstreetmap) · [Identifiers](#identity-descriptors-and-reference-normalization) · [Services](#service-and-provider-boundary) · [Rights](#rights-attribution-and-source-role) · [Privacy](#privacy-sensitivity-and-minimization) · [Lifecycle](#lifecycle-and-finite-outcomes) · [Consumers](#consumer-import-and-configuration-boundary) · [Validation](#validation-and-ci-guardrails) · [Migration](#migration-deprecation-and-tombstone-procedure) · [Correction](#correction-deactivation-and-rollback) · [Directory map](#directory-map) · [Done](#definition-of-done) · [Backlog](#open-verification-register) · [Evidence](#evidence-ledger)

> [!IMPORTANT]
> **Evidence snapshot:** `main@0f2333a34ffa25bc90a509c24b39d2a622cc0d3e`
> **Target blob before this revision:** `514dd57ee42ed18aa1615ae63dd50dbe2e8e914a`
> **Bounded alias-lane result:** this README only
> **Checked absent alias implementation paths:** `pyproject.toml`, `src/README.md`, and `tests/README.md`
> **Repository-present OpenStreetMap implementation/documentation lane:** [`connectors/openstreetmap/`](../openstreetmap/README.md)
> **Activation:** an alias, path, link, import string, source-list entry, successful workflow, or future redirect activates nothing

> [!CAUTION]
> `osm` is an abbreviation, not a separate source family, provider, database, service, product, license, package, or authority. Do not mint a second source identity merely because both path spellings exist.

> [!WARNING]
> Do not add source clients, package code, tests, fixtures, credentials, provider profiles, source descriptors, downloaded data, receipts, proofs, release objects, public routes, or generated outputs under `connectors/osm/`. The smallest sound state is README-only until an accepted migration deliberately changes it.

---

## Status and evidence boundary

### Safe conclusion

`connectors/osm/` is a repository-present, README-only short-name compatibility lane. The inspected repository establishes `connectors/openstreetmap/` as the fuller OpenStreetMap connector boundary and Python package location. No accepted ADR or migration note was verified that permanently declares either spelling canonical for all time.

Therefore:

- **CONFIRMED:** `connectors/osm/README.md` exists.
- **CONFIRMED:** `connectors/openstreetmap/` contains the coordinating connector README, placeholder package metadata, source-root README, importable-package README, empty initializer, and test-boundary README.
- **CONFIRMED:** dedicated OpenStreetMap source-family and regional-extract documentation exist.
- **CONFIRMED:** the checked `connectors/osm/pyproject.toml`, `connectors/osm/src/README.md`, and `connectors/osm/tests/README.md` paths are absent.
- **PROPOSED:** classify this child lane as a frozen compatibility alias pointing one way to `connectors/openstreetmap/`.
- **CONFLICTED:** final `osm` versus `openstreetmap` naming disposition remains unresolved without an accepted ADR or migration note.
- **UNKNOWN:** exhaustive recursive alias inventory, consumer references, generator behavior, symlink behavior, active SourceDescriptors, source activation, runtime use, and release state.

### Truth labels used here

| Label | Meaning |
|---|---|
| `CONFIRMED` | Verified from current repository evidence, bounded path checks, or merged governed documentation in this session. |
| `PROPOSED` | A safe design or migration requirement not established as current implementation. |
| `CONFLICTED` | Two naming surfaces coexist without verified final disposition. |
| `UNKNOWN` | Not proven by inspected repository, runtime, workflow, or release evidence. |
| `NEEDS VERIFICATION` | Checkable, but unresolved strongly enough to act as fact. |
| `DENY` | Disallowed by this compatibility boundary unless governance deliberately changes it. |

### Maturity matrix

| Capability or artifact | Status | Evidence-bounded conclusion |
|---|---:|---|
| Alias README | `CONFIRMED` | This file exists at `connectors/osm/README.md`. |
| Alias package metadata | `NOT FOUND AT CHECKED PATH` | No `connectors/osm/pyproject.toml` was found. |
| Alias source tree | `NOT FOUND AT CHECKED PATH` | No `connectors/osm/src/README.md` was found. |
| Alias tests root | `NOT FOUND AT CHECKED PATH` | No `connectors/osm/tests/README.md` was found. |
| Canonical-lane coordinating README | `CONFIRMED` | `connectors/openstreetmap/README.md` is repository-present and v0.2. |
| Canonical-lane package | `PLACEHOLDER` | Package metadata is version `0.0.0`; initializer is empty. |
| Canonical-lane executable client | `NOT ESTABLISHED` | The parent boundary records bounded absence of expected client/config/descriptor modules. |
| OpenStreetMap source-family doctrine | `CONFIRMED DOCUMENTATION` | Dedicated source-family standard exists. |
| Regional extract product doctrine | `CONFIRMED DOCUMENTATION` | Dedicated product page exists. |
| Active source descriptor | `UNKNOWN` | No activation decision is established by this README. |
| Approved provider profile | `UNKNOWN` | No provider or service is approved by alias existence. |
| Alias consumer/import | `UNKNOWN` | No accepted consumer binding was verified. |
| Alias CI enforcement | `UNKNOWN` | No dedicated no-new-files alias validator was verified. |
| Release or publication | `DENIED / NOT ESTABLISHED` | Connector aliases have no release authority. |

[Back to top](#top)

---

## Purpose

This README has one safe purpose:

> Preserve the common abbreviation `OSM` as a navigational and compatibility term while preventing it from becoming a second source of connector authority.

It should help maintainers answer:

- Does `osm` refer to OpenStreetMap? **Yes.**
- Does `connectors/osm/` contain a second connector implementation? **No.**
- Where should current connector implementation and tests be inspected? [`connectors/openstreetmap/`](../openstreetmap/README.md).
- Where does OpenStreetMap source-family doctrine live? [`docs/sources/catalog/openstreetmap/`](../../docs/sources/catalog/openstreetmap/README.md).
- Does this alias activate a source or provider? **No.**
- May a future migration change the accepted path? **Yes, but only through explicit, reversible governance.**

### Audience

- connector, source, OpenStreetMap, rights, sensitivity, privacy, security, data, validation, CI, migration, and docs stewards;
- Roads/Rail/Trade, Settlements/Infrastructure, Spatial Foundation, Hydrology, Archaeology, and other domain reviewers using OSM-derived context;
- maintainers resolving `osm` versus `openstreetmap` references;
- reviewers preventing duplicate packages, descriptors, fixtures, receipts, tests, and release paths;
- operators verifying that short-name convenience never weakens source admission or rights controls.

### Non-goals

This README does not:

- choose a permanent repository-wide naming convention by assertion;
- implement a redirect, symlink, import alias, package alias, registry alias, or shell command;
- activate OpenStreetMap, an extract provider, an API, Overpass, Nominatim, tiles, replication, or any other service;
- define OpenStreetMap source-family meaning, rights, attribution, sensitivity, or provider terms;
- define a `SourceDescriptor`, source role, schema, policy, fixture, receipt, `EvidenceBundle`, or release record;
- fetch, parse, normalize, conflate, route, geocode, tile, publish, or serve data;
- promise backward compatibility for unverified consumers;
- authorize public UI, API, map, search, export, or AI access.

[Back to top](#top)

---

## Authority and anti-collapse

### Responsibility split

```text
connectors/osm/                         = README-only short-name compatibility boundary
connectors/openstreetmap/               = repository-present connector/package boundary
docs/sources/catalog/openstreetmap/     = source-family and product doctrine
data/registry/sources/                  = SourceDescriptor identity and activation
policy/rights/                          = rights, attribution, share-alike, use constraints
policy/sensitivity/                     = sensitivity and precise-location decisions
schemas/contracts/v1/source/            = machine-checkable source contract shape
data/raw/ | data/quarantine/            = permitted source-admission data handoffs
data/receipts/                          = connector run/probe/admission process memory
data/proofs/                            = proof closure, not owned by connectors
release/                                = release, correction, withdrawal, rollback authority
apps/                                   = governed serving surfaces after release
```

### What this README may decide

This README may define:

- the safe maintenance boundary for `connectors/osm/`;
- that current implementation work must not be duplicated here;
- that short-name references resolve to the OpenStreetMap source family;
- what evidence is currently verified;
- what remains `PROPOSED`, `CONFLICTED`, `UNKNOWN`, or `NEEDS VERIFICATION`;
- review, migration, correction, and rollback expectations for this alias;
- the minimum guardrails before any path disposition changes.

### What this README cannot decide

This README cannot:

- admit or activate a source;
- approve a provider, endpoint, extract, service, tile server, or geocoder;
- assign source role;
- decide current rights, attribution, ODbL, share-alike, or provider-terms obligations;
- establish `src-osm`, `osm`, `openstreetmap`, or another identifier as canonical registry identity;
- create executable package or import behavior;
- rewrite existing consumer configuration;
- create evidence, prove completeness, or close a claim;
- approve publication;
- turn community-edited geography into government, cadastral, legal, operational, routing-safety, or complete-inventory truth.

### Disallowed collapses

```text
OSM abbreviation                  -> separate source family
connectors/osm path               -> active connector
README link                       -> redirect implementation
alias presence                    -> canonical naming decision
alias reference                   -> active SourceDescriptor
source-family document            -> source activation
provider name                     -> provider approval
valid URL                         -> permitted service use
successful fetch                  -> source correctness
OSM object id                     -> KFM canonical identity
OSM tag                           -> official domain truth
copied authoritative tag          -> inherited authority
OSM road geometry                 -> legal access or route safety
OSM parcel-like geometry          -> cadastral or title boundary
Nominatim result                  -> canonical place identity
raster tile                       -> database extract
vector tile                       -> complete source snapshot
Overpass result                   -> complete inventory
regional extract                  -> globally complete state
receipt                           -> EvidenceBundle
proof                             -> release decision
connector output                  -> publication
```

### One-way resolution rule

Until governance decides otherwise:

```text
osm -> OpenStreetMap -> connectors/openstreetmap/
```

The reverse implication is forbidden:

```text
connectors/openstreetmap/ -> duplicate osm package
```

The alias is a navigational convenience, not a second implementation authority.

[Back to top](#top)

---

## Repository fit and naming topology

### Directory Rules basis

Directory Rules assign source-specific external fetch and admission support to `connectors/`. The `connectors/openstreetmap/` lane therefore fits the responsibility root. The presence of two child spellings is a naming and migration concern, not permission to build two connectors.

Directory Rules also establish that compatibility surfaces must not evolve as parallel authority. Although `connectors/osm/` is a child lane rather than a repository root, the same anti-duplication rule applies: canonical changes land once, and compatibility surfaces point, freeze, regenerate, or migrate.

### Current topology

```text
connectors/
├── README.md
├── openstreetmap/
│   ├── README.md
│   ├── pyproject.toml
│   ├── src/
│   │   ├── README.md
│   │   └── openstreetmap/
│   │       ├── README.md
│   │       └── __init__.py
│   └── tests/
│       └── README.md
└── osm/
    └── README.md
```

### Path posture

| Path | Current role | Change posture |
|---|---|---|
| `connectors/openstreetmap/` | Coordinating connector and package lane | Current implementation/documentation target unless governance changes it. |
| `connectors/openstreetmap/src/` | Canonical source-root boundary | New implementation belongs here after activation and contract gates. |
| `connectors/openstreetmap/src/openstreetmap/` | Package boundary and import namespace | Preserve unless an accepted migration changes it. |
| `connectors/openstreetmap/tests/` | Test and fixture-governance boundary | Tests belong here, not under `osm/`. |
| `connectors/osm/` | README-only short-name compatibility lane | Freeze implementation; documentation-only changes permitted. |
| `docs/sources/catalog/openstreetmap/` | Source-family and product doctrine | Referenced, never mirrored into either connector lane. |

### Why a short alias may remain useful

A README-only alias can:

- help contributors searching for the common abbreviation;
- prevent accidental creation of a second connector;
- point stale internal references toward the fuller lane;
- preserve migration context;
- make naming conflict visible;
- provide a rollback-safe tombstone if a future migration removes or renames a path.

It is not useful when it accumulates implementation, policy, registry state, test data, receipts, or independent doctrine.

[Back to top](#top)

---

## Confirmed current state

### Alias lane

Confirmed at the evidence snapshot:

```text
connectors/osm/
└── README.md
```

Checked and not found:

```text
connectors/osm/pyproject.toml
connectors/osm/src/README.md
connectors/osm/tests/README.md
```

These checks are bounded. They do not prove every possible hidden, generated, ignored, branch-only, or externally mounted file is absent.

### OpenStreetMap lane

Confirmed documentation and package surfaces:

```text
connectors/openstreetmap/
├── README.md                    # governed coordinating boundary v0.2
├── pyproject.toml               # kfm-connector-openstreetmap, version 0.0.0
├── src/
│   ├── README.md                # governed source-root boundary v0.2
│   └── openstreetmap/
│       ├── README.md            # governed package boundary v0.2
│       └── __init__.py          # empty
└── tests/
    └── README.md                # governed no-network test boundary v0.2
```

The canonical lane is documentation-rich but implementation-light. Alias governance must not describe it as production-ready.

### Source documentation

Confirmed repository documentation:

- OpenStreetMap source-family standard;
- OpenStreetMap regional-extract product page;
- source descriptor standard;
- rights and sensitivity map;
- Roads/Rail/Trade and Settlements/Infrastructure domain context.

The prior alias README statement that a dedicated OpenStreetMap source page was not found is superseded.

### Not established

The inspected evidence does not establish:

- active source descriptors;
- approved provider profiles;
- allowed endpoints;
- executable source clients;
- parsers;
- no-network fixture payloads;
- executable lane-specific tests;
- schedules;
- emitted receipts;
- runtime deployments;
- alias imports;
- alias configuration compatibility;
- public release of any OSM-derived artifact.

[Back to top](#top)

---

## Compatibility alias contract

### Default class

**PROPOSED class:** frozen README-only compatibility alias.

A future ADR or migration note may choose a different disposition, but until then:

- new implementation files are denied;
- new package metadata is denied;
- new tests and fixtures are denied;
- new descriptors are denied;
- new provider profiles are denied;
- new receipt paths are denied;
- new source data is denied;
- public serving behavior is denied;
- independent doctrine is denied.

### Allowed contents

This lane may contain:

- this README;
- a future migration notice explicitly authorized by an ADR;
- a future machine-readable redirect marker only when a governing contract defines its semantics and validators;
- a future tombstone notice with rollback guidance;
- links to canonical source, implementation, test, policy, and migration surfaces.

Any additional file is `NEEDS VERIFICATION` and should be rejected by default until reviewed.

### Denied contents

| Material | Reason | Correct home |
|---|---|---|
| Python package or source client | Creates parallel implementation. | `connectors/openstreetmap/src/openstreetmap/` |
| Package metadata | Creates competing install identity. | `connectors/openstreetmap/pyproject.toml` |
| Tests and fixtures | Splits proof and coverage. | `connectors/openstreetmap/tests/` |
| Provider profiles | Alias cannot approve services. | Accepted config/provider-profile home referenced by canonical connector. |
| Source descriptors | Splits source identity and activation. | `data/registry/sources/` |
| Source-family doctrine | Duplicates governance. | `docs/sources/catalog/openstreetmap/` |
| Rights or sensitivity policy | Alias cannot decide admissibility. | `policy/rights/`, `policy/sensitivity/` |
| Downloaded OSM data | Violates lifecycle and access boundaries. | Governed `data/raw/` or `data/quarantine/` after activation. |
| Receipts | Creates split process lineage. | `data/receipts/` |
| EvidenceBundles | Connector alias is not proof authority. | `data/proofs/` |
| Release records | Alias is not release authority. | `release/` |
| Public routes or UI | Bypasses trust membrane. | Governed `apps/` after release. |
| Credentials or cookies | Secret exposure. | Approved secret management only. |

### No implicit forwarding

A README link is not an executable redirect. Code must not assume that opening, importing, resolving, or scheduling `connectors/osm/` automatically forwards to `connectors/openstreetmap/`.

Any future executable forwarding must be:

- explicitly designed;
- deterministic;
- tested;
- no-network at import;
- backward-compatible or migration-documented;
- free of duplicate initialization;
- free of duplicate source IDs;
- reversible.

[Back to top](#top)

---

## Relationship to `connectors/openstreetmap/`

### Governing rule

The OpenStreetMap parent boundary owns the current connector coordination contract. This alias inherits its prohibitions but does not restate or replace its operational detail.

The parent boundary currently requires:

- read-only upstream behavior;
- no network by default;
- active `SourceDescriptor` resolution before live access;
- explicit provider or distribution profiles;
- service-specific terms and resource budgets;
- source-native preservation;
- completeness, freshness, and truncation handling;
- rights, attribution, sensitivity, privacy, and source-role gates;
- deterministic identity, hashing, replay, and correction;
- RAW, QUARANTINE, or connector-receipt handoffs only;
- no upstream edits, public tile scraping, generic public geocoding, identity evasion, release, or publication.

This alias must not weaken any parent requirement.

### Parent-child authority table

| Surface | Owns | Alias behavior |
|---|---|---|
| `connectors/openstreetmap/README.md` | Coordinating connector boundary | Link and defer. |
| `connectors/openstreetmap/src/README.md` | Source-tree organization and import safety | Do not mirror. |
| `connectors/openstreetmap/src/openstreetmap/README.md` | Detailed package behavior contract | Do not create `osm` package twin. |
| `connectors/openstreetmap/tests/README.md` | No-network tests and fixture governance | Do not create parallel tests. |
| `connectors/openstreetmap/pyproject.toml` | Package metadata | Do not add alias package metadata. |
| `docs/sources/catalog/openstreetmap/README.md` | Source-family governance | Link and defer. |
| `docs/sources/catalog/openstreetmap/regional-extracts.md` | Product/distribution doctrine | Link and defer. |
| `connectors/osm/README.md` | Short-name compatibility and migration warning | Remain README-only. |

### Canonical lane maturity caution

The long-name lane is not proven production-ready. Its `0.0.0` metadata and empty initializer are scaffold evidence. Pointing to that lane does not establish:

- executable completeness;
- source activation;
- endpoint approval;
- current rights clearance;
- source correctness;
- receipt emission;
- release readiness.

[Back to top](#top)

---

## Identity, descriptors, and reference normalization

### Source identity rule

One upstream source family must map to one governed KFM source identity per admitted product/profile. Path aliases must not mint duplicate source identities.

Unsafe pattern:

```text
src-osm             -> one descriptor
src-openstreetmap   -> second descriptor
```

Safe proposed pattern:

```text
one accepted source_id
aliases: [osm, openstreetmap]
canonical connector_ref: connectors/openstreetmap
```

The exact fields and identifier are `NEEDS VERIFICATION` against the accepted source contract and registry implementation.

### Identifier classes that must remain distinct

- repository path;
- Python package name;
- Python import namespace;
- KFM source family ID;
- SourceDescriptor ID;
- provider profile ID;
- distribution/product ID;
- upstream OSM object identity;
- dataset/extract identity;
- run ID;
- receipt ID;
- evidence reference;
- release ID.

The abbreviation `osm` may be a display or search alias for some of these. It must not silently substitute across all classes.

### Source-native identity

The canonical connector boundary requires preservation of source-native OpenStreetMap identity, which may include:

- element type;
- element ID;
- element version;
- timestamp;
- changeset/user visibility posture where permitted;
- tags;
- node/way/relation membership;
- provider or extract context;
- query or manifest identity;
- source vintage;
- digest.

This alias stores none of those values.

### Descriptor normalization requirements

Before an alias is used in machine configuration, governance should define:

- accepted canonical source ID;
- accepted canonical connector path;
- accepted alias vocabulary;
- whether aliases are case-sensitive;
- whether aliases are stored or derived;
- how duplicate descriptors are detected;
- how migrations update references;
- how historical receipts preserve the spelling used at run time;
- how corrections resolve old aliases;
- how rollback restores prior resolution.

### Deduplication rule

A change from `osm` spelling to `openstreetmap` spelling is not a new source observation, new dataset version, or new evidence object. Naming normalization must not mint duplicate lifecycle entities.

[Back to top](#top)

---

## Service and provider boundary

### OSM is not one endpoint

The OpenStreetMap ecosystem includes multiple materially different access and product surfaces. Examples may include:

- database extracts;
- planet or replication data;
- regional extract providers;
- editing APIs;
- query services;
- geocoding/search services;
- raster tiles;
- vector tiles;
- downstream routing graphs;
- third-party hosted APIs.

An `osm` alias cannot stand in for an approved provider profile.

### Provider-profile requirement

Any future live interaction must resolve one explicit provider/distribution profile that defines at least:

- source family and product;
- provider identity;
- access method;
- endpoint family;
- permitted request classes;
- rate, concurrency, timeout, and size limits;
- authentication or user-agent requirements;
- attribution and terms references;
- completeness and freshness semantics;
- retry and circuit-breaker policy;
- privacy and minimization rules;
- allowed geographic and temporal scope;
- expected payload and digest behavior;
- fixture provenance;
- correction and deactivation behavior.

### Denied generic behavior

The alias must not authorize:

- upstream edits or changesets;
- automated website-form interaction;
- public tile scraping or bulk prefetch;
- generic public geocoding or autocomplete;
- systematic POI enumeration;
- identity, IP, account, or rate-limit evasion;
- unbounded Overpass-style queries;
- use of a third-party endpoint merely because it accepts OSM-related requests;
- silent failover to a different provider;
- network access during import, docs build, tests, or fixture discovery.

### Service anti-collapse

```text
OpenStreetMap database   != standard raster tile service
OpenStreetMap database   != Nominatim
OpenStreetMap database   != Overpass deployment
OpenStreetMap database   != regional extract provider
OpenStreetMap database   != routing graph
OpenStreetMap data       != a provider's service terms
provider availability    != provider approval
```

[Back to top](#top)

---

## Rights, attribution, and source role

### Rights authority

This alias does not own rights interpretation. Current rights, attribution, database-license, produced-work, derivative-database, tile-style, provider, redistribution, and share-alike questions belong to the source-family, policy, source activation, and release review surfaces.

### Fail-closed rule

When rights or current terms are unresolved:

```text
public promotion -> DENY
source admission -> QUARANTINE or no-op
network request  -> DENY unless provider profile is approved
```

### Attribution preservation

A mature canonical connector must preserve enough metadata to support later attribution and license review. This alias must not:

- shorten attribution;
- replace provider-specific attribution;
- strip source references;
- assert a license decision;
- infer release permission from public accessibility;
- treat a fixture notice as release attribution.

### Source role

OpenStreetMap is not assigned one universal KFM source role merely because it is OpenStreetMap. Source role is decided per admitted object family and source product.

The alias must not label OSM universally as:

- authoritative;
- regulatory;
- observed;
- official;
- complete;
- current;
- cadastral;
- routing-safe.

### Upstream authority rule

When an OSM feature cites or derives from an authoritative upstream, KFM should admit and cite the upstream authority directly when the claim depends on that authority. Authority does not flow through a copied tag.

[Back to top](#top)

---

## Privacy, sensitivity, and minimization

### Alias posture

The alias holds no data and performs no network activity. Therefore it must not contain:

- downloaded feature payloads;
- user or contributor metadata;
- query results;
- exact sensitive locations;
- infrastructure inventories;
- archaeological points;
- rare-species locations;
- private-person location joins;
- raw fixture extracts;
- request headers, tokens, cookies, IPs, or account identifiers.

### Canonical connector obligations

A future canonical run must apply content-appropriate sensitivity controls. OSM-derived material may expose:

- archaeological or culturally sensitive places;
- critical infrastructure detail;
- rare-species or habitat clues;
- private access and residence context;
- community-edited personal or business details;
- contributor/user metadata;
- disputed boundaries or names;
- sensitive routes, crossings, or facilities.

Unresolved sensitivity routes to quarantine, restriction, generalization, redaction, delayed access, or denial.

### Data minimization

Only fields necessary for the approved admission purpose should be requested and retained. A generic OSM alias is not a reason to collect all tags, all history, all users, all relations, or all nearby features.

### Logging

Logs and receipts should record operational evidence without reproducing sensitive payloads. The alias itself emits no logs or receipts.

[Back to top](#top)

---

## Lifecycle and finite outcomes

### Lifecycle invariant

The connector responsibility root participates only at the source-admission edge of:

```text
RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED
```

This alias performs no transition.

### Allowed canonical connector handoffs

A verified canonical connector may prepare:

- immutable RAW admission candidate;
- QUARANTINE candidate with finite reason;
- connector run/probe/admission receipt candidate;
- deterministic parse result returned to an orchestrator;
- explicit no-op or denied result.

It does not write downstream truth by implication.

### Alias finite outcomes

Any machine resolver introduced later should return a finite result such as:

| Outcome | Meaning |
|---|---|
| `RESOLVED` | Alias deterministically maps to the accepted canonical connector identity. |
| `NOT_CONFIGURED` | No machine alias contract exists. |
| `AMBIGUOUS` | More than one candidate canonical identity exists. |
| `DEPRECATED` | Alias remains for compatibility but new use is denied. |
| `DENIED` | Alias use violates migration, security, or governance policy. |
| `ERROR` | Resolver failed without inventing a result. |

These names are `PROPOSED`; an accepted contract owns the final vocabulary.

### Forbidden outcomes

The resolver must not:

- activate the source;
- select a provider silently;
- start network I/O;
- create a SourceDescriptor;
- create RAW data;
- emit an EvidenceBundle;
- approve release;
- return a public artifact.

### Promotion is separate

Even if the alias resolves successfully:

```text
alias resolution
  != connector activation
  != source admission
  != data validation
  != proof closure
  != release approval
  != publication
```

[Back to top](#top)

---

## Consumer, import, and configuration boundary

### Import namespace

The repository-present package namespace is `openstreetmap` under `connectors/openstreetmap/src/openstreetmap/`. No `osm` Python package was established by the bounded inspection.

Do not add:

```python
import osm
```

or compatibility shims under this lane without:

- verified consumers;
- an accepted migration need;
- import-safety tests;
- deprecation policy;
- collision analysis;
- packaging analysis;
- rollback plan.

### Configuration aliases

Configuration may eventually accept `osm` as an input alias, but only if the owning configuration contract defines deterministic normalization.

Illustrative only:

```yaml
connector: openstreetmap
accepted_aliases:
  - osm
```

This is not a current canonical schema.

### Consumer migration checklist

Before changing a spelling:

1. inventory repository and deployment consumers;
2. identify package/import/config/source-ID/reference classes separately;
3. freeze new references to the deprecated form;
4. define deterministic normalization;
5. add valid and invalid fixtures;
6. test ambiguous, missing, deprecated, and rollback states;
7. update docs and registry references;
8. preserve historical receipt and evidence lineage;
9. provide correction and rollback steps;
10. verify no public or scheduled path bypasses activation.

### Generated references

If docs, configs, or indexes are generated, update the canonical source and regenerate. Do not edit a generated alias independently.

[Back to top](#top)

---

## Validation and CI guardrails

### Current validation boundary

No dedicated executable alias-lane validator was established by the bounded inspection. The canonical OpenStreetMap test README defines expected no-network testing, but documentation does not prove those tests exist or run.

### Recommended no-new-files guard

**PROPOSED:** add a repository validator in a separate change that fails when unexpected files appear under `connectors/osm/`.

Illustrative policy:

```text
allowed:
  connectors/osm/README.md

deny unless migration manifest authorizes:
  connectors/osm/pyproject.toml
  connectors/osm/src/**
  connectors/osm/tests/**
  connectors/osm/fixtures/**
  connectors/osm/config/**
  connectors/osm/data/**
```

The validator location and implementation require Directory Rules preflight.

### Required validation categories

A future alias implementation or migration must prove:

- README-only or manifest-authorized file inventory;
- one-way canonical resolution;
- no duplicate package or import namespace;
- no duplicate source descriptors;
- no duplicate provider profiles;
- no duplicate fixtures or tests;
- no duplicate schedules;
- no duplicate receipts or release paths;
- no network on import/resolution;
- no secrets;
- deterministic ambiguity handling;
- historical reference preservation;
- correction and rollback behavior.

### Negative fixtures

Negative fixtures should cover:

- both aliases marked canonical;
- two source descriptors for one source/product;
- alias resolver starts network I/O;
- alias selects a provider implicitly;
- alias package shadows the canonical package;
- source ID changes when spelling changes;
- deprecated alias accepted without warning;
- migration omits a consumer;
- rollback cannot restore prior resolution;
- sensitive or secret values embedded in alias config.

### Documentation validation

For this README revision:

- one H1;
- unique H2 headings;
- balanced code fences;
- valid local anchors;
- no trailing whitespace;
- no secret-like values;
- links remain relative and responsibility-root aware;
- no claim that alias status activates implementation.

[Back to top](#top)

---

## Migration, deprecation, and tombstone procedure

### No migration implied

This README does not move, rename, delete, symlink, or deprecate either lane. It records the current topology and the controls required for future change.

### Possible governed dispositions

| Disposition | Meaning | Minimum evidence |
|---|---|---|
| Keep README-only alias | `openstreetmap/` remains implementation lane; `osm/` points to it. | Root note or ADR, no-new-files guard, consumer inventory. |
| Deprecate alias | New `osm` references denied; existing references migrate. | Migration manifest, deprecation period, tests, correction sweep. |
| Tombstone alias | README remains solely to explain removal and rollback. | Completed migration, no consumers, rollback card. |
| Make `osm/` canonical | Full lane migrates from `openstreetmap/`. | Accepted ADR, consumer/source-ID/package migration, redirects, tests, rollback. |
| External-export alias | Alias exists for downstream tooling only. | Explicit consumer contract and generated/mirror status. |

### Migration manifest requirements

A migration should identify:

- decision ID;
- old and new path;
- old and new package/import names;
- old and new source IDs, if any;
- alias rules;
- affected descriptors;
- affected configs and schedules;
- affected code and tests;
- affected fixtures;
- affected receipts/evidence/release references;
- deprecation date;
- removal criteria;
- correction sweep;
- rollback target;
- reviewers and approvals.

### Canonicalization principles

- Prefer one implementation.
- Prefer one package.
- Prefer one test lane.
- Prefer one source identity per product/profile.
- Preserve historical provenance.
- Avoid silent redirects.
- Avoid alias cycles.
- Keep changes reversible.
- Do not combine source activation with a path migration unless both are separately reviewed.

### Tombstone behavior

A tombstone README should:

- name the former path;
- identify the accepted canonical path;
- cite the migration decision;
- state the effective date;
- deny new implementation;
- document rollback;
- avoid executable redirect behavior unless explicitly contracted.

[Back to top](#top)

---

## Correction, deactivation, and rollback

### Documentation correction

A correction to this README should:

- preserve the prior commit and blob in history;
- explain the incorrect topology or claim;
- update related parent/source/test docs where necessary;
- avoid changing implementation in the same hidden step;
- identify downstream references requiring correction.

### Alias deactivation

If the alias creates ambiguity or unsafe behavior, deactivation may include:

- denying new `osm` references;
- removing resolver configuration;
- disabling an import shim;
- updating schedules/configs;
- preserving a tombstone README;
- issuing correction notices for public docs;
- sweeping registry and receipt references.

Deactivation must not require deleting provenance.

### Source deactivation is separate

Disabling an alias does not deactivate OpenStreetMap. Disabling OpenStreetMap does not automatically remove an alias. Source activation/deactivation belongs to the source registry and policy/operations surfaces.

### Rollback triggers

Rollback may be required when:

- consumers break after path normalization;
- source IDs split;
- package imports collide;
- scheduled jobs use the wrong connector;
- provider profiles bind incorrectly;
- historical receipts cannot resolve;
- alias resolution starts network I/O;
- sensitive data lands under the alias lane;
- rights or attribution lineage becomes ambiguous.

### Documentation-only rollback

This README revision can be rolled back by reverting its commit. It creates no implementation, descriptor, data, receipt, proof, policy, or release state.

[Back to top](#top)

---

## Directory map

### Confirmed current alias lane

```text
connectors/osm/
└── README.md          # compatibility boundary; this file
```

### Confirmed current OpenStreetMap lane

```text
connectors/openstreetmap/
├── README.md
├── pyproject.toml
├── src/
│   ├── README.md
│   └── openstreetmap/
│       ├── README.md
│       └── __init__.py
└── tests/
    └── README.md
```

### Denied speculative alias tree

```text
connectors/osm/
├── pyproject.toml     # DENY without accepted migration
├── src/               # DENY without accepted migration
├── tests/             # DENY without accepted migration
├── fixtures/          # DENY without accepted migration
├── config/            # DENY without accepted migration
└── data/              # DENY always; lifecycle data belongs under data/
```

### Related responsibility map

| Responsibility | Home |
|---|---|
| Connector coordination | `connectors/openstreetmap/` |
| Connector package source | `connectors/openstreetmap/src/openstreetmap/` |
| Connector tests | `connectors/openstreetmap/tests/` |
| OpenStreetMap source doctrine | `docs/sources/catalog/openstreetmap/` |
| Product/distribution doctrine | `docs/sources/catalog/openstreetmap/<product>.md` |
| Source descriptors and activation | `data/registry/sources/` |
| Source schema | `schemas/contracts/v1/source/` |
| Rights policy | `policy/rights/` |
| Sensitivity policy | `policy/sensitivity/` |
| RAW/QUARANTINE data | `data/raw/`, `data/quarantine/` |
| Connector receipts | `data/receipts/` |
| Proofs | `data/proofs/` |
| Release and rollback | `release/` |
| Public serving | governed `apps/` after release |

### Placement test

> If a file implements or tests OpenStreetMap source admission, it belongs under the accepted OpenStreetMap connector lane, not the alias. If it defines source meaning, rights, policy, schema, lifecycle data, proof, release, or public behavior, it belongs in that responsibility root instead.

[Back to top](#top)

---

## Definition of done

### This README revision

| Criterion | Status |
|---|---:|
| identifies `connectors/osm/` as README-only compatibility surface | `PASS` |
| records the fuller `connectors/openstreetmap/` lane without claiming production maturity | `PASS` |
| corrects the stale claim that source-family documentation was absent | `PASS` |
| records checked absence of alias package/source/test roots | `PASS` |
| prevents parallel package, source, tests, descriptors, provider profiles, receipts, and release paths | `PASS` |
| preserves connector RAW/QUARANTINE/receipt boundary | `PASS` |
| defines identity, rights, sensitivity, migration, correction, and rollback obligations | `PASS` |
| changes no code, package metadata, source, tests, fixtures, descriptors, policy, data, receipts, proofs, or releases | `PASS` |
| verifies repository-native checks after PR creation | `PENDING UNTIL CI` |

### Future resolved alias

The alias posture is done only when:

- owners are assigned;
- final alias class is accepted;
- canonical connector path is recorded;
- package/import/config/source-ID reference classes are separated;
- consumer inventory is complete;
- no duplicate implementation or test lane exists;
- source descriptors cannot split across spellings;
- current rights/provider decisions remain external and resolvable;
- no-new-files and ambiguity tests pass;
- migration, correction, deactivation, and rollback are exercised;
- related documentation is consistent;
- publication remains separately governed.

### Future canonical-path migration

A migration is not done until:

- ADR or migration decision is accepted;
- all consumers are inventoried;
- source identities and historical lineage are preserved;
- imports/configs/schedules are migrated deterministically;
- redirects or tombstones are explicit;
- valid and invalid fixtures pass;
- no network occurs during alias resolution;
- rollback restores the prior working state;
- release and public surfaces are swept for stale references.

[Back to top](#top)

---

## Open verification register

| ID | Question | Status | Evidence needed |
|---|---|---|---|
| `OSM-ALIAS-001` | What is the accepted final class of `connectors/osm/`? | `CONFLICTED / NEEDS VERIFICATION` | Accepted ADR, root note, or migration decision. |
| `OSM-ALIAS-002` | Is `connectors/openstreetmap/` formally canonical or only the current implementation lane? | `NEEDS VERIFICATION` | Accepted path decision and migration posture. |
| `OSM-ALIAS-003` | Are there any consumers using `connectors/osm/` as code, config, import, or schedule identity? | `UNKNOWN` | Repository/deployment-generated consumer inventory. |
| `OSM-ALIAS-004` | What is the accepted Python package and import namespace compatibility policy? | `NEEDS VERIFICATION` | Packaging contract, consumer tests, migration decision. |
| `OSM-ALIAS-005` | What canonical source-family, product, and SourceDescriptor identifiers are accepted? | `NEEDS VERIFICATION` | Registry contract and active descriptor records. |
| `OSM-ALIAS-006` | May `osm` appear as a machine alias in configs or descriptors? | `NEEDS VERIFICATION` | Accepted schema/normalization contract and tests. |
| `OSM-ALIAS-007` | Which provider/distribution profiles are approved? | `UNKNOWN` | Source activation decisions, current terms, operations review. |
| `OSM-ALIAS-008` | Which rights, attribution, derivative, redistribution, and share-alike decisions are current? | `NEEDS VERIFICATION` | Rights review and release obligations. |
| `OSM-ALIAS-009` | Does a validator enforce README-only alias inventory? | `UNKNOWN` | Validator code, negative fixture, CI result. |
| `OSM-ALIAS-010` | Are generated docs or indexes derived from a canonical alias registry? | `UNKNOWN` | Generator/config evidence. |
| `OSM-ALIAS-011` | How are old alias references corrected in receipts, evidence, catalogs, and releases? | `NEEDS VERIFICATION` | Correction contract and impact-sweep tooling. |
| `OSM-ALIAS-012` | What deprecation period and tombstone behavior apply if the alias is retired? | `NEEDS VERIFICATION` | Migration policy and rollback card. |
| `OSM-ALIAS-013` | What is the exhaustive recursive inventory of the alias and canonical lanes? | `NEEDS VERIFICATION` | Repository-generated inventory at a pinned commit. |
| `OSM-ALIAS-014` | Are any external deployments or notebooks depending on the short path? | `UNKNOWN` | Deployment, workflow, and external-consumer inventory. |
| `OSM-ALIAS-015` | How does alias resolution behave when the source is suspended or rights are unresolved? | `NEEDS VERIFICATION` | Resolver, registry, policy, and operational tests. |

[Back to top](#top)

---

## Evidence ledger

| Evidence | Status | What it supports | What it does not prove |
|---|---:|---|---|
| target prior blob `514dd57e…` | `CONFIRMED` | Existing short-name alias posture and source-admission boundary. | Final naming decision or implementation. |
| Directory Rules blob `2affb080…` | `CONFIRMED DOCTRINE` | Connector responsibility root, compatibility anti-duplication, lifecycle and release boundaries. | Current child implementation. |
| connectors root README blob `bdd50032…` | `CONFIRMED ROOT CONTRACT` | RAW/QUARANTINE/receipt connector authority and exclusions. | OpenStreetMap activation. |
| canonical connector README blob `3d25e611…` | `CONFIRMED DOCUMENTATION` | Current long-name connector topology, restrictions, maturity, and backlog. | Executable correctness or source activation. |
| source-root README blob `8364bfb2…` | `CONFIRMED DOCUMENTATION` | Source-tree and import-safety boundary. | Executable modules or tests. |
| canonical package metadata blob `db4ce6f2…` | `CONFIRMED PLACEHOLDER` | Package name and version `0.0.0`. | Installability or behavior. |
| empty initializer blob `e69de29b…` | `CONFIRMED EMPTY FILE` | Package path exists. | Public API or implementation. |
| source-family README blob `3c3974c3…` | `CONFIRMED DOCUMENTATION` | Dedicated source-family doctrine and rights/source-role posture. | Active descriptor or final rights decision. |
| bounded alias path checks | `CONFIRMED BOUNDED RESULT` | README-only result and absence of three checked implementation roots. | Exhaustive recursive absence. |
| repository code search | `CONFIRMED BOUNDED RESULT` | Alias references in canonical and domain/source documentation. | External consumers or unindexed branches. |

### Evidence hierarchy

Current repository files, accepted contracts, tests, workflows, logs, and release records outrank planning documents for implementation behavior. Directory Rules and governing doctrine control responsibility placement. The fuller OpenStreetMap connector boundary controls current connector guidance; this alias cannot override it.

[Back to top](#top)

---

## Maintainer note

Keep `connectors/osm/` boring, README-only, and one-way.

Do not add implementation here because the abbreviation is convenient. Do not create a second package, second source tree, second tests lane, second provider-profile registry, second source identity, second receipt path, or second release path.

Use [`connectors/openstreetmap/`](../openstreetmap/README.md) for current connector implementation documentation, [`docs/sources/catalog/openstreetmap/`](../../docs/sources/catalog/openstreetmap/README.md) for source doctrine, and the appropriate responsibility roots for registry, policy, lifecycle data, proofs, and release decisions.

<p align="right"><a href="#top">Back to top</a></p>
