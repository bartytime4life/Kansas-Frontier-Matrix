<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/tools-validators-bridge-river-crossing-readme
title: tools/validators/bridge_river_crossing/ — Bridge and River-Crossing Validator Specialization Boundary
type: readme; directory-readme; validator-specialization; crossings-child; roads-rail-trade; hydrology-boundary; infrastructure-boundary; non-authoritative
version: v0.2
status: draft; repository-grounded; README-only-lane; executable-enforcement-unestablished; generic-crossings-parent-confirmed; roads-rail-trade-domain-index-confirmed; transport-topology-adjacent; contracts-draft; paired-schemas-missing; crossings-schema-index-only; policy-greenfield; dedicated-tests-unestablished; shared-validator-runtime-confirmed; aggregate-registration-absent; domain-ci-todo-only; sensitivity-aware; not-live-routing; not-safety-authority; fail-closed
owners: OWNER_TBD — Roads/Rail/Trade steward · Crossings steward · Bridge steward · Hydrology steward · Settlements/Infrastructure steward · Hazards steward · Archaeology/Cultural Heritage reviewer · Graph/topology steward · Source-role steward · Temporal/freshness steward · Geometry steward · Rights/sensitivity reviewer · Evidence steward · Policy steward · Security reviewer · Release steward · Correction/rollback steward · CI steward · Docs steward
created: 2026-07-07
updated: 2026-07-16
supersedes: v0.1 proposed bridge and river-crossing validator guide
policy_label: "repository-facing; tools; validators; crossings-child; bridge; river-crossing; ford; transport-side-claim; carried-object; crossed-object; hydrology-reference; infrastructure-reference; graph-derived; spatial-intersection-not-evidence; source-role; temporal-scope; current-status; legal-access; structural-condition; flood-condition; archaeology; cultural-corridor; critical-infrastructure; evidence-aware; policy-aware; release-gated; correction-aware; rollback-aware; no-network-by-default; fail-closed; no-truth-authority; no-routing-authority; no-safety-authority; no-release-authority"
owning_root: tools/
current_path: tools/validators/bridge_river_crossing/README.md
responsibility: >
  Repository-grounded specialization, orchestration, and routing boundary for deterministic checks over Roads/Rail/Trade
  Bridge and RiverCrossing candidates. This lane preserves transport-side claim scope; generic Crossing, Bridge,
  RiverCrossing, Ferry, route, segment, facility, event, restriction, Hydrology, infrastructure, archaeology, hazards, and
  graph boundaries; carried-versus-crossed references; source role; temporal and current-status posture; geometry and
  topology lineage; sensitivity and rights; evidence closure; policy obligations; release state; correction lineage; and
  rollback while delegating generic crossing checks to tools/validators/crossings/ and domain-specific truth to owning
  lanes. It never becomes bridge asset truth, water truth, structural-condition authority, legal-access authority, live
  routing, safe-passage advice, emergency guidance, graph truth, policy authority, evidence authority, or publication
  authority.
truth_posture: >
  CONFIRMED target README v0.1 and prior blob; bounded repository search surfaced only README.md under
  tools/validators/bridge_river_crossing/ and no validate_bridge_river_crossing executable,
  BRIDGE_RIVER_CROSSING_VALIDATION producer, or dedicated test implementation; tools/validators/crossings/ is the generic
  parent and names this lane as the bridge/river-crossing child; tools/validators/domains/roads-rail-trade/ is the per-domain
  transport validator index; tools/validators/transport-facility-topology/ is an adjacent topology/facility boundary;
  Bridge and River Crossing semantic contracts exist as draft v0.2 documents and explicitly deny structural, Hydrology,
  live-status, legal-access, navigation, safe-passage, graph, and publication authority; both paired schemas are missing;
  the Roads/Rail/Trade schema lane contains only an index in its confirmed inventory and records roads-rail-trade versus
  transport slug/path conflict; schemas/contracts/v1/crossings/ is compatibility/index-only; Roads/Rail/Trade policy is a
  greenfield scaffold; domain tests are documentation-led with executable behavior and pass rates unverified; the shared
  validator runtime exists elsewhere but this specialization did not surface in the five-entry aggregate; the domain
  workflow executes TODO-only echo steps / PROPOSED immutable specialization packet, deterministic parent/child result
  envelope, finite findings and reason codes, no-network public-safe fixtures, sensitivity and carrier checks, CI admission,
  correction cascade, migration, deprecation, and rollback / CONFLICTED or drift-prone generic parent versus specialization
  ownership, roads-rail-trade versus transport contract/schema slugs, domain-first versus subtype-first source registry
  topology, crossings compatibility schema versus domain schema candidates, and stale README inventories /
  NEEDS VERIFICATION owners, CODEOWNERS, canonical executable and registry entry, complete child/dependency manifest,
  accepted contracts/schemas, source descriptors and rights, policy entrypoints, status/freshness profiles, sensitivity
  profiles, meaningful fixtures/tests, structured report destination, CI significance, correction cascade, and
  release-gate adoption / UNKNOWN runtime invocation, production consumers, emitted reports, operational metrics,
  deployment, current pass results, and branch-protection significance
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  repository_id: "1059091169"
  visibility: public
  base_ref: main
  base_commit: "0bc925d42301025dbf5e5ce08a154bbc35388bca"
  prior_blob: 3e564b643394c3e84716222a9e2e90e8d245f2cd
  bridge_contract_blob: 2d00036dcd47c5fac7ee43679ada4682ee654776
  river_crossing_contract_blob: 1f9779a6aeb08110c77ef0b5a3ecff19fd602bda
  crossings_parent_blob: 7807275a0afca4aa1518787a392225e2732a6757
  roads_rail_trade_validator_index_blob: 1d5942ab5499cd752974aee804372d89e3c315c0
  transport_facility_topology_blob: 35773f93f2d3a4684e4419719e9e79b724cb06fa
  graph_projections_blob: 4031c319e0eb1dc8a79e2ca5953311cc37c08115
  roads_rail_trade_schema_index_blob: 91cd62a640d5a91270564727ff3704a8c236b012
  crossings_schema_index_blob: cf4ef35500c71060065e80b8ce7ae0aac2dc9665
  roads_rail_trade_policy_blob: 508062700bc3f56fb05914290fc160d7634b53f4
  roads_rail_trade_tests_blob: 3c362bf18f228e5b23a533eb4fc0214ca80a614a
  roads_rail_trade_workflow_blob: c6f547b0acd8018284001ed67d25b153c0d9992b
  roads_rail_trade_source_registry_blob: 54087e02e329b98c595807e4c9041c97972c0179
  roads_rail_trade_sensitivity_blob: 59870cd850b6491488578a296294691e8c9c50eb
  validators_root_blob: e35742288404a1eeb214f8269fbacb1429c0f86a
  validator_tests_parent_blob: c703a64eef3f69044a54696f121f4e5ae05a3631
  directory_rules_blob: 2affb080e6f0043867c64c7f06c1ca52030fbd55
  generated_receipt_schema_blob: fba21ed27ebccf1362fe397fe0c3ebd85e072685
  bounded_path_checks:
    - tools/validators/bridge_river_crossing/ surfaced only README.md
    - validate_bridge_river_crossing, BRIDGE_RIVER_CROSSING_VALIDATION, and test_bridge_river_crossing searches returned no implementation
    - tools/validators/crossings/ is the generic parent; bridge_river_crossing is the confirmed documented specialization
    - paired bridge.schema.json and river_crossing.schema.json were not confirmed
    - schemas/contracts/v1/crossings/ is compatibility/index-only
    - policy/domains/roads-rail-trade/README.md is a PROPOSED greenfield scaffold
    - tests/domains/roads-rail-trade/ is documentation-led; executable crossing tests were not confirmed
    - domain-roads-rail-trade workflow executes TODO echo commands
related:
  - ../README.md
  - ../_common/README.md
  - ../crossings/README.md
  - ../domains/roads-rail-trade/README.md
  - ../transport-facility-topology/README.md
  - ../geometry/README.md
  - ../freshness/README.md
  - ../evidence/README.md
  - ../citation/README.md
  - ../policy/README.md
  - ../release/README.md
  - ../cross-domain-joins/README.md
  - ../cross-lane/README.md
  - ../../../contracts/domains/roads-rail-trade/bridge.md
  - ../../../contracts/domains/roads-rail-trade/river_crossing.md
  - ../../../contracts/domains/roads-rail-trade/crossing.md
  - ../../../contracts/domains/roads-rail-trade/ferry.md
  - ../../../contracts/domains/roads-rail-trade/access_restriction.md
  - ../../../contracts/domains/roads-rail-trade/status_event.md
  - ../../../contracts/domains/roads-rail-trade/restriction_event.md
  - ../../../contracts/domains/roads-rail-trade/network_node.md
  - ../../../contracts/domains/roads-rail-trade/network_edge.md
  - ../../../docs/domains/roads-rail-trade/OBJECT_FAMILIES.md
  - ../../../docs/domains/roads-rail-trade/IDENTITY_MODEL.md
  - ../../../docs/domains/roads-rail-trade/GRAPH_PROJECTIONS.md
  - ../../../docs/domains/roads-rail-trade/SENSITIVITY.md
  - ../../../docs/domains/hydrology/README.md
  - ../../../docs/domains/settlements-infrastructure/
  - ../../../schemas/contracts/v1/domains/roads-rail-trade/README.md
  - ../../../schemas/contracts/v1/crossings/README.md
  - ../../../policy/domains/roads-rail-trade/README.md
  - ../../../data/registry/sources/roads-rail-trade/README.md
  - ../../../data/proofs/
  - ../../../data/receipts/
  - ../../../release/
  - ../../../tests/domains/roads-rail-trade/README.md
  - ../../../tests/validators/README.md
  - ../../../.github/workflows/domain-roads-rail-trade.yml
  - ../../../docs/doctrine/directory-rules.md
tags: [kfm, tools, validators, bridge, river-crossing, ford, crossings, roads-rail-trade, hydrology, infrastructure, hazards, archaeology, graph, topology, source-role, time, freshness, sensitivity, evidence, policy, release, correction, rollback]
notes:
  - "This revision changes only tools/validators/bridge_river_crossing/README.md plus the required generated provenance receipt."
  - "No validator executable, schema, semantic contract, policy rule, source descriptor, fixture, test, workflow, pipeline, lifecycle object, EvidenceBundle, release record, route status, bridge condition, water condition, graph artifact, model call, or public artifact is created or modified."
  - "The README contains no current conditions, operational guidance, restricted infrastructure detail, precise cultural/archaeological location, private access detail, hidden policy threshold, or control-defeating value."
  - "A future executable must remain a thin specialization under the generic crossings parent and must not duplicate shared topology, geometry, freshness, evidence, policy, or release logic."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Bridge and River-Crossing Validator Specialization Boundary

`tools/validators/bridge_river_crossing/`

> **One-line purpose.** Define the deterministic child-validator boundary for Bridge and RiverCrossing candidates under the generic Crossings parent—preserving carried-versus-crossed identity, Hydrology and infrastructure references, source role, time/current-status posture, graph derivation, sensitivity, evidence, policy, release, correction, and rollback without becoming bridge-asset truth, water truth, structural/safe-passage authority, legal-access authority, live routing, graph truth, or publication authority.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Version: v0.2" src="https://img.shields.io/badge/version-v0.2-informational">
  <img alt="Root: tools" src="https://img.shields.io/badge/root-tools%2F-blue">
  <img alt="Role: crossings child" src="https://img.shields.io/badge/role-crossings__child-blueviolet">
  <img alt="Implementation: README only" src="https://img.shields.io/badge/implementation-README__only-orange">
  <img alt="Schemas: missing" src="https://img.shields.io/badge/paired__schemas-missing-red">
  <img alt="Boundary: not live routing" src="https://img.shields.io/badge/boundary-not__live__routing-critical">
  <img alt="Posture: cite or abstain" src="https://img.shields.io/badge/posture-cite__or__abstain-success">
</p>

> [!IMPORTANT]
> **Current specialization enforcement is not established.** Bounded repository search surfaced only this README under `tools/validators/bridge_river_crossing/`; no specialization executable, result producer, dedicated test lane, emitted report, or runtime consumer was confirmed.

> [!CAUTION]
> **Geometry and proximity are not crossing evidence.** A line crossing a water polygon, a point near a stream, a map label, a graph edge, an OCR result, or generated text does not prove a bridge, ford, ferry, legal crossing, current passage, or transport relationship.

> [!WARNING]
> **This lane is never structural, navigation, access, or emergency authority.** It must deny or abstain from bridge-condition, load/clearance, fordability, water-depth/flow, flood state, navigability, legal access, right-of-way, current closure, service availability, emergency routing, and safe-passage claims unless a separate governed authoritative path supports the exact requested use. Validator success still does not authorize such use.

**Quick links:** [Purpose](#purpose) · [Status](#status-and-evidence) · [Placement](#directory-rules-and-authority) · [Inventory](#confirmed-repository-inventory) · [Topology](#validator-topology-and-delegation) · [Ownership](#domain-and-object-ownership-boundary) · [Families](#object-family-and-specialization-model) · [Packet](#validation-input-packet) · [Invariants](#specialization-validation-invariants) · [Operational](#operational-safety-and-access-boundary) · [Sensitivity](#sensitivity-rights-and-public-surface-boundary) · [Report](#validation-report-contract) · [Outcomes](#finite-outcomes-and-reason-codes) · [Maturity](#contract-schema-policy-source-and-test-maturity) · [Security](#security-untrusted-content-and-resource-limits) · [Lifecycle](#lifecycle-release-correction-and-rollback) · [Tests](#tests-fixtures-and-no-network-posture) · [CI](#ci-admission-contract) · [Implementation](#smallest-sound-implementation-sequence) · [Done](#definition-of-done) · [Migration](#migration-compatibility-and-deprecation) · [Open](#open-verification-register) · [Rollback](#rollback-path) · [Ledger](#evidence-ledger) · [Changelog](#changelog)

---

<a id="purpose"></a>

## Purpose

`tools/validators/bridge_river_crossing/` is the narrow Roads/Rail/Trade validator specialization for Bridge and RiverCrossing candidates.

The durable validation question is:

> Does the candidate remain a source-scoped transport-side crossing claim with explicit carried and crossed objects, correct specialization, governed Hydrology and infrastructure references, bounded source role and time, evidence-supported geometry/topology, safe sensitivity posture, and complete policy/release/correction/rollback support for the requested use?

This lane may eventually orchestrate deterministic checks for:

- Bridge versus RiverCrossing versus generic Crossing versus Ferry classification;
- carried transport object and crossed object identity;
- bridge transport-role versus canonical infrastructure-asset identity;
- river/watercourse reference versus transport-side crossing relation;
- road, rail, trail, route, corridor, membership, facility, status, and restriction references;
- observed, administrative, regulatory, modeled, aggregate, candidate, synthetic, historic, and contextual roles;
- source time, observed/asserted time, valid/effective time, retrieval time, status time, release time, correction time, and stale state;
- geometry role, spatial support, uncertainty, topology derivation, and graph lineage;
- critical-infrastructure, cultural-corridor, archaeology-adjacent, private-access, and restricted-source sensitivity;
- EvidenceRef/EvidenceBundle, PolicyDecision, ReviewRecord, receipt, ReleaseManifest, correction, withdrawal, and rollback linkage;
- public-map, tile, API, search, graph, Focus Mode, export, screenshot, embedding, and AI carrier boundaries.

It must not:

- define Bridge, RiverCrossing, Crossing, Ferry, Hydrology, or infrastructure meaning;
- infer a crossing merely from geometry;
- decide structural condition, passability, access, closure, flood state, navigability, or safety;
- create SourceDescriptors, EvidenceBundles, PolicyDecisions, receipts, or release records;
- materialize graph truth or route guidance;
- publish or approve a public artifact.

[Back to top](#top)

---

<a id="status-and-evidence"></a>

## Status and evidence

### Confirmed snapshot

| Surface | Current-session finding | Truth label |
|---|---|---|
| `tools/validators/bridge_river_crossing/README.md` | v0.1 existed with prior blob `3e564b643394c3e84716222a9e2e90e8d245f2cd`. | **CONFIRMED** |
| Direct specialization inventory | Bounded search surfaced only this README. | **CONFIRMED**, bounded |
| Specialization executable | No `validate_bridge_river_crossing*` implementation surfaced. | **NOT FOUND in bounded search** |
| Result producer | No `BRIDGE_RIVER_CROSSING_VALIDATION*` producer surfaced. | **NOT FOUND in bounded search** |
| Dedicated tests | No dedicated specialization test implementation surfaced. | **NOT FOUND in bounded search** |
| Generic parent | `tools/validators/crossings/README.md` exists and identifies this lane as the Bridge/RiverCrossing child. | **CONFIRMED README** |
| Domain parent | `tools/validators/domains/roads-rail-trade/README.md` exists as the per-domain validator index. | **CONFIRMED README** |
| Adjacent topology lane | `tools/validators/transport-facility-topology/README.md` exists for facility/node/edge topology boundaries. | **CONFIRMED README** |
| Shared validator runtime | Shared JSON Schema runner and aggregate exist elsewhere; direct validator tests remain incomplete. | **CONFIRMED adjacent implementation / partial coverage** |
| Aggregate registration | No Bridge/RiverCrossing entrypoint surfaced in the documented five-entry aggregate. | **NOT CONFIRMED** |
| Contracts | Bridge and River Crossing v0.2 semantic contracts exist. | **CONFIRMED draft contracts** |
| Paired schemas | Both contracts report their paired schemas missing. | **CONFIRMED contract finding / current existence NEEDS VERIFICATION** |
| Domain schema lane | Index exists; its checked inventory confirms no concrete schema. | **CONFIRMED index / implementation NEEDS VERIFICATION** |
| Crossings schema lane | Compatibility/index-only; canonical status unresolved. | **CONFIRMED compatibility README** |
| Domain policy | Greenfield scaffold. | **CONFIRMED file / enforcement PROPOSED** |
| Domain tests | Documentation-led parent and child READMEs; executable behavior/pass rates unverified. | **CONFIRMED docs / execution NEEDS VERIFICATION** |
| Domain workflow | TODO-only echo steps. | **CONFIRMED** |
| Runtime use and current results | No logs, reports, consumers, deployment evidence, or current results inspected. | **UNKNOWN** |

### What this revision establishes

This README establishes a **reviewable design and routing contract**. It does not establish executable enforcement.

### What this revision does not prove

It does not prove:

- a validator package or CLI exists;
- bridge or river-crossing schemas exist;
- source descriptors are active;
- policy evaluation is wired;
- test fixtures exist;
- CI blocks on this specialization;
- graph projections are operational;
- public APIs or maps consume these records;
- current bridge, crossing, water, access, or closure conditions;
- any release is approved.

[Back to top](#top)

---

<a id="directory-rules-and-authority"></a>

## Directory Rules and authority

Directory Rules assign durable validators and checker helpers to `tools/`. The target therefore remains under:

```text
tools/validators/bridge_river_crossing/
```

This is the smallest sound documentation change because the directory already exists and the requested work is validator-specialization guidance.

### Responsibility split

| Responsibility | Owning root or lane | This specialization's role |
|---|---|---|
| Generic crossing-family invariants | `tools/validators/crossings/` | Depend on or delegate; do not duplicate. |
| Bridge/RiverCrossing specialization checks | `tools/validators/bridge_river_crossing/` | Narrow orchestration boundary. |
| Domain-wide transport validation | `tools/validators/domains/roads-rail-trade/` | Parent route for Roads/Rail/Trade checks. |
| Facility/node/edge topology | `tools/validators/transport-facility-topology/` | Adjacent dependency where facility/topology is involved. |
| Shared geometry checks | `tools/validators/geometry/` | Validate geometry carriers and declared geometry roles. |
| Freshness/stale-state checks | `tools/validators/freshness/` | Shared time/status dependency. |
| Domain meaning | `docs/domains/...`, `contracts/domains/...` | Validators consume; they do not define. |
| Machine shape | Accepted `schemas/contracts/v1/...` lane | Validators consume accepted schema references. |
| Source admission and authority | `data/registry/sources/...` and source-validator lanes | Validators check references and role posture. |
| Hydrology truth | Hydrology docs/contracts/data | Cite; never absorb. |
| Infrastructure/place/asset truth | Settlements/Infrastructure docs/contracts/data | Cite; never absorb. |
| Hazards and operational event truth | Hazards/source-specific lanes | Cite; never become alert authority. |
| Archaeology/cultural truth | Archaeology/Cultural Heritage lanes | Cite only under sensitivity policy. |
| Policy decisions | `policy/` and accepted decision stores | Consume decisions; never decide locally. |
| Evidence/proofs/receipts | `data/proofs/`, `data/receipts/` | Resolve/check; never store locally. |
| Lifecycle records | `data/` lifecycle roots | Never use validator path as data store. |
| Release/correction/rollback | `release/` | Check references; never approve publication. |
| Executable proof | `tests/`, `fixtures/` | Tests consume this design; README is not proof. |
| Public serving | Governed applications/APIs over released derivatives | No direct read from this lane. |

### Denied placement shortcuts

Do not use this directory for:

- semantic contracts;
- JSON Schemas or enums;
- source descriptors;
- bridge, river, water, route, infrastructure, access, condition, or closure payloads;
- hidden policy thresholds or sensitivity parameters;
- evidence/proof/receipt instances;
- lifecycle data;
- graph/triplet outputs;
- release manifests or rollback cards;
- public API, map, tile, route, navigation, emergency, or AI runtime code.

[Back to top](#top)

---

<a id="confirmed-repository-inventory"></a>

## Confirmed repository inventory

### Direct lane

```text
tools/validators/bridge_river_crossing/
└── README.md
```

This is a bounded current-session inventory. Ignored, generated, unindexed, branch-local, dynamically loaded, package-local, or external code remains unknown.

### Nearby validator topology

```text
tools/validators/
├── crossings/                         # generic Crossing parent
├── bridge_river_crossing/             # this specialization
├── domains/roads-rail-trade/          # domain-wide parent/index
├── transport-facility-topology/       # facility/node/edge topology
├── geometry/                          # shared geometry-carrier checks
├── freshness/                         # shared stale/current-time checks
├── evidence/                          # evidence resolution checks
├── policy/                            # policy-result/check routing
├── release/                           # release/correction/rollback checks
├── cross-domain-joins/                # ownership/source-role join checks
└── cross-lane/                        # broad cross-lane invariants
```

### Confirmed semantic surfaces

The checked semantic contract lane includes:

- `bridge.md`;
- `river_crossing.md`;
- `crossing.md`;
- `ferry.md`;
- road and rail segment contracts;
- route/corridor/membership contracts;
- status and restriction contracts;
- network node and edge contracts;
- domain validation/report descriptors.

### Known maturity constraints

- Bridge and RiverCrossing contracts are draft and schema-missing.
- Schema placement is affected by `roads-rail-trade` versus `transport` and domain versus flat path drift.
- The generic `crossings` schema lane is compatibility/index-only.
- Policy is a scaffold.
- Tests are mostly README-defined in the inspected domain tree.
- The workflow does not execute substantive domain checks.
- Shared validator runtime does not establish registration or coverage for this specialization.

[Back to top](#top)

---

<a id="validator-topology-and-delegation"></a>

## Validator topology and delegation

This specialization should be a **thin child**, not a second generic crossing validator.

### Delegation map

| Concern | Primary validator lane | Bridge/RiverCrossing behavior |
|---|---|---|
| Generic crossing family and object separation | `crossings/` | Consume child result or delegate. |
| Spatial intersection is not evidence | `crossings/`, `geometry/` | Require generic result; add water/bridge specialization context. |
| Bridge/RiverCrossing-specific refs | this lane | Validate carried/crossed/Hydrology/infrastructure refs. |
| Road/Rail/Trade domain-wide object posture | `domains/roads-rail-trade/` | Consume or delegate. |
| Facility/node/edge topology | `transport-facility-topology/` | Delegate when facility or graph topology is present. |
| Geometry shape/role | `geometry/` | Delegate; this lane evaluates semantic use, not low-level geometry. |
| Time/current/stale posture | `freshness/` plus domain contracts | Delegate generic checks; enforce specialization consequences. |
| Evidence/citations | `evidence/`, `citation/` | Consume finite result. |
| Source role/rights | source/source-role/rights lanes | Consume finite result. |
| Sensitivity/geoprivacy | sensitivity/geoprivacy lanes | Consume most-restrictive result. |
| Policy | `policy/` | Consume PolicyDecision; do not calculate local allow. |
| Release/correction/rollback | `release/`, lifecycle/promotion lanes | Consume finite release readiness. |

### Dependency behavior

A future parent report must not convert dependency uncertainty into success.

| Dependency result | Specialization behavior |
|---|---|
| `PASS` | Continue specialization checks. |
| `FAIL` | Fail with child findings preserved. |
| `DENY` | Deny requested use. |
| `HOLD` / `REVIEW_REQUIRED` | Preserve hold/review state. |
| `ABSTAIN` | Abstain unless profile explicitly permits narrower evaluation. |
| `ERROR` / unavailable | Fail closed; do not silently skip. |
| Missing expected child | Emit bounded missing-dependency finding. |

### No duplicate authority

The specialization must not:

- reimplement generic crossing classification differently from `crossings/`;
- define another geometry validity vocabulary;
- create another source-role enum;
- define local freshness thresholds;
- define local infrastructure or Hydrology schemas;
- create a second graph/topology truth path;
- decide policy or release.

[Back to top](#top)

---

<a id="domain-and-object-ownership-boundary"></a>

## Domain and object ownership boundary

### Roads/Rail/Trade owns

For this seam, Roads/Rail/Trade owns the **transport-side claim** that a source relates a Bridge or RiverCrossing to movement, routes, segments, corridors, facilities, crossings, restrictions, status, or historic/trade interpretation.

It may own source-scoped:

- Bridge role in a transport network;
- RiverCrossing relation;
- carried transport object reference;
- crossed object relation reference;
- crossing specialization;
- route/segment/membership references;
- transport source role and temporal scope;
- transport-side uncertainty and limitations;
- release-facing transport interpretation.

### Hydrology owns

Hydrology retains authority over:

- waterbody, stream, river, reach, watershed, gauge, and hydro-feature identity;
- water level, flow, discharge, stage, flood/inundation, water quality, and current condition;
- hydrologic geometry and model outputs;
- fordability-relevant water evidence;
- water-condition freshness and uncertainty.

A `hydrology_ref` is a citation boundary, not a copied water object.

### Settlements/Infrastructure owns

Infrastructure/place/asset lanes retain authority over:

- canonical bridge or facility asset identity where applicable;
- structural components and condition;
- inspection, maintenance, load, clearance, vulnerability, and critical-infrastructure detail;
- facility/place identity and asset ownership context;
- structural serviceability.

An `infrastructure_asset_ref` is a citation boundary, not permission to copy restricted asset detail.

### Hazards owns

Hazards and official operational sources retain authority over:

- hazard event and cause;
- live warning/advisory context;
- flood/emergency event state;
- current operational closure where authoritative;
- emergency routing and life-safety context.

### Archaeology/Cultural Heritage owns

Archaeology and cultural stewardship lanes retain authority over:

- archaeological/cultural site identity;
- culturally significant crossing meaning;
- protected route/corridor interpretation;
- exact sensitive coordinates and steward-held context;
- release/generalization decisions for sensitive cultural material.

### People/Land and legal authorities own

Other owning lanes retain:

- property/title/right-of-way;
- private access;
- legal public-access status;
- permits and legal determinations;
- living-person/private records.

### Graph/triplet systems own no source truth

Graph projections may represent connectivity, but each projected node/edge must remain:

- derived;
- rebuildable;
- evidence-linked;
- sensitivity-inheriting;
- invalidatable;
- subordinate to canonical evidence and domain records.

[Back to top](#top)

---

<a id="object-family-and-specialization-model"></a>

## Object family and specialization model

### Required separation

| Object family | Meaning | Must not collapse into |
|---|---|---|
| `Crossing` | Generic transport-side crossing relation. | Bridge, RiverCrossing, Ferry, route, segment, graph edge, or confirmed intersection by default. |
| `Bridge` | Transport-side bridge claim and relation. | Full structural asset truth, inspection, load/clearance, legal access, or safe passage. |
| `RiverCrossing` | Transport-side watercourse/ford/crossing relation. | Hydrology truth, current water condition, fordability, navigability, or legal access. |
| `Ferry` | Ferry crossing/service claim. | Current operation, legal service, safe passage, or vessel/navigation authority. |
| `RoadSegment` / `RailSegment` | Transport segment identity/claim. | Bridge or crossing record. |
| `CorridorRoute` / `RouteMembership` | Route/corridor identity and membership. | Segment or crossing truth. |
| `TransportFacility` | Source-scoped transport facility role. | Canonical asset/place truth. |
| `StatusEvent` / `RestrictionEvent` / `AccessRestriction` | Time-scoped context. | The Bridge/RiverCrossing identity or current authoritative state. |
| `NetworkNode` / `NetworkEdge` | Derived graph projection. | Canonical crossing or source geometry. |
| `HistoricRouteClaim` / narrative | Time-scoped interpretive claim. | Modern route/access/current-condition truth. |

### Specialization consistency

A candidate declaring `Bridge` or `RiverCrossing` must:

- identify the declared object family;
- retain a generic crossing relationship where the accepted contract requires it;
- not declare mutually incompatible specializations without explicit multi-record modeling;
- not use `Bridge` and `RiverCrossing` as interchangeable field names;
- not infer `Ferry` or `Ford` from historical wording alone;
- preserve candidate/model/interpretive posture where specialization is uncertain;
- maintain stable identity independent of public label or graph node id.

### Carried versus crossed

A Bridge or RiverCrossing candidate should distinguish:

- `carried_object_ref`: what movement object is carried or represented;
- `crossed_object_ref`: what is crossed;
- `crossing_ref`: the generic or specialized crossing relation;
- `hydrology_ref`: water-system evidence where material;
- `infrastructure_asset_ref`: external asset identity where material;
- `facility_ref`: transport facility role where material;
- `status_refs` / `restriction_refs`: separate time-scoped context.

Missing or ambiguous roles must not be repaired by guessing from geometry or labels.

[Back to top](#top)

---

<a id="validation-input-packet"></a>

## Validation input packet

A future specialization should consume an immutable, versioned packet. The shape below is **PROPOSED**, not an accepted schema.

```yaml
profile:
  id: bridge-river-crossing
  version: <semver>
  digest: <content-hash>
  no_network: true

request:
  operation: validate
  requested_surface: <internal|review|map|api|graph|export|focus|ai|release>
  audience: <internal|reviewer|restricted|public>
  validation_instant: <RFC3339>
  strictness: <default|release>

candidate:
  id: <candidate-id>
  object_family: <Bridge|RiverCrossing>
  lifecycle_state: <RAW|WORK|QUARANTINE|PROCESSED|CATALOG|TRIPLET|PUBLISHED>
  source_role: <declared-role>
  knowledge_character: <observed|administrative|regulatory|modeled|aggregate|candidate|synthetic|historic|context>
  carried_object_ref: <ref|null>
  crossed_object_ref: <ref|null>
  crossing_ref: <ref|null>
  hydrology_ref: <ref|null>
  infrastructure_asset_ref: <ref|null>
  facility_ref: <ref|null>
  route_refs: []
  segment_refs: []
  status_refs: []
  restriction_refs: []
  geometry_ref: <ref|null>
  geometry_role: <point|line|area|generalized|derived|unknown>
  source_time: <RFC3339|null>
  observed_or_asserted_time: <RFC3339|null>
  valid_time: <interval|null>
  retrieval_time: <RFC3339|null>
  status_time: <RFC3339|null>
  release_time: <RFC3339|null>
  correction_time: <RFC3339|null>
  uncertainty: <structured|null>
  limitations: []

governance:
  source_descriptor_refs: []
  evidence_refs: []
  policy_decision_ref: <ref|null>
  review_refs: []
  receipt_refs: []
  release_manifest_ref: <ref|null>
  correction_ref: <ref|null>
  withdrawal_ref: <ref|null>
  rollback_ref: <ref|null>
  rights_state: <resolved|restricted|unknown>
  sensitivity_state: <public-safe|generalized|review|restricted|deny|unknown>

dependencies:
  generic_crossings_result: <result-ref|null>
  domain_result: <result-ref|null>
  topology_result: <result-ref|null>
  geometry_result: <result-ref|null>
  freshness_result: <result-ref|null>
  evidence_result: <result-ref|null>
  policy_result: <result-ref|null>
  release_result: <result-ref|null>
```

### Packet invariants

- Inputs are immutable for one run.
- Profile id/version/digest are recorded.
- Validation instant is explicit and pinned.
- No network is the default.
- All referenced objects resolve locally or return finite negative outcomes.
- Missing required dependencies do not silently disappear.
- The packet contains references and safe metadata, not restricted payload copies.
- Public requests require a released public-safe derivative, not merely a `PUBLISHED` label.
- Validation does not mutate lifecycle state or approve release.

[Back to top](#top)

---

<a id="specialization-validation-invariants"></a>

## Specialization validation invariants

### 1. Generic parent must close

The candidate must satisfy accepted generic Crossings checks before specialization can pass.

Fail when:

- generic crossing family is unresolved;
- spatial intersection is the only support;
- route, segment, crossing, Bridge, RiverCrossing, Ferry, and graph families collapse;
- generic parent result is missing, unknown, or error under a strict profile.

### 2. Transport-side scope must remain bounded

Pass only when the candidate describes the transport relationship and limitations.

Fail or deny when it claims:

- structural condition;
- inspection validity;
- load rating or clearance permission;
- legal access or right-of-way;
- current operational state;
- safety, passability, navigability, or emergency suitability;
- Hydrology condition;
- public release permission.

### 3. Carried and crossed roles must be explicit

Require semantic roles where applicable.

Fail when:

- one opaque reference is used for both roles;
- a route label substitutes for a segment/crossing relation;
- a water name is treated as a governed Hydrology object without a ref;
- a Bridge is treated as both structure, route, and graph edge in one untyped object;
- roles are guessed from coordinate ordering or UI labels.

### 4. Hydrology boundary must close

A RiverCrossing or water-related Bridge needs an owning Hydrology reference or an explicit justified unknown state.

Fail, hold, or abstain when:

- waterbody/reach identity is required but absent;
- water condition is copied into the transport record;
- flood, stage, depth, flow, fordability, or navigability is inferred from crossing existence;
- stale water context is presented as current;
- Hydrology source role or evidence is hidden;
- generalized public geometry could expose restricted Hydrology or adjacent sensitive detail.

### 5. Infrastructure boundary must close

A Bridge transport claim must not become full asset truth.

Fail or restrict when:

- asset identity is asserted without owning reference;
- structural condition, inspection, maintenance, vulnerability, load, clearance, or component detail appears without authorized scope;
- critical-infrastructure sensitivity is unresolved;
- public output exposes restricted asset detail;
- transport and asset identities are merged without a reviewed crosswalk.

### 6. Geometry is a carrier, not evidence

Geometry checks must distinguish shape, role, precision, and proof.

Fail when:

- geometric intersection alone proves a crossing;
- a point near a stream proves a ford or bridge;
- a graph edge proves source alignment;
- a generalized geometry is used as canonical exact geometry;
- map/screenshot/tile placement is treated as evidence;
- public geometry exceeds approved precision or enables reconstruction.

### 7. Source role must remain fixed

Observed, administrative, regulatory, modeled, aggregate, candidate, synthetic, historic, contextual, and restricted roles must remain visible.

Fail when:

- candidate or modeled crossing becomes observed;
- administrative inventory becomes current operational truth;
- historic narrative becomes modern access truth;
- aggregate route context becomes per-crossing fact;
- synthetic or generated interpretation becomes source evidence;
- role is upgraded by processing, graph projection, rendering, or release.

### 8. Time kinds must remain distinct

Preserve:

- source/publication time;
- observation/assertion time;
- validity/effective interval;
- retrieval/freeze time;
- status/restriction time;
- release time;
- correction/supersession time.

Fail when one timestamp silently stands in for all meanings.

### 9. Current status requires current authoritative support

A current bridge/crossing status request must have:

- authoritative source role and identity;
- current valid/effective interval;
- retrieval time;
- freshness/stale-state outcome;
- supersession/correction handling;
- official-source caveat/redirect;
- policy/release support for the requested surface.

Otherwise return stale, hold, deny, or abstain—not a current answer.

### 10. Status and restriction records remain separate

Bridge/RiverCrossing identity must not absorb:

- closure;
- detour;
- access restriction;
- load/height restriction;
- seasonal condition;
- operator status;
- incident or hazard event.

Use typed refs and time-scoped records.

### 11. Historic and modern claims must not collapse

Require explicit temporal scope, confidence, method, and limitations for historic crossings.

Fail when:

- historic crossing becomes current road access;
- reconstructed alignment becomes observed geometry;
- cultural route interpretation becomes legal route truth;
- uncertain historic location is rendered with false precision;
- archaeological/cultural sensitivity is unresolved.

### 12. Graph projection remains derived

Each projected node/edge must:

- be rebuildable;
- cite the underlying Bridge/RiverCrossing/Crossing evidence;
- preserve source role and sensitivity;
- record derivation identity/digest;
- become stale or invalid when source evidence changes;
- never become live routing or source geometry authority.

### 13. Evidence must close independently

Every consequential candidate and each owning-domain dependency must resolve appropriate EvidenceRefs/EvidenceBundles.

Fail or abstain when:

- a claim floats free of evidence;
- only the graph/map/UI is cited;
- one domain's evidence is used to prove another domain's fact;
- evidence was corrected/withdrawn without cascade;
- a generated summary is cited as source evidence.

### 14. Most-restrictive sensitivity and rights win

A join may become more sensitive than any visible input.

Fail closed when:

- critical-infrastructure detail is unresolved;
- culturally sensitive or archaeology-adjacent precision is exposed;
- private access or land detail is inferred;
- restricted source terms are not propagated;
- public tiles/search/graph/export/AI can reconstruct withheld detail;
- required transform/review/policy/release receipts are absent.

### 15. Policy must be external and explicit

A future validator consumes a PolicyDecision or finite policy result.

It must not:

- infer allow from missing policy;
- embed hidden allow lists;
- calculate legal access;
- weaken an owning domain's disposition;
- present a warning as an allow;
- treat policy engine failure as pass.

### 16. Release remains a separate governed state transition

A pass only says configured checks passed.

Public-bound use still requires:

- admitted source posture;
- accepted contracts/schemas where required;
- evidence closure;
- sensitivity/rights resolution;
- policy decision;
- review state;
- release manifest;
- correction path;
- rollback target;
- carrier-specific validation.

### 17. Public carriers remain downstream

Maps, tiles, API payloads, graph/search, exports, screenshots, Focus Mode, embeddings, and AI text must use released public-safe derivatives.

Deny direct exposure of:

- RAW/WORK/QUARANTINE/PROCESSED candidates;
- internal exact geometry;
- restricted bridge condition/vulnerability;
- unresolved access/closure/status;
- sensitive cultural/archaeological crossing detail;
- unreleased graph projections;
- unreviewed generated interpretations.

### 18. Corrections cascade

Corrections to:

- source identity or role;
- Bridge/RiverCrossing classification;
- carried/crossed refs;
- Hydrology or infrastructure refs;
- geometry/precision;
- status/restriction records;
- rights/sensitivity/policy;
- evidence;
- release;

must invalidate or revalidate dependent catalog, graph, tile, API, search, Focus Mode, export, and AI artifacts.

[Back to top](#top)

---

<a id="operational-safety-and-access-boundary"></a>

## Operational, safety, and access boundary

This specialization is **not** a source of operational advice.

### Always outside this validator's authority

- Is the bridge structurally safe?
- What is the current load rating or clearance?
- Is the ford passable?
- What is the current water depth, flow, stage, or flood condition?
- Is the route legally accessible?
- Is a private road open?
- Is the bridge or crossing currently closed?
- Is ferry service operating?
- Is this an approved emergency route?
- Is passage safe for a vehicle, pedestrian, train, boat, livestock, or equipment?
- Does a map line establish right-of-way?
- Does a historical crossing authorize modern access?

### Required response posture

| Request type | Validator posture |
|---|---|
| Semantic contract validation | Evaluate only declared shape/refs/invariants. |
| Historical/contextual explanation | Allow bounded evidence-linked context with temporal caveats and sensitivity controls. |
| Current status | Require authoritative current source, freshness, policy, release, and official redirect; otherwise abstain/deny. |
| Engineering/safety decision | Deny as outside authority. |
| Legal access/right-of-way | Abstain or deny unless an accepted legal-authority path exists; this validator cannot decide. |
| Emergency routing | Deny as outside authority. |
| Public carrier output | Require released public-safe derivative and visible limitations. |

The README contains no operational conditions and should never be cited as one.

[Back to top](#top)

---

<a id="sensitivity-rights-and-public-surface-boundary"></a>

## Sensitivity, rights, and public-surface boundary

### Reachable sensitive classes

- bridge/crossing condition or vulnerability;
- critical freight or transport infrastructure;
- exact coordinates that enable harm;
- restricted-source-derived fields;
- Indigenous/cultural mobility corridors;
- archaeological/cultural site adjacency;
- private access or land context;
- hazard/emergency status;
- reverse-engineerable graph, tile, search, or generated outputs.

### Output-level review

The validator must evaluate the **produced output**, not merely the input labels.

A public-looking input can yield a restricted output when joined with:

- sensitive infrastructure;
- archaeology/cultural context;
- private access information;
- Hydrology/hazard current-condition detail;
- restricted source metadata;
- exact geometry or topology;
- multiple generalized layers that reconstruct exact location.

### Most-restrictive propagation

The strongest applicable disposition must travel through:

- joins;
- derived graph edges;
- generalized geometry;
- tiles and caches;
- screenshots;
- search indexes;
- exports;
- embeddings;
- Focus Mode;
- AI answers;
- correction and rollback operations.

### Safe diagnostics

Findings may expose:

- candidate id;
- object family;
- safe dependency ids;
- finite outcome;
- reason code;
- field path;
- safe time category;
- missing-ref type;
- release/policy/review state.

Findings must not expose:

- restricted coordinates;
- vulnerability/condition detail;
- private access notes;
- cultural/archaeological exact locations;
- hidden generalization thresholds;
- secrets or private endpoints;
- restricted source payloads.

[Back to top](#top)

---

<a id="validation-report-contract"></a>

## Validation report contract

A future report should be deterministic, bounded, machine-readable, and safe. This is **PROPOSED**.

```yaml
report_id: <stable-id>
validator:
  id: bridge-river-crossing
  version: <semver>
  profile_digest: <hash>
run:
  validation_instant: <RFC3339>
  no_network: true
  input_digest: <hash>
  dependency_order: []
candidate:
  id: <candidate-id>
  object_family: <Bridge|RiverCrossing>
  lifecycle_state: <state>
request:
  operation: validate
  surface: <surface>
  audience: <audience>
outcome: <PASS|FAIL|DENY|HOLD|REVIEW_REQUIRED|ABSTAIN|ERROR>
findings:
  - code: <finite-reason-code>
    severity: <info|warning|error|critical>
    disposition: <fail|deny|hold|review|abstain>
    object_ref: <safe-ref|null>
    field_path: <safe-json-pointer|null>
    dependency: <validator-id|null>
    message: <bounded-safe-text>
dependencies:
  - validator_id: <id>
    outcome: <finite-outcome>
    report_ref: <safe-ref|null>
obligations:
  evidence_refs: []
  policy_decision_ref: <ref|null>
  review_refs: []
  receipt_refs: []
  release_manifest_ref: <ref|null>
  correction_ref: <ref|null>
  rollback_ref: <ref|null>
integrity:
  report_digest: <hash>
  implementation_digest: <hash>
  fixture_digest: <hash|null>
```

### Report invariants

- Stable sorting of findings.
- Stable reason-code vocabulary.
- No timestamps generated implicitly.
- No network-dependent content.
- No secret or restricted payload echo.
- Dependency results preserved.
- Unknown/error not coerced to pass.
- Report destination separated from source code.
- Report does not mutate candidate or release state.
- Report pass is not evidence, policy, review, or publication approval.

[Back to top](#top)

---

<a id="finite-outcomes-and-reason-codes"></a>

## Finite outcomes and reason codes

### Parent outcomes

| Outcome | Meaning |
|---|---|
| `PASS` | All required configured checks passed for the declared scope. |
| `FAIL` | One or more deterministic conformance checks failed. |
| `DENY` | Requested use is prohibited by authority, sensitivity, safety, rights, policy, or public-surface boundary. |
| `HOLD` | Candidate must remain internal/quarantined pending missing support. |
| `REVIEW_REQUIRED` | Named steward/security/cultural/infrastructure review is required. |
| `ABSTAIN` | Available evidence or authority is insufficient to decide safely. |
| `ERROR` | Validator could not complete safely. |

### Proposed reason-code families

Use the prefix `BRC_` for specialization-local findings.

#### Topology and dependency

- `BRC_GENERIC_CROSSINGS_RESULT_MISSING`
- `BRC_GENERIC_CROSSINGS_FAILED`
- `BRC_DOMAIN_RESULT_MISSING`
- `BRC_TOPOLOGY_RESULT_MISSING`
- `BRC_DEPENDENCY_ERROR`
- `BRC_DEPENDENCY_OUTCOME_UNKNOWN`
- `BRC_PROFILE_UNKNOWN`
- `BRC_PROFILE_DIGEST_MISMATCH`

#### Object family and identity

- `BRC_OBJECT_FAMILY_UNSUPPORTED`
- `BRC_SPECIALIZATION_AMBIGUOUS`
- `BRC_GENERIC_CROSSING_REF_MISSING`
- `BRC_CARRIED_OBJECT_REF_MISSING`
- `BRC_CROSSED_OBJECT_REF_MISSING`
- `BRC_CARRIED_CROSSED_ROLE_COLLAPSE`
- `BRC_ROUTE_SEGMENT_CROSSING_COLLAPSE`
- `BRC_BRIDGE_ASSET_IDENTITY_COLLAPSE`
- `BRC_FERRY_BRIDGE_RIVER_CROSSING_COLLAPSE`
- `BRC_IDENTITY_UNSTABLE`

#### Hydrology and infrastructure

- `BRC_HYDROLOGY_REF_MISSING`
- `BRC_HYDROLOGY_REF_UNRESOLVED`
- `BRC_HYDROLOGY_TRUTH_ABSORBED`
- `BRC_WATER_CONDITION_UNSUPPORTED`
- `BRC_INFRASTRUCTURE_REF_MISSING`
- `BRC_INFRASTRUCTURE_REF_UNRESOLVED`
- `BRC_STRUCTURAL_TRUTH_ABSORBED`
- `BRC_CRITICAL_INFRASTRUCTURE_REVIEW_REQUIRED`

#### Geometry and graph

- `BRC_SPATIAL_INTERSECTION_NOT_EVIDENCE`
- `BRC_GEOMETRY_ROLE_MISSING`
- `BRC_GEOMETRY_PRECISION_UNSAFE`
- `BRC_PROXIMITY_INFERENCE_UNSUPPORTED`
- `BRC_GRAPH_AUTHORITY_COLLAPSE`
- `BRC_GRAPH_EVIDENCE_REF_MISSING`
- `BRC_GRAPH_DERIVATION_MISSING`
- `BRC_GRAPH_STALE_AFTER_CORRECTION`

#### Source role, knowledge character, and time

- `BRC_SOURCE_DESCRIPTOR_MISSING`
- `BRC_SOURCE_ROLE_MISSING`
- `BRC_SOURCE_ROLE_COLLAPSE`
- `BRC_KNOWLEDGE_CHARACTER_MISSING`
- `BRC_CANDIDATE_AS_CONFIRMED`
- `BRC_MODELED_AS_OBSERVED`
- `BRC_HISTORIC_AS_CURRENT`
- `BRC_SYNTHETIC_AS_EVIDENCE`
- `BRC_TIME_KIND_COLLAPSE`
- `BRC_VALID_TIME_MISSING`
- `BRC_CURRENT_STATUS_STALE`
- `BRC_STATUS_SOURCE_NOT_AUTHORITATIVE`
- `BRC_SUPERSESSION_UNRESOLVED`

#### Safety, access, and operational authority

- `BRC_STRUCTURAL_SAFETY_DENIED`
- `BRC_LOAD_CLEARANCE_ADVICE_DENIED`
- `BRC_FORDABILITY_DENIED`
- `BRC_NAVIGATION_ADVICE_DENIED`
- `BRC_LEGAL_ACCESS_DENIED`
- `BRC_RIGHT_OF_WAY_UNSUPPORTED`
- `BRC_LIVE_CLOSURE_UNSUPPORTED`
- `BRC_FERRY_OPERATION_UNSUPPORTED`
- `BRC_EMERGENCY_ROUTING_DENIED`
- `BRC_SAFE_PASSAGE_DENIED`

#### Evidence, rights, sensitivity, policy, and release

- `BRC_EVIDENCE_REF_MISSING`
- `BRC_EVIDENCE_UNRESOLVED`
- `BRC_EVIDENCE_CORRECTED_OR_WITHDRAWN`
- `BRC_RIGHTS_UNKNOWN`
- `BRC_RESTRICTED_SOURCE_LEAK`
- `BRC_SENSITIVITY_UNKNOWN`
- `BRC_MOST_RESTRICTIVE_POLICY_NOT_PROPAGATED`
- `BRC_CULTURAL_REVIEW_REQUIRED`
- `BRC_ARCHAEOLOGY_DETAIL_DENIED`
- `BRC_PRIVATE_ACCESS_DETAIL_DENIED`
- `BRC_TRANSFORM_RECEIPT_MISSING`
- `BRC_POLICY_DECISION_MISSING`
- `BRC_POLICY_DENY`
- `BRC_REVIEW_RECORD_MISSING`
- `BRC_RELEASE_REFERENCE_MISSING`
- `BRC_PUBLIC_DERIVATIVE_NOT_APPROVED`
- `BRC_CORRECTION_PATH_MISSING`
- `BRC_ROLLBACK_TARGET_MISSING`
- `BRC_LIFECYCLE_VIOLATION`
- `BRC_PUBLIC_SURFACE_VIOLATION`

#### Security and execution

- `BRC_NETWORK_ACCESS_DENIED`
- `BRC_UNTRUSTED_CONTENT_INSTRUCTION_IGNORED`
- `BRC_PATH_ESCAPE_DENIED`
- `BRC_REFERENCE_CYCLE`
- `BRC_RESOURCE_LIMIT_EXCEEDED`
- `BRC_REPORT_SENSITIVE_DETAIL_DENIED`
- `BRC_NONDETERMINISTIC_RESULT`
- `BRC_INTERNAL_ERROR`

Reason codes describe validator findings. They do not define policy or domain truth.

[Back to top](#top)

---

<a id="contract-schema-policy-source-and-test-maturity"></a>

## Contract, schema, policy, source, and test maturity

### Contracts

| Surface | Status | Safe interpretation |
|---|---|---|
| Bridge contract | Draft v0.2; transport-side claim; schema missing. | Meaning guidance exists; machine enforcement does not. |
| River Crossing contract | Draft v0.2; transport-side water-crossing claim; schema missing. | Meaning guidance exists; water/safety/access authority explicitly denied. |
| Generic Crossing contract | Draft; parent semantics. | Parent relationship exists; exact runtime behavior unverified. |
| Ferry/status/restriction/network contracts | Present in contract lane or referenced. | Need file-by-file contract/schema pairing before enforcement. |

### Schemas

| Surface | Status | Consequence |
|---|---|---|
| `schemas/contracts/v1/domains/roads-rail-trade/` | Draft index, slug-conflicted, no concrete schema confirmed in checked inventory. | No bridge/river machine shape may be claimed active. |
| `schemas/contracts/v1/crossings/` | Compatibility/index-only, canonical unresolved. | Must not become a parallel schema authority. |
| `bridge.schema.json` | Contract reports missing. | Fields remain semantic proposals. |
| `river_crossing.schema.json` | Contract reports missing. | Fields remain semantic proposals. |
| ValidationReport/profile schemas | Not established for this specialization. | Proposed report/profile cannot be treated as contract. |

### Policy

`policy/domains/roads-rail-trade/README.md` is a greenfield scaffold. Therefore:

- no executable policy entrypoint is claimed;
- no stable input/output vocabulary is claimed;
- no policy-bundle digest is available;
- no allow/deny parity is proven;
- no local validator fallback may be treated as policy.

### Sources

A Roads/Rail/Trade source registry README exists, but:

- registry topology is conflicted between subtype-first and domain-first lanes;
- descriptor instances were not inventoried here;
- active source roles, rights, cadence, status authority, and crossing claims remain unverified;
- registry presence does not prove bridge/crossing truth or current conditions.

### Tests

- The domain test tree has contract/evidence/policy/release README families.
- Executable test files, fixture payloads, collected cases, pass rates, and CI significance remain unverified.
- `tests/validators/` is a README-only direct lane while shared runtime exists elsewhere.
- No dedicated Bridge/RiverCrossing suite surfaced.

### CI

The domain workflow runs only TODO echo steps. A green workflow therefore does not establish substantive Bridge/RiverCrossing validation.

[Back to top](#top)

---

<a id="security-untrusted-content-and-resource-limits"></a>

## Security, untrusted content, and resource limits

### No-network default

The validator must not fetch:

- live road/rail feeds;
- bridge databases;
- current closure systems;
- Hydrology APIs;
- map tiles;
- geocoders;
- external schema refs;
- private services;
- emergency/status sources.

Tests use pinned local fixtures and local references.

### Untrusted source content

Names, descriptions, OCR, historic text, status notes, metadata, URLs, and generated summaries are data—not instructions.

The validator must ignore embedded text that asks it to:

- change validation policy;
- suppress findings;
- reveal secrets;
- fetch a URL;
- execute code;
- reinterpret a role;
- approve public release;
- claim safe passage or current status.

### Reference safety

A future implementation must defend against:

- path traversal;
- symlink escape;
- recursive reference cycles;
- oversized geometry;
- excessive coordinate counts;
- deeply nested JSON/YAML;
- decompression bombs;
- unbounded evidence refs;
- report amplification;
- malicious Unicode/control characters;
- secret leakage in exceptions.

### Proposed resource controls

Profiles should pin:

- maximum input bytes;
- maximum object refs;
- maximum geometry vertices;
- maximum dependency depth;
- maximum findings;
- maximum message length;
- maximum reference resolution count;
- timeout;
- memory ceiling;
- no-network state.

Exact thresholds require security and implementation review and do not belong in this README as hidden operational policy.

[Back to top](#top)

---

<a id="lifecycle-release-correction-and-rollback"></a>

## Lifecycle, release, correction, and rollback

### Lifecycle invariant

```text
RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED
```

Validators inspect eligibility; they do not promote or move records.

### Stage posture

| Stage | Bridge/RiverCrossing posture |
|---|---|
| RAW | Preserve source payload and source identity; no public path. |
| WORK | Parse/normalize candidates; keep uncertainty and role. |
| QUARANTINE | Hold unresolved family, identity, Hydrology/infrastructure refs, rights, sensitivity, evidence, time, access, status, geometry, or policy. |
| PROCESSED | Produce role-preserving normalized candidates; still not public. |
| CATALOG | Close evidence and references; create reviewable catalog identity. |
| TRIPLET | Derive graph/topology projection with lineage; never canonical truth. |
| PUBLISHED | Serve only reviewed, policy-approved, released public-safe derivative through governed interfaces. |

### Release readiness

A validator may report release readiness only if the selected profile requires and resolves:

- source admission;
- contracts/schemas;
- identity;
- source role;
- time/freshness;
- evidence;
- rights/sensitivity;
- policy;
- review;
- transform receipts;
- release manifest;
- correction and rollback.

It still cannot approve the release.

### Correction cascade

Corrections may require:

1. mark source/candidate/report stale;
2. invalidate affected Bridge/RiverCrossing/Crossing catalog records;
3. rebuild graph/topology projections;
4. invalidate map/tile/search/export/Focus/AI carriers;
5. emit CorrectionNotice/WithdrawalNotice under accepted roots;
6. route affected release through review;
7. repoint to a prior safe release or deny exposure.

### Rollback principle

Rollback targets a known prior safe version. It must not restore an unsafe output solely because an older validator accepted it.

[Back to top](#top)

---

<a id="tests-fixtures-and-no-network-posture"></a>

## Tests, fixtures, and no-network posture

### Proposed test home

```text
tests/validators/bridge_river_crossing/
├── README.md
├── conftest.py
├── test_profile.py
├── test_delegation.py
├── test_object_families.py
├── test_carried_crossed_roles.py
├── test_hydrology_boundary.py
├── test_infrastructure_boundary.py
├── test_geometry_not_evidence.py
├── test_source_role_and_time.py
├── test_status_and_safety_denials.py
├── test_graph_derivation.py
├── test_sensitivity_and_public_carriers.py
├── test_correction_and_rollback.py
├── test_security.py
└── test_determinism.py
```

This layout is **PROPOSED**. Do not create it until test placement and fixture homes are accepted.

### Fixture posture

Reusable fixtures should live in accepted fixture roots. Test-local wrappers may live with tests if they do not become a parallel canonical fixture family.

Fixtures must be:

- synthetic;
- public-safe;
- deterministic;
- no-network;
- small;
- clearly labeled valid/invalid;
- free of real restricted infrastructure, private access, cultural/archaeological, or operational data;
- linked to expected finite outcomes and reason codes.

### Required positive controls

- transport-side Bridge with generic crossing ref, carried/crossed refs, evidence, and no structural claims;
- RiverCrossing with Hydrology ref, explicit transport role, historical/current distinction, and limitations;
- historic crossing with uncertainty, generalized public geometry, review, and no modern-access claim;
- derived graph edge that cites released catalog evidence and remains derivative;
- released public-safe summary with policy/review/release/correction/rollback refs.

### Required negative controls

- spatial line/polygon intersection treated as confirmed crossing;
- Bridge candidate claiming structural safety;
- RiverCrossing candidate claiming fordability or current water condition;
- missing Hydrology ref where water identity is material;
- missing infrastructure ref where asset identity is asserted;
- carried/crossed role collapse;
- Ferry/Bridge/RiverCrossing family collapse;
- historic crossing treated as modern legal access;
- graph edge treated as source evidence;
- stale closure/status treated as current;
- private-access or right-of-way claim without authority;
- critical-infrastructure vulnerability leaked publicly;
- archaeology/cultural exact location exposed;
- source-role or time-kind collapse;
- unresolved EvidenceRef;
- policy unavailable/error treated as pass;
- unreleased candidate sent to map/API/AI;
- correction not propagated;
- source content attempting prompt/config injection;
- fixture family empty but suite passes;
- nondeterministic finding order.

### Determinism pins

Tests should pin:

- validator/profile version and digest;
- dependency versions/order;
- contracts/schemas;
- fixture digests;
- policy bundle version;
- validation instant;
- timezone;
- reason-code registry;
- sort order;
- no-network state;
- locale and serialization.

[Back to top](#top)

---

<a id="ci-admission-contract"></a>

## CI admission contract

### Current evidence

`.github/workflows/domain-roads-rail-trade.yml` currently checks out the repository and runs TODO echo commands for validation, proof building, and publish dry-run. Its existence or green status does not prove substantive specialization coverage.

Shared schema/validator workflows may exercise other validators, but no Bridge/RiverCrossing registration surfaced.

### Proposed blocking stages

A future CI path should include:

1. README/link checks;
2. profile and dependency-manifest parse;
3. contract/schema path checks;
4. validator import and `--help` smoke test;
5. generic Crossings parent delegation;
6. positive synthetic fixtures;
7. negative object-family and geometry-not-evidence fixtures;
8. Hydrology/infrastructure boundary fixtures;
9. source-role/time/current-status fixtures;
10. safety/access/operational denial fixtures;
11. sensitivity and public-carrier leakage fixtures;
12. graph derivation and correction invalidation;
13. no-network enforcement;
14. policy unavailable/error behavior;
15. report schema and safe-diagnostic validation;
16. deterministic rerun comparison;
17. report/receipt destination validation;
18. coverage-manifest check proving this entrypoint is collected.

### CI must fail when

- the specialization bypasses generic Crossings checks;
- multiple active entrypoints claim the same specialization;
- expected contract/schema/profile refs do not resolve;
- required fixture families are empty;
- a negative fixture passes;
- a valid fixture fails;
- an unknown/error is converted to pass;
- current/safety/access claims escape required denials;
- sensitive detail appears in output;
- findings are nondeterministic;
- network access occurs;
- the specialization is absent from its accepted manifest/aggregate;
- TODO-only jobs are presented as substantive coverage.

### Artifact posture

A future CI report should record:

- commit;
- profile and implementation digests;
- dependency manifest;
- fixture counts/digests;
- outcomes/reason counts;
- no-network proof;
- deterministic comparison;
- test command;
- environment summary;
- artifact retention and access policy.

[Back to top](#top)

---

<a id="smallest-sound-implementation-sequence"></a>

## Smallest sound implementation sequence

Use small, reviewable, reversible pull requests.

### PR 1 — topology and authority decision

- accept `crossings/` as generic parent and this lane as specialization;
- accept one executable/registry identity;
- resolve owner and CODEOWNERS;
- record dependency manifest;
- document rollback.

### PR 2 — contract/schema pairing

- disposition `roads-rail-trade` versus `transport` slug/path conflict;
- disposition `schemas/contracts/v1/crossings/` compatibility lane;
- add or accept Bridge and RiverCrossing schemas;
- add stable ids, required fields, and bounded extensibility;
- add valid/invalid schema fixtures;
- add migration notes for aliases.

### PR 3 — source, time, and policy profiles

- accept SourceDescriptor/source-role vocabulary;
- define Bridge/RiverCrossing claim-authority profiles;
- define time kinds and freshness/current-status behavior;
- define Hydrology/infrastructure dependency requirements;
- define policy entrypoints and fail-closed errors;
- define sensitivity and rights review roles.

### PR 4 — child validators and shared dependencies

- implement or reuse generic Crossings checks;
- implement geometry-not-evidence and carried/crossed-role checks;
- integrate topology, freshness, evidence, sensitivity, policy, and release dependencies;
- ensure no duplicate source-role/time/geometry logic.

### PR 5 — thin specialization and report

- implement one narrow orchestrator;
- emit deterministic structured report;
- use finite outcomes and reason codes;
- enforce safe diagnostics and resource budgets;
- write artifacts only to accepted roots.

### PR 6 — tests, CI, correction, and rollout

- add public-safe no-network positive/negative fixtures;
- add security/determinism tests;
- wire collection/coverage manifest;
- add correction/withdrawal/rollback cases;
- run non-blocking adoption;
- review findings and false positives;
- adopt as release gate only through separate governance review.

Each PR must include validation and rollback. None may silently create operational or public authority.

[Back to top](#top)

---

<a id="definition-of-done"></a>

## Definition of done

The specialization is not implementation-complete until all required items are verified.

### Placement and ownership

- [ ] `crossings/` is accepted as generic parent.
- [ ] `bridge_river_crossing/` is accepted as narrow child.
- [ ] One canonical executable, registry id, profile family, and report family exist.
- [ ] Owners and CODEOWNERS are assigned.
- [ ] Shared geometry, freshness, evidence, policy, release, and topology responsibilities are non-overlapping.
- [ ] Contract/schema/source-registry path drift is dispositioned.

### Contracts and schemas

- [ ] Bridge and RiverCrossing semantic contracts are accepted.
- [ ] Paired schemas exist at accepted homes.
- [ ] Generic Crossing relationship is explicit.
- [ ] Carried/crossed/Hydrology/infrastructure/status/restriction refs are modeled.
- [ ] Stable ids and digests are defined.
- [ ] ValidationReport/profile schemas are accepted.
- [ ] Compatibility paths have migration/deprecation notes.

### Sources, rights, policy, and evidence

- [ ] Active source descriptor profiles are identified.
- [ ] Source role and authority limits are tested.
- [ ] Current-status authority and freshness rules are explicit.
- [ ] Rights/sensitivity profiles are accepted.
- [ ] Policy entrypoints, defaults, obligations, and errors are tested.
- [ ] EvidenceRef/EvidenceBundle resolution is deterministic.
- [ ] Infrastructure/Hydrology/cultural review requirements are explicit.

### Tests and CI

- [ ] Positive and negative fixtures exist.
- [ ] Fixture families are nonempty.
- [ ] No-network behavior is enforced.
- [ ] Geometry-not-evidence cases fail correctly.
- [ ] Safety/access/current-status cases fail correctly.
- [ ] Sensitive output cannot leak through carriers or diagnostics.
- [ ] Correction/rollback cases invalidate derivatives.
- [ ] Deterministic reruns match.
- [ ] CI actually collects the specialization and is required where intended.
- [ ] Current results are recorded with commit/profile digests.

### Operations and governance

- [ ] Reports/receipts write to accepted roots.
- [ ] Metrics exclude sensitive payloads.
- [ ] Incident and correction owners are assigned.
- [ ] Release-gate adoption is separately reviewed.
- [ ] Public interfaces consume released derivatives only.
- [ ] Rollback and withdrawal are rehearsed.
- [ ] No operational, legal, safety, navigation, or emergency authority is implied.

[Back to top](#top)

---

<a id="migration-compatibility-and-deprecation"></a>

## Migration, compatibility, and deprecation

### Current documented topology

```text
tools/validators/crossings/                 # generic parent
tools/validators/bridge_river_crossing/     # Bridge/RiverCrossing specialization
tools/validators/domains/roads-rail-trade/  # domain parent/index
tools/validators/transport-facility-topology/ # adjacent facility/topology checks
```

### Current path drift

The repository records unresolved drift involving:

- `roads-rail-trade` versus `transport` contract/schema segments;
- domain-specific versus flat schema paths;
- `schemas/contracts/v1/crossings/` compatibility family versus Roads/Rail/Trade domain schemas;
- domain-first versus subtype-first Roads/Rail/Trade source registry topology;
- old README statements that predate newer parent/index files.

This README records drift; it does not decide it.

### One-active-implementation rule

At any time there should be:

- one generic Crossings parent implementation;
- one Bridge/RiverCrossing specialization implementation;
- one stable CLI/package entrypoint per role;
- one dependency manifest;
- one profile identity;
- one report schema;
- compatibility paths that delegate or redirect, never fork behavior.

### Migration requirements

Any rename, move, merge, or package extraction must include:

- accepted owner/root decision;
- ADR or migration note where authority/compatibility changes;
- consumer/import/workflow/registry inventory;
- atomic code/test/fixture/config updates;
- compatibility adapter where required;
- deprecation window;
- receipt/report compatibility;
- rollback to prior entrypoint/path;
- no period with two divergent active implementations.

### Deprecation requirements

A deprecated path must state:

- successor;
- date/status;
- accepted consumers;
- removal condition;
- report/receipt compatibility;
- rollback;
- migration owner.

[Back to top](#top)

---

<a id="open-verification-register"></a>

## Open verification register

| ID | Question | Status | Required evidence |
|---|---|---|---|
| BRC-001 | Is `crossings/` formally accepted as the generic parent? | NEEDS VERIFICATION | Steward/ADR/registry decision. |
| BRC-002 | Is this exact directory the accepted specialization home? | NEEDS VERIFICATION | Directory/validator topology decision. |
| BRC-003 | What is the canonical executable/package/CLI identity? | UNKNOWN | Implementation and registry manifest. |
| BRC-004 | What is the complete consumer/import/workflow inventory? | UNKNOWN | Code/workflow/runtime search. |
| BRC-005 | Which Bridge contract version is accepted? | NEEDS VERIFICATION | Contract review and registry. |
| BRC-006 | Which RiverCrossing contract version is accepted? | NEEDS VERIFICATION | Contract review and registry. |
| BRC-007 | Where is the canonical Bridge schema? | NEEDS VERIFICATION | Schema-home decision and file. |
| BRC-008 | Where is the canonical RiverCrossing schema? | NEEDS VERIFICATION | Schema-home decision and file. |
| BRC-009 | Should `schemas/contracts/v1/crossings/` remain index-only? | NEEDS VERIFICATION | ADR/migration/schema registry. |
| BRC-010 | How is `roads-rail-trade` versus `transport` slug drift resolved? | NEEDS VERIFICATION | ADR and migration plan. |
| BRC-011 | What source-role vocabulary is authoritative? | NEEDS VERIFICATION | Accepted source schema/ADR. |
| BRC-012 | Which source descriptors can support Bridge claims? | UNKNOWN | Source registry inventory and rights review. |
| BRC-013 | Which source descriptors can support RiverCrossing claims? | UNKNOWN | Source registry inventory and rights review. |
| BRC-014 | Which sources may support current closure/status claims? | NEEDS VERIFICATION | Authority/cadence/freshness profiles. |
| BRC-015 | What time fields are required per object family? | NEEDS VERIFICATION | Contract/schema/time-profile review. |
| BRC-016 | What stale thresholds apply per source/product? | NEEDS VERIFICATION | Freshness policy/profile. |
| BRC-017 | How are carried and crossed object roles encoded? | NEEDS VERIFICATION | Accepted schema and fixtures. |
| BRC-018 | When is a generic Crossing ref mandatory? | NEEDS VERIFICATION | Contract/schema decision. |
| BRC-019 | Which Hydrology object refs are accepted? | NEEDS VERIFICATION | Hydrology contract/schema registry. |
| BRC-020 | Which infrastructure asset refs are accepted? | NEEDS VERIFICATION | Settlements/Infrastructure contracts/registry. |
| BRC-021 | How are bridge transport identity and asset identity crosswalked? | NEEDS VERIFICATION | Crosswalk contract and tests. |
| BRC-022 | What geometry roles and precision profiles are accepted? | NEEDS VERIFICATION | Geometry contract/policy/fixtures. |
| BRC-023 | How is spatial intersection evidence represented? | NEEDS VERIFICATION | Evidence/derivation contract. |
| BRC-024 | How are historic crossings represented without false precision? | NEEDS VERIFICATION | Historic-route contract/policy/fixtures. |
| BRC-025 | Which cultural/archaeology reviews are required? | NEEDS VERIFICATION | Sensitivity policy and CODEOWNERS. |
| BRC-026 | Which critical-infrastructure review is required? | NEEDS VERIFICATION | Security/sensitivity policy. |
| BRC-027 | How are private access and legal status excluded or represented? | NEEDS VERIFICATION | Policy/contract/legal-authority design. |
| BRC-028 | What policy bundle evaluates this specialization? | UNKNOWN | Bundle manifest, entrypoint, tests. |
| BRC-029 | What finite policy outcomes/obligations are authoritative? | NEEDS VERIFICATION | Policy contract/schema. |
| BRC-030 | What EvidenceBundle admission result is consumed? | UNKNOWN | Evidence resolver contract and fixtures. |
| BRC-031 | What is the accepted specialization report schema? | PROPOSED | Contract/schema/fixtures. |
| BRC-032 | Where do reports and validation receipts live? | NEEDS VERIFICATION | Artifact/receipt layout decision. |
| BRC-033 | Is the specialization registered in shared validator aggregate? | NOT CONFIRMED | Aggregate/manifest implementation. |
| BRC-034 | What is the dedicated test home? | NEEDS VERIFICATION | Test topology decision. |
| BRC-035 | Which valid/invalid fixture families exist? | UNKNOWN | Fixture inventory. |
| BRC-036 | Are fixture nonempty checks enforced? | UNKNOWN | Test implementation. |
| BRC-037 | Is no-network enforced for this specialization? | UNKNOWN | Test/CI evidence. |
| BRC-038 | What resource budgets apply? | NEEDS VERIFICATION | Security/implementation profile. |
| BRC-039 | How are graph derivatives identified and invalidated? | NEEDS VERIFICATION | Graph contract/pipeline/tests. |
| BRC-040 | How are source corrections propagated? | UNKNOWN | Dependency/correction workflow. |
| BRC-041 | How are Hydrology/infrastructure corrections propagated? | UNKNOWN | Cross-domain dependency graph/tests. |
| BRC-042 | Which public carriers require separate leakage validation? | NEEDS VERIFICATION | Surface inventory and policy matrix. |
| BRC-043 | Is this specialization used by map/API/Focus/AI/release gates? | UNKNOWN | Runtime/workflow/log evidence. |
| BRC-044 | Are domain workflows intended to become blocking? | NEEDS VERIFICATION | Workflow policy/branch protection. |
| BRC-045 | What artifact retention/access rules apply? | NEEDS VERIFICATION | CI/security policy. |
| BRC-046 | What compatibility/deprecation window applies? | NEEDS VERIFICATION | Consumer inventory/migration plan. |
| BRC-047 | What are current pass/fail results? | UNKNOWN | Executable and pinned test run. |
| BRC-048 | What operational metrics/incidents exist? | UNKNOWN | Dashboards/logs/incident records. |
| BRC-049 | Who owns security, cultural, infrastructure, and release review? | NEEDS VERIFICATION | CODEOWNERS/governance assignments. |
| BRC-050 | Has rollback been rehearsed? | UNKNOWN | Drill evidence. |

[Back to top](#top)

---

<a id="rollback-path"></a>

## Rollback path

### Documentation-only rollback

For this revision:

1. revert the README commit;
2. restore prior blob `3e564b643394c3e84716222a9e2e90e8d245f2cd`;
3. revert or supersede the paired generated receipt;
4. confirm parent/index links still resolve;
5. confirm no stale PR/registry pointer claims v0.2 as accepted implementation.

No runtime, source, schema, policy, evidence, graph, lifecycle, deployment, or release rollback is required because this revision changes documentation only.

### Future implementation rollback

A future rollout must define:

- previous executable/profile/dependency manifest;
- previous contract/schema baseline;
- previous policy bundle;
- feature flag or gate-disable mechanism;
- report/receipt compatibility;
- affected catalog/graph/public carriers;
- correction/withdrawal steps;
- consumer migration window;
- incident owner;
- safe fallback behavior.

Rollback must fail closed. It must not restore unsafe access, status, condition, crossing, or routing claims merely because a prior version accepted them.

[Back to top](#top)

---

<a id="evidence-ledger"></a>

## Evidence ledger

| Evidence | Blob | What it supports |
|---|---|---|
| Prior target README | `3e564b643394c3e84716222a9e2e90e8d245f2cd` | v0.1 scope and prior proposed outcomes. |
| Bridge contract | `2d00036dcd47c5fac7ee43679ada4682ee654776` | Transport-side bridge meaning; schema missing; structural/live/access denial. |
| River Crossing contract | `1f9779a6aeb08110c77ef0b5a3ecff19fd602bda` | Transport-side river/ford claim; Hydrology/safety/access boundary; schema missing. |
| Generic Crossings parent | `7807275a0afca4aa1518787a392225e2732a6757` | Parent-child topology and generic crossing invariants. |
| Roads/Rail/Trade validator index | `1d5942ab5499cd752974aee804372d89e3c315c0` | Domain-wide routing, object families, slug drift, authority denials. |
| Transport facility topology lane | `35773f93f2d3a4684e4419719e9e79b724cb06fa` | Facility/graph identity, cross-domain and critical-transport topology boundaries. |
| Graph projections doctrine | `4031c319e0eb1dc8a79e2ca5953311cc37c08115` | Graph is derived, evidence-linked, rebuildable, not canonical truth. |
| Domain schema index | `91cd62a640d5a91270564727ff3704a8c236b012` | No concrete schema confirmed; candidate Bridge/RiverCrossing schemas; slug conflict. |
| Crossings schema compatibility index | `cf4ef35500c71060065e80b8ce7ae0aac2dc9665` | Crossings path index-only and canonical unresolved. |
| Domain policy README | `508062700bc3f56fb05914290fc160d7634b53f4` | Greenfield policy maturity. |
| Domain tests README | `3c362bf18f228e5b23a533eb4fc0214ca80a614a` | Documentation-led no-network test posture and unverified execution. |
| Domain workflow | `c6f547b0acd8018284001ed67d25b153c0d9992b` | TODO-only validation/proof/publish jobs. |
| Source registry README | `54087e02e329b98c595807e4c9041c97972c0179` | Source-role/current-status/rights boundaries and registry topology drift. |
| Sensitivity doctrine | `59870cd850b6491488578a296294691e8c9c50eb` | Critical infrastructure, cultural/archaeology, exact-harm, rights, most-restrictive posture. |
| Validator root | `e35742288404a1eeb214f8269fbacb1429c0f86a` | Validators check and fail closed; they are not truth/policy/release authority. |
| Validator tests parent | `c703a64eef3f69044a54696f121f4e5ae05a3631` | Shared runtime exists; direct tests lane README-only; aggregate coverage partial. |
| Directory Rules | `2affb080e6f0043867c64c7f06c1ca52030fbd55` | Responsibility-root placement, lifecycle, and parallel-home discipline. |
| Generated receipt schema | `fba21ed27ebccf1362fe397fe0c3ebd85e072685` | Required provenance receipt shape. |

### Evidence limitations

- Repository search is bounded.
- README presence does not prove executable behavior.
- Contract presence does not prove accepted schema or runtime conformance.
- Workflow presence does not prove substantive checks.
- Schema indexes do not prove concrete schemas.
- No live source, runtime, deployment, dashboard, branch-protection, or current-condition evidence was used.
- No claim is made about actual bridge condition, crossing access, water condition, current closure, ferry operation, or public release.

[Back to top](#top)

---

<a id="changelog"></a>

## Changelog

### v0.2 — 2026-07-16

- grounded the specialization in current repository evidence;
- classified the direct lane as README-only and enforcement as unestablished;
- established `crossings/` as the documented generic parent and this lane as a narrow child;
- mapped domain, Hydrology, infrastructure, hazards, archaeology/cultural, people/land, graph, geometry, evidence, policy, and release boundaries;
- recorded draft contracts, missing schemas, compatibility schema lane, slug/path drift, greenfield policy, documentation-led tests, partial shared runtime coverage, and TODO-only CI;
- added carried/crossed identity, geometry-not-evidence, source-role, time/current-status, historic/modern, graph-derivation, sensitivity, rights, carrier, correction, and rollback invariants;
- added explicit structural, navigation, legal-access, live-routing, emergency, and safe-passage denials;
- added proposed input packet, report contract, finite outcomes, reason-code families, tests, CI contract, implementation sequence, definition of done, migration/deprecation, verification register, rollback, and evidence ledger;
- paired the revision with a generated provenance receipt.

### v0.1 — 2026-07-07

- replaced the empty file with a broad proposed Bridge/RiverCrossing validator guide.

[Back to top](#top)
