<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/tools-validators-transport-facility-topology-readme
title: tools/validators/transport-facility-topology README
type: README
version: v0.1
status: draft
owner: TODO-tooling-qa-owner-plus-roads-rail-trade-steward-plus-transport-facility-steward-plus-network-topology-steward-plus-settlements-infrastructure-steward-plus-policy-steward-plus-evidence-steward-plus-release-steward
created: 2026-07-08
updated: 2026-07-08
policy_label: repository-facing; transport-facility-topology-validator-index; roads-rail-trade; transport-facility; network-node; network-edge; graph-projection; source-role-aware; temporal-scope-aware; sensitivity-aware; release-gated; rollback-aware; not-live-routing; not-legal-access; not-facility-truth; non-authoritative
owning_root: tools/
responsibility: transport facility topology validator routing README under tools/validators; documents validation expectations for transport-facility role claims, facility-to-network-node linkage, facility-to-road/rail/crossing/corridor relationships, graph-projection derivation, source-role preservation, temporal scope, identity boundary with settlements-infrastructure, topology consistency, route/corridor membership posture, operator/status/restriction adjacency, sensitivity and critical-transport review, evidence/proof linkage, policy/review/release posture, correction cascade, rollback support, public-surface denial, schema/fixture/test routing, and finite outcomes while deferring domain meaning, canonical schemas, policy decisions, evidence records, receipts, lifecycle data, graph runtime storage, release records, public runtime code, and release authority to their owning roots
truth_posture: cite-or-abstain; implementation claims require current repo evidence
related:
  - ../README.md
  - ../_common/README.md
  - ../source_role/README.md
  - ../sensitivity/README.md
  - ../rights/README.md
  - ../policy/README.md
  - ../release/README.md
  - ../promotion_gate/README.md
  - ../geometry/README.md
  - ../../../contracts/domains/roads-rail-trade/transport_facility.md
  - ../../../contracts/domains/roads-rail-trade/network_node.md
  - ../../../contracts/domains/roads-rail-trade/network_edge.md
  - ../../../contracts/domains/roads-rail-trade/road_segment.md
  - ../../../contracts/domains/roads-rail-trade/rail_segment.md
  - ../../../contracts/domains/roads-rail-trade/crossing.md
  - ../../../contracts/domains/roads-rail-trade/bridge.md
  - ../../../contracts/domains/roads-rail-trade/ferry.md
  - ../../../contracts/domains/roads-rail-trade/river_crossing.md
  - ../../../contracts/domains/roads-rail-trade/depot.md
  - ../../../contracts/domains/roads-rail-trade/siding.md
  - ../../../contracts/domains/roads-rail-trade/yard.md
  - ../../../contracts/domains/roads-rail-trade/corridor_route.md
  - ../../../contracts/domains/roads-rail-trade/route_membership.md
  - ../../../contracts/domains/roads-rail-trade/operator_assignment.md
  - ../../../contracts/domains/roads-rail-trade/operator_status.md
  - ../../../contracts/domains/roads-rail-trade/status_event.md
  - ../../../contracts/domains/roads-rail-trade/restriction_event.md
  - ../../../docs/domains/roads-rail-trade/OBJECT_FAMILIES.md
  - ../../../docs/domains/roads-rail-trade/GRAPH_PROJECTIONS.md
  - ../../../docs/domains/roads-rail-trade/IDENTITY_MODEL.md
  - ../../../docs/domains/roads-rail-trade/SENSITIVITY.md
  - ../../../docs/domains/roads-rail-trade/MAP_UI_CONTRACTS.md
  - ../../../data/processed/roads-rail-trade/facilities/README.md
  - ../../../data/quarantine/roads-rail-trade/README.md
  - ../../../data/registry/sources/roads-rail-trade/README.md
  - ../../../schemas/contracts/v1/domains/roads-rail-trade/
  - ../../../policy/domains/roads-rail-trade/
  - ../../../data/proofs/
  - ../../../data/receipts/
  - ../../../release/
  - ../../../fixtures/domains/roads-rail-trade/
  - ../../../tests/domains/roads-rail-trade/
notes:
  - "This README replaces an empty placeholder at tools/validators/transport-facility-topology/README.md. It does not confirm executable validators, registry wiring, topology algorithms, schemas, fixtures, policy bundles, receipt emission, runtime behavior, graph runtime behavior, or CI behavior."
  - "TransportFacility is a source-scoped transport-role claim. It is not canonical place/facility identity, infrastructure asset truth, property title, legal access, live service, operator legal identity, structural condition, map truth, graph truth, or publication approval."
  - "NetworkNode is a derived graph-projection object. It is not canonical place truth, facility truth, segment truth, live routing authority, legal-access authority, EvidenceBundle truth, or publication approval."
  - "Topology validation may check consistency of links among facilities, nodes, roads, rail, crossings, corridors, route memberships, status/restriction events, and operator assignments, but it must not create graph truth or public routing authority."
  - "Critical-transport detail, condition/vulnerability fields, restricted-source-derived fields, culturally sensitive corridor joins, legal access, emergency status, active service, freight capacity, and exact coordinates require fail-closed review and must not be exposed by validator docs or public surfaces."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# tools/validators/transport-facility-topology

![status](https://img.shields.io/badge/status-draft-orange)
![root](https://img.shields.io/badge/root-tools%2F-blue)
![scope](https://img.shields.io/badge/scope-transport--facility--topology-informational)
![authority](https://img.shields.io/badge/authority-validator--not--topology--truth-lightgrey)
![posture](https://img.shields.io/badge/posture-release--gated-critical)
![truth](https://img.shields.io/badge/truth-cite--or--abstain-success)

> **One-line purpose.** `tools/validators/transport-facility-topology/` is the validator routing lane for checking transport-facility role claims and their topology links to network nodes, road/rail segments, crossings, corridors, route memberships, operators, status/restriction events, evidence, policy, release, and public-surface envelopes without becoming facility truth, graph truth, live routing authority, infrastructure authority, or publication authority.

---

## Purpose

`tools/validators/transport-facility-topology/` exists to make transport-facility topology validation visible under the durable `tools/validators/` surface.

The durable KFM question for this lane is:

> Does a transport facility topology candidate preserve the difference between a source-scoped facility role claim, canonical facility/place identity, derived graph nodes/edges, route/corridor membership, operator/status/restriction context, evidence support, source-role/time posture, sensitivity review, policy decision, release reference, correction path, rollback target, and public-surface limits?

The answer should be a deterministic validation result or routing decision. This folder should not define Roads/Rail/Trade meaning, create canonical facility identity, certify structural condition, decide legal access, create graph runtime truth, create EvidenceBundles, write receipts, store lifecycle data, approve release, publish map layers, expose public API payloads, authorize live routing, or generate public answers from unresolved topology.

[Back to top](#top)

---

## Status

| Surface | Status | Notes |
|---|---|---|
| `tools/validators/transport-facility-topology/README.md` | **CONFIRMED README** | This README replaces the previous empty placeholder. |
| `contracts/domains/roads-rail-trade/transport_facility.md` | **CONFIRMED draft contract / schema and runtime NEEDS VERIFICATION** | Defines `transport_facility` as a source-scoped transport-role claim and explicitly excludes canonical place/facility identity, legal access, live service, graph truth, map truth, and publication approval. |
| `contracts/domains/roads-rail-trade/network_node.md` | **CONFIRMED draft contract / schema and runtime NEEDS VERIFICATION** | Defines `network_node` as a derived graph-projection object and excludes canonical place/facility truth, live routing, legal access, graph runtime storage, and publication approval. |
| `docs/domains/roads-rail-trade/OBJECT_FAMILIES.md` | **CONFIRMED object-family reference / field realization NEEDS VERIFICATION** | Names Roads/Rail/Trade object families including `Network Node`, `TransportFacility`, corridors, route membership, crossings, events, and operator assignments; field realization remains proposed. |
| `data/processed/roads-rail-trade/facilities/README.md` | **CONFIRMED processed-lane README / payload behavior NEEDS VERIFICATION** | Processed facility artifacts are not public by default and require catalog, evidence, rights, sensitivity, policy, release, correction, and rollback support before public use. |
| `data/quarantine/roads-rail-trade/README.md` | **CONFIRMED quarantine README / payload behavior NEEDS VERIFICATION** | Unresolved route identity, network topology, critical-transport sensitivity, cultural-corridor sensitivity, geometry precision, review, receipt, correction, or rollback support stays no-public-path. |
| Executable transport-facility topology scripts, topology algorithms, registry wiring, schemas, fixtures, policy bundles, reports, receipts, release integration, graph runtime behavior, public API behavior, and CI wiring | **NEEDS VERIFICATION** | This README is documentation only. |

[Back to top](#top)

---

## Relationship to nearby lanes

| Concern | Preferred home | Boundary |
|---|---|---|
| Transport-facility topology validation | `tools/validators/transport-facility-topology/` | Checks facility-role topology packets and fail-closed posture. |
| Roads/Rail/Trade contracts | `contracts/domains/roads-rail-trade/` | Define semantic object meaning; validators check conformance. |
| Facility processed data | `data/processed/roads-rail-trade/facilities/` | Holds processed artifacts, not public truth. |
| Held/unresolved roads/rail/trade material | `data/quarantine/roads-rail-trade/` | No-public-path hold lane. |
| Canonical facility/place identity | Settlements/Infrastructure homes when verified | Transport role may cite but must not absorb facility/place authority. |
| Water crossing evidence | Hydrology homes when verified | Crossings may cite hydrology; they do not own river/water truth. |
| Roads/Rail/Trade schemas | `schemas/contracts/v1/domains/roads-rail-trade/` or accepted schema homes | Machine shape only. |
| Roads/Rail/Trade policy | `policy/domains/roads-rail-trade/` and sensitivity policy homes | Policy decides allow/deny/restrict/hold/abstain. |
| Evidence/proofs and receipts | `data/proofs/`, `data/receipts/` | Validators check refs; they do not create authority records here. |
| Release and rollback | `release/` | Validator success is not release approval. |
| Fixtures and tests | `fixtures/domains/roads-rail-trade/`, `tests/domains/roads-rail-trade/` | Synthetic examples and tests prove behavior; they are not topology authority. |

[Back to top](#top)

---

## Validation packet

A transport-facility topology candidate should expose enough explicit context for deterministic validation.

| Required family | Validator expectation | Must not be treated as |
|---|---|---|
| Candidate identity | Candidate id, object family, lifecycle state, source refs, artifact refs, requested audience, operation, and surface. | Permission by naming convention. |
| Facility role claim | Transport role, facility class, source-scoped name, source role, temporal scope, and admissibility limits are explicit. | Canonical facility/place truth. |
| Topology links | Network node refs, network edge refs, road/rail segment refs, crossing/bridge/ferry/river-crossing refs, corridor refs, and route membership refs resolve where required. | Graph truth or live routing authority. |
| Identity boundary | Settlement/infrastructure/place/building/operator/legal-access facts remain cited external authority where applicable. | Absorption of another domain's truth. |
| Source-role posture | Administrative rosters, observed records, modeled reconstructions, aggregate summaries, candidate connector outputs, and synthetic descriptions remain distinct. | Source-role collapse or upgrade. |
| Temporal posture | Valid time, observed time, asserted time, status time, restriction time, historical period, supersession, and stale-state posture are visible. | Current service/status guarantee. |
| Geometry/topology posture | Geometry role, topology role, precision/exposure posture, public-safe derivative state, and reconstruction risk are checked. | Public exact-location permission. |
| Sensitivity/rights posture | Critical-transport, culturally sensitive corridor, condition/vulnerability, restricted-source, operator, access, and rights constraints are resolved. | Public release by processed status. |
| Evidence/policy/release support | EvidenceRef, EvidenceBundle/proof refs, validation report, policy decision, reason codes, obligations, review bindings, release reference, correction path, rollback target, and receipts exist where required. | Publication by validator success. |
| Public-surface envelope | Map/API/tile/export/screenshot/graph/search/Focus Mode/embedding/AI surfaces are limited to released, public-safe derivatives and caveats. | Unbounded reuse across public surfaces. |

[Back to top](#top)

---

## Topology invariants

| Invariant | Validator expectation | Fail / abstain condition |
|---|---|---|
| Facility role is not facility truth | A TransportFacility describes how a source places a facility in transport evidence. | Candidate certifies place identity, asset identity, property title, legal access, or structural condition. |
| Network nodes are derived | NetworkNode represents a rebuildable graph projection from catalog-closed evidence. | Candidate treats node as canonical place/facility truth or routing authority. |
| Source roles do not collapse | Administrative, observed, modeled, aggregate, candidate, and synthetic source roles remain distinct. | Candidate upgrades role or hides uncertainty. |
| Topology links resolve | Facility-to-node/edge/segment/crossing/corridor relations resolve to governed refs. | Link is inferred only from proximity, name similarity, UI display, or generated text. |
| Cross-domain truth stays external | Settlements/Infrastructure, Hydrology, Hazards, Archaeology/Cultural Heritage, People/Land, and operators retain their own authority. | Roads/Rail/Trade validator absorbs external truth. |
| Sensitive infrastructure fails closed | Critical-transport detail, conditions, vulnerabilities, exact locations, restricted-source fields, and cultural-corridor joins require review and policy support. | Public surface exposes restricted detail. |
| Current status is not assumed | Status, restriction, service, access, and operator claims are time-bound and source-bound. | Candidate implies current operational status without support. |
| Corrections cascade | Facility, topology, route, source, status, restriction, rights, sensitivity, or release changes invalidate dependent graph/public outputs. | Downstream graph or map remains active after blocking change. |
| Carriers are not authority | Maps, tiles, graph views, exports, screenshots, Focus Mode, embeddings, and AI answers are downstream carriers. | Carrier becomes evidence, topology, routing, or release authority. |

[Back to top](#top)

---

## Fail-closed conditions

A transport-facility topology candidate should fail closed, deny, restrict, abstain, or route to steward review when:

- facility role, topology role, source role, temporal scope, lifecycle state, source refs, object refs, or route/corridor membership refs are missing;
- facility-to-node, node-to-edge, facility-to-segment, facility-to-crossing, facility-to-corridor, or facility-to-operator links are unresolved, circular, duplicated, contradicted, proximity-only, name-only, or generated-only;
- canonical facility/place identity, property title, legal access, structural condition, active service, operator legal identity, emergency status, or live routing is implied without the correct external authority;
- source-role boundaries collapse across administrative, observed, modeled, aggregate, candidate, synthetic, or regulatory records;
- temporal state is stale, missing, contradicted, or overbroad;
- critical-transport detail, condition/vulnerability fields, restricted-source-derived fields, culturally sensitive corridor joins, private operator detail, or exact geometry is public-bound without review and policy support;
- EvidenceRef, EvidenceBundle, validation report, receipt, policy decision, review binding, release reference, correction path, rollback target, or supersession posture is missing where required;
- public map, tile, export, screenshot, graph, search, Focus Mode, popup, or AI output would expose unreleased topology or overclaim facility/network truth.

[Back to top](#top)

---

## Authority boundary

| Responsibility | Home |
|---|---|
| Transport-facility topology validator routing | `tools/validators/transport-facility-topology/` |
| Roads/Rail/Trade semantic contracts | `contracts/domains/roads-rail-trade/` |
| Roads/Rail/Trade machine schemas | `schemas/contracts/v1/domains/roads-rail-trade/` or accepted schema homes |
| Roads/Rail/Trade source registry | `data/registry/sources/roads-rail-trade/` |
| Processed facility artifacts | `data/processed/roads-rail-trade/facilities/` |
| Quarantined unresolved Roads/Rail/Trade material | `data/quarantine/roads-rail-trade/` |
| Graph/public artifacts | governed catalog/triplet/published/release homes only after gates close |
| Sensitivity and domain policy | `policy/domains/roads-rail-trade/`, accepted sensitivity policy homes |
| Evidence/proofs | `data/proofs/` |
| Receipts | `data/receipts/` |
| Release records and rollback | `release/` |
| Fixtures | `fixtures/domains/roads-rail-trade/` and accepted fixture homes |
| Tests | `tests/domains/roads-rail-trade/` and accepted test homes |
| Public API/UI/map/AI runtime | governed application/runtime roots |

Safe interpretation:

- **CONFIRMED:** this README exists.
- **PROPOSED:** validator code may live here when it checks declared transport-facility topology invariants and delegates semantic meaning, canonical schemas, policy decisions, evidence, receipts, lifecycle data, graph runtime storage, release records, and public runtime authority to owning roots.
- **NEEDS VERIFICATION:** exact executable files, registry entries, topology algorithms, schemas, fixture files, test paths, policy bundle homes, report destinations, receipt emission, release integration, graph runtime behavior, public API behavior, and CI wiring.
- **DENY:** using this folder as canonical facility truth, infrastructure authority, live routing authority, legal access authority, graph runtime store, source registry, policy home, schema home, evidence store, proof store, receipt store, lifecycle data store, release record store, public runtime surface, AI answer source, or publication authority.

[Back to top](#top)

---

## What belongs here

Good fits for `tools/validators/transport-facility-topology/` include:

- this README;
- small validation adapters that check transport-facility topology packets;
- checks for facility-to-node/edge/segment/crossing/corridor/operator/status/restriction refs;
- checks that topology links are evidence-backed rather than proximity-only, name-only, UI-only, or generated-only;
- checks that TransportFacility remains a transport-role claim and NetworkNode remains a derived graph projection;
- checks for source-role preservation, temporal scope, sensitivity, rights, review, release, correction, and rollback support;
- finite outcome vocabulary and reason-code mapping;
- report destination notes that keep generated outputs out of policy, receipt, proof, lifecycle, graph runtime, and release authority unless explicitly routed to accepted homes.

[Back to top](#top)

---

## What does not belong here

| Do not put in this folder | Correct home |
|---|---|
| Roads/Rail/Trade semantic contracts | `contracts/domains/roads-rail-trade/` |
| Machine schemas, DTOs, enums, topology object schemas | `schemas/contracts/v1/domains/roads-rail-trade/` or accepted schema homes |
| Facility data, graph data, network payloads, route/corridor artifacts, public map artifacts | governed `data/` lifecycle roots and `release/` after gates close |
| Legal access, live routing, active service, emergency status, structural condition, vulnerability, or security determinations | authoritative external/domain-specific homes and policy/review workflows |
| Policy rules, allowlists, denylists, steward decisions, release decisions | `policy/`, `release/`, accepted governance homes |
| EvidenceBundles, proof packs, receipts, ValidationReports | `data/proofs/`, `data/receipts/`, accepted report lanes |
| Tests and fixtures | `tests/` and `fixtures/` conventions |
| Public API, UI, MapLibre runtime code, tile service code, Focus Mode, export, screenshot, graph, embedding, or AI runtime code | governed application/runtime roots |
| Secrets, source credentials, restricted infrastructure fields, sensitive exact locations, hidden thresholds, production signing keys, or reconstruction hints | denied here; keep out of repository-facing validator docs |

[Back to top](#top)

---

## Standard outcomes

| Outcome | Meaning |
|---|---|
| `TRANSPORT_FACILITY_TOPOLOGY_PASS` | Candidate passed configured transport-facility topology checks. |
| `TRANSPORT_FACILITY_TOPOLOGY_FAIL` | Candidate failed one or more configured checks. |
| `TRANSPORT_FACILITY_TOPOLOGY_DENY` | Candidate must not proceed because topology, evidence, policy, review, release, rollback, or public-surface support cannot be resolved. |
| `TRANSPORT_FACILITY_TOPOLOGY_RESTRICT` | Candidate may proceed only in restricted/steward-gated contexts. |
| `TRANSPORT_FACILITY_TOPOLOGY_ABSTAIN` | Candidate lacks enough support for a topology assertion. |
| `FACILITY_ROLE_MISSING` | Required transport-facility role claim is absent. |
| `NETWORK_NODE_REF_MISSING` | Required network-node reference is absent or unresolved. |
| `NETWORK_EDGE_REF_MISSING` | Required network-edge reference is absent or unresolved. |
| `TOPOLOGY_LINK_UNRESOLVED` | Facility/node/edge/segment/crossing/corridor/operator/status link is unresolved. |
| `TOPOLOGY_LINK_PROXIMITY_ONLY_DENIED` | Link is inferred only from distance, name similarity, UI display, or generated text. |
| `FACILITY_IDENTITY_OVERCLAIM` | Transport role claim is treated as canonical facility/place/infrastructure truth. |
| `GRAPH_PROJECTION_OVERCLAIM` | Derived graph node/edge is treated as live routing, legal access, or canonical truth. |
| `SOURCE_ROLE_COLLAPSE_DENIED` | Administrative/observed/modeled/aggregate/candidate/synthetic roles are collapsed or upgraded. |
| `TEMPORAL_SCOPE_MISSING` | Required valid/asserted/status/restriction time posture is absent. |
| `SENSITIVITY_REVIEW_REQUIRED` | Critical-transport, cultural-corridor, restricted-source, condition, vulnerability, or exact-geometry context requires review. |
| `POLICY_OR_REVIEW_GAP` | Required policy decision, review state, rights posture, sensitivity posture, or obligations are absent. |
| `EVIDENCE_REF_MISSING` | Required EvidenceRef, EvidenceBundle, proof, or validation support is absent. |
| `RELEASE_REFERENCE_MISSING` | Required release, correction, withdrawal, reevaluation, or rollback reference is absent. |
| `CORRECTION_CASCADE_MISSING` | Facility/topology/source/status/restriction correction did not propagate downstream. |
| `PUBLIC_SURFACE_LEAKAGE_DENIED` | Candidate would expose unsupported or sensitive transport topology to public API, map, tile, export, screenshot, graph, Focus Mode, embedding, or AI surfaces. |
| `VALIDATOR_SYSTEM_ERROR` | Validator could not complete because of malformed input, missing dependency, missing registry entry, evaluator error, timeout, or unexpected runtime error. |

[Back to top](#top)

---

## Minimal future layout

Future implementation should remain small and reversible:

```text
tools/validators/transport-facility-topology/
├── README.md
├── validate_transport_facility_topology.py  # PROPOSED; not confirmed
├── validate_facility_node_links.py          # PROPOSED; not confirmed
├── validate_topology_public_surface.py      # PROPOSED; not confirmed
└── registry_notes.md                        # PROPOSED; documentation only
```

Do not add executable validators, policy bundles, topology datasets, local schema files, facility payloads, graph payloads, release records, or fixtures unless the placement decision is documented, the canonical authority relationship is explicit, and tests prove fail-closed behavior without granting facility, topology, routing, public-surface, or release authority.

[Back to top](#top)

---

## Acceptance checklist

This README is complete for documentation purposes when:

- [x] It replaces the empty placeholder at `tools/validators/transport-facility-topology/README.md`.
- [x] It marks this path as validator routing, not facility truth, graph truth, infrastructure authority, live routing authority, legal access authority, schema authority, policy authority, proof/receipt storage, release record storage, public runtime, or AI authority.
- [x] It preserves TransportFacility as a source-scoped transport-role claim and NetworkNode as a derived graph projection.
- [x] It preserves source-role, temporal, topology, evidence, sensitivity, rights, review, release, correction, rollback, and public-surface boundaries.
- [x] It routes domain meaning to `contracts/` and `docs/`, machine shape to `schemas/`, policy to `policy/`, receipts/proofs to `data/`, release records to `release/`, fixtures to `fixtures/`, and tests to `tests/`.
- [x] It marks executable scripts, registry wiring, topology algorithms, schemas, fixtures, tests, policy bundles, receipt emission, release integration, graph runtime behavior, public API behavior, and CI wiring as **NEEDS VERIFICATION**.

Future implementation is not complete until:

- [ ] Validator registry or CLI references to transport-facility topology validators are searched and classified.
- [ ] TransportFacility, NetworkNode, NetworkEdge, route/corridor, crossing, operator/status/restriction schema bindings are verified.
- [ ] Facility-to-node/edge/segment/crossing/corridor/operator/status fixtures are added only as synthetic/minimized public-safe payloads with documented expected outcomes.
- [ ] Tests prove positive, negative, deny, restrict, abstain, missing-facility-role, missing-node-ref, unresolved-link, proximity-only-link, source-role-collapse, temporal-scope-missing, sensitivity-review-required, release-missing, correction-cascade-missing, and public-surface-blocked cases.
- [ ] CI invokes transport-facility topology validators in deterministic order.
- [ ] Any generated validation outputs write only to accepted report, proof, receipt, or artifact roots.

[Back to top](#top)

---

## Changelog

| Date | Change | Status |
|---|---|---|
| 2026-07-08 | Replaced empty placeholder with transport-facility topology validator README. | **CONFIRMED README / implementation NEEDS VERIFICATION** |
