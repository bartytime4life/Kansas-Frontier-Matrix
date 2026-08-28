<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/contracts-domains-roads-rail-trade-yard
title: Yard Contract — Roads / Rail / Trade Routes
type: semantic-contract
version: v0.2
status: draft; PROPOSED; schema-missing; slug-CONFLICTED; rail-facility-role; NEEDS VERIFICATION before promotion
owners:
  - OWNER_TBD — Roads/Rail/Trade Routes domain steward
  - OWNER_TBD — Rail steward
  - OWNER_TBD — Settlements/Infrastructure steward
  - OWNER_TBD — Contracts steward
  - OWNER_TBD — Source steward
  - OWNER_TBD — Evidence steward
  - OWNER_TBD — Schema steward
  - OWNER_TBD — Policy steward
  - OWNER_TBD — Release steward
  - OWNER_TBD — Docs steward
created: NEEDS VERIFICATION — scaffold existed before v0.2 expansion
updated: 2026-06-23
policy_label: public; contracts; roads-rail-trade; yard; rail-yard; rail-facility-role; transport-side-claim; source-role-aware; temporal-scope-aware; evidence-bound; settlements-infrastructure-boundary-aware; rail-segment-adjacent; siding-adjacent; depot-adjacent; operator-status-aware; graph-projection-aware; infrastructure-sensitive; release-gated; rollback-aware; not-property-title; not-structural-inspection; not-live-service-status; not-switching-instruction; not-operational-authority; not-publication-authority
tags: [kfm, contracts, roads-rail-trade, yard, rail-yard, terminal-yard, classification-yard, storage-yard, interchange-yard, depot, siding, transport-facility, rail-segment, corridor-route, route-membership, operator-assignment, operator-status, status-event, route-event, access-restriction, restriction-event, settlement, infrastructure-identity, network-node, network-edge, source-role, valid-time, EvidenceBundle, PolicyDecision, ReviewRecord, ReleaseManifest, RollbackCard]
related:
  - ./README.md
  - ./rail_segment.md
  - ./depot.md
  - ./siding.md
  - ./transport_facility.md
  - ./corridor_route.md
  - ./route_membership.md
  - ./operator_assignment.md
  - ./operator_status.md
  - ./route_event.md
  - ./status_event.md
  - ./access_restriction.md
  - ./restriction_event.md
  - ./crossing.md
  - ./bridge.md
  - ./river_crossing.md
  - ./network_node.md
  - ./network_edge.md
  - ./movement_story_node.md
  - ./domain_observation.md
  - ./domain_feature_identity.md
  - ./domain_validation_report.md
  - ./domain_layer_descriptor.md
  - ../roads/README.md
  - ../../../docs/domains/roads-rail-trade/README.md
  - ../../../docs/domains/roads-rail-trade/CANONICAL_PATHS.md
  - ../../../docs/domains/roads-rail-trade/OBJECT_FAMILIES.md
  - ../../../docs/domains/roads-rail-trade/IDENTITY_MODEL.md
  - ../../../docs/domains/roads-rail-trade/DATA_LIFECYCLE.md
  - ../../../docs/domains/roads-rail-trade/SOURCES.md
  - ../../../docs/domains/roads-rail-trade/sublanes/rail.md
  - ../../../docs/domains/roads-rail-trade/GRAPH_PROJECTIONS.md
  - ../../../docs/domains/roads-rail-trade/MAP_UI_CONTRACTS.md
  - ../../../docs/runbooks/roads-rail-trade/PROMOTION_RUNBOOK.md
  - ../../../docs/runbooks/roads-rail-trade/ROLLBACK_RUNBOOK.md
  - ../../../schemas/contracts/v1/domains/roads-rail-trade/yard.schema.json
  - ../../../policy/domains/roads-rail-trade/
  - ../../../fixtures/domains/roads-rail-trade/yard/
  - ../../../tests/domains/roads-rail-trade/
  - ../../../release/candidates/roads-rail-trade/
notes:
  - "Expanded from a PROPOSED scaffold at contracts/domains/roads-rail-trade/yard.md."
  - "A paired schema at schemas/contracts/v1/domains/roads-rail-trade/yard.schema.json was not found in this task. Field realization remains PROPOSED."
  - "The parent domain names Yard as a Roads / Rail / Trade Routes object, while rail sublane doctrine warns that depot/siding/yard facility canonical identity remains settlement/infrastructure-owned."
  - "The Transport Facility contract defines the broader source-scoped facility role surface; Yard is the rail-yard specialization of that role pattern."
  - "The Siding contract uses the same rail-facility boundary pattern: the Roads/Rail/Trade file defines the rail-network role claim, not full place, building, title, structural, legal-entity, operator, switching, or live-service authority."
  - "This contract defines source-scoped yard meaning. It does not prove rail-segment identity, facility canonical identity, property title, switching permission, current service, operator control, legal access, graph truth, map truth, or publication approval."
  - "The Roads / Rail / Trade Routes docs record a slug conflict between roads-rail-trade and transport for contract/schema homes. This file preserves the observed requested path and does not resolve the ADR question."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Yard Contract — Roads / Rail / Trade Routes

> Semantic contract for `yard`: the transport-side claim that a rail-associated facility, track group, switching area, classification area, storage area, interchange point, terminal yard, depot-adjacent rail area, or historic rail feature functioned as a yard in rail movement evidence — without becoming rail-segment truth, settlement/infrastructure canonical identity, property title, switch authority, current service authority, live operating instruction, graph truth, map truth, or publication approval.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Root: contracts" src="https://img.shields.io/badge/root-contracts%2F-0a7ea4">
  <img alt="Domain: roads-rail-trade" src="https://img.shields.io/badge/domain-roads--rail--trade-slategray">
  <img alt="Schema: missing" src="https://img.shields.io/badge/schema-missing-red">
  <img alt="Truth: rail role claim" src="https://img.shields.io/badge/truth-rail__role__claim-blue">
  <img alt="Boundary: facility identity separate" src="https://img.shields.io/badge/boundary-facility__identity__separate-orange">
  <img alt="Publication: release gated" src="https://img.shields.io/badge/publication-release--gated-orange">
</p>

`contracts/domains/roads-rail-trade/yard.md`

## Quick jumps

[Status](#status) · [Meaning](#meaning) · [Repo fit](#repo-fit) · [Schema posture](#schema-posture) · [Accepted uses](#accepted-uses) · [Exclusions](#exclusions) · [Recommended fields](#recommended-fields) · [Invariants](#invariants) · [Yard claim families](#yard-claim-families) · [Source-role and time rules](#source-role-and-time-rules) · [Lifecycle](#lifecycle) · [Validation](#validation) · [Rollback](#rollback) · [Evidence basis](#evidence-basis) · [Open questions](#open-questions)

---

## Status

> [!IMPORTANT]
> **Status:** `draft` / semantic contract  
> **Owner:** `OWNER_TBD`  
> **Contract path:** `contracts/domains/roads-rail-trade/yard.md`  
> **Schema path:** `schemas/contracts/v1/domains/roads-rail-trade/yard.schema.json` — **not found in this task**  
> **Truth posture:** target path and prior scaffold are confirmed from current repo evidence. `Yard` is confirmed as a Roads / Rail / Trade Routes object term in the domain vocabulary and as a rail sublane in-scope rail-network facility type whose identity remains settlement/infrastructure-owned. Exact schema fields, validator behavior, fixture coverage, policy behavior, source-registry behavior, release manifests, emitted proofs, public API behavior, map rendering, graph behavior, and runtime behavior remain **NEEDS VERIFICATION**.

> [!CAUTION]
> This contract defines yard meaning only. It does **not** certify track ownership, property title, switch permission, train handling authority, active service, structural condition, depot/siding/facility identity, current operating railroad authority, public access, emergency status, map/API behavior, or publication approval.

---

## Meaning

`yard` records the semantic meaning of a rail-associated yard claim inside Roads / Rail / Trade Routes.

It may represent that a source asserts a yard:

- functioned as a classification yard, storage yard, terminal yard, interchange yard, industry yard, depot-adjacent yard, team-track yard, switching yard, maintenance-of-way yard, freight yard, passenger-coach yard, or historic yard;
- was associated with a `Rail Segment`, `CorridorRoute`, `RouteMembership`, `Depot`, `Siding`, `TransportFacility`, `OperatorAssignment`, `OperatorStatus`, `RouteEvent`, `StatusEvent`, `AccessRestriction`, `NetworkNode`, `NetworkEdge`, or released map/Focus Mode view;
- had a source-scoped name, railroad/operator relation, timetable relation, station/agency-point relation, line/branch relation, map relation, asset/inventory relation, historical period, or yard-site claim;
- may contribute to a released graph projection only as a governed, evidence-cited, release-gated derivative;
- may cite settlement, infrastructure, land, parcel, building, railroad, operating, historical, preservation, or hazard evidence without absorbing those domains' authority.

The yard contract owns the **rail-network role claim**: how a track group or facility-adjacent rail feature functioned as a yard in rail movement, route evidence, operator evidence, and historical transport context. The canonical place/facility identity usually belongs to `settlements-infrastructure`. Property, parcel, deed, right-of-way, or ownership truth belongs to People/Land or the relevant source authority. Operational permission, switching instructions, yard limits, service status, dispatching, and safety claims require separate authoritative and policy-reviewed records.

---

## Repo fit

| Responsibility | Path or root | Relationship |
|---|---|---|
| Parent contract lane | `./README.md` | Defines this folder as semantic contracts only. |
| Rail segment companion | `./rail_segment.md` | Yard may cite rail-alignment evidence; it does not replace rail segment identity. |
| Related rail facility contracts | `./depot.md`, `./siding.md`, `./transport_facility.md` | Adjacent rail role/facility meanings; canonical place/facility identity remains separate. |
| Route/corridor contracts | `./corridor_route.md`, `./route_membership.md` | Yard may participate in a route/corridor context without becoming route membership. |
| Operator/status/event contracts | `./operator_assignment.md`, `./operator_status.md`, `./route_event.md`, `./status_event.md`, `./access_restriction.md`, `./restriction_event.md` | Operator, status, route, restriction, and event semantics remain separate. |
| Crossing and bridge contracts | `./crossing.md`, `./bridge.md`, `./river_crossing.md` | Yard may be near or connected to crossing/bridge evidence without absorbing those meanings. |
| Graph contracts | `./network_node.md`, `./network_edge.md` | Derived topology; graph output must cite yard evidence. |
| Parent doctrine | `../../../docs/domains/roads-rail-trade/README.md` | Domain scope and object roster. |
| Rail sublane dossier | `../../../docs/domains/roads-rail-trade/sublanes/rail.md` | Rail-specific realization and explicit non-ownership of depot/siding/yard facility canonical identity. |
| Object families | `../../../docs/domains/roads-rail-trade/OBJECT_FAMILIES.md` | Broader object-family spine and deterministic identity posture; Yard appears in the domain/rail sublane vocabulary rather than the fourteen-family table. |
| Schemas | `../../../schemas/contracts/v1/domains/roads-rail-trade/` or ADR-selected alternate | Machine shape; paired schema missing in this task. |
| Policy | `../../../policy/domains/roads-rail-trade/` or ADR-selected alternate | Allow/deny/restrict/abstain decisions. |
| Fixtures/tests | `../../../fixtures/domains/roads-rail-trade/`, `../../../tests/domains/roads-rail-trade/` | Behavior proof; not contract prose. |
| Release/rollback | `../../../release/candidates/roads-rail-trade/` and release roots | Promotion, release, correction, and rollback. |

---

## Schema posture

A direct paired schema was checked at:

```text
schemas/contracts/v1/domains/roads-rail-trade/yard.schema.json
```

That file was **not found** in this task.

> [!WARNING]
> Because no paired schema was confirmed, every field below is **PROPOSED** semantic guidance. Do not treat it as machine-enforced until schema, fixtures, validator, source registry records, policy tests, release checks, governed API behavior, map behavior, graph behavior, and runtime behavior are verified.

---

## Accepted uses

| Use | Allowed? | Rule |
|---|---:|---|
| Recording a source-scoped yard role claim | Yes | Must preserve source role, time scope, identity, evidence, and limitations. |
| Associating a yard with rail segments or route membership | Yes | Use refs; do not embed rail-segment or route-membership truth in the yard. |
| Associating a yard with depot, siding, station, terminal, or facility context | Conditional | Facility/place identity remains separate and may be settlement/infrastructure-owned. |
| Supporting operator/status/event context | Conditional | Operator/status/event semantics remain separate and valid-time scoped. |
| Supporting graph projections | Conditional | Network nodes/edges are derived and rollbackable. |
| Supporting public map/Focus Mode display | Conditional | Requires EvidenceBundle, PolicyDecision, ReviewRecord, ReleaseManifest, correction path, and RollbackCard. |
| Proving active service, switching authority, legal access, ownership, structural condition, or safety | No | Requires separate authoritative evidence and policy review; often should abstain or deny. |
| Acting as live railroad operating instruction | No | KFM is not operational railroad authority under this contract. |

---

## Exclusions

`yard` must not be used as:

| Misuse | Required outcome |
|---|---|
| Rail Segment replacement | Use `rail_segment.md` for track-centerline/alignment evidence. |
| Depot/Siding/TransportFacility canonical identity | Use the relevant facility contracts and Settlements/Infrastructure ownership boundary. |
| Property title or right-of-way proof | `ABSTAIN`; cite People/Land/legal authority if policy-cleared. |
| Active service, yard limit, or train operation proof | Use OperatorStatus, StatusEvent, source authority, and release gates. |
| Switching instruction, dispatching rule, or safety advice | `DENY`; outside KFM public documentation scope. |
| Operator legal-entity truth | Use People/Land or legal/corporate source authority. |
| Public access authority | `ABSTAIN`; yard relation does not confer legal access. |
| Graph canonical truth | Network nodes/edges are derived; EvidenceBundle and yard records outrank projections. |
| Public API/map payload by itself | Use governed API/released artifacts only. |
| Publication approval | ReleaseManifest, ReviewRecord, PolicyDecision, correction path, and RollbackCard remain separate. |

---

## Recommended fields

The following fields are **PROPOSED** until a schema is added and validated.

| Field | Meaning |
|---|---|
| `id` | Canonical yard identifier. |
| `version` | Contract/object version. |
| `spec_hash` | Deterministic hash over normalized yard role-claim content. |
| `domain` | Expected value: `roads-rail-trade` unless ADR selects another slug. |
| `yard_name` | Source-stated or normalized yard label, if any. |
| `yard_type` | Classification yard, storage yard, terminal yard, interchange yard, industry yard, depot-adjacent yard, maintenance yard, freight yard, coach yard, historic yard, candidate, or source-specific type. |
| `yard_statement` | Source-scoped yard statement being preserved. |
| `source_ref` | SourceDescriptor/source registry reference. |
| `source_role` | Accepted source role; must be preserved from admission through publication. |
| `source_native_id` | Source-native yard, station, line, facility, timetable, map, roster, inventory, terminal, or asset ID. |
| `evidence_refs` | EvidenceRefs or EvidenceBundle refs. |
| `rail_segment_refs` | Rail Segment refs associated with the yard. |
| `route_membership_refs` | RouteMembership refs, if yard participates in route/corridor context. |
| `corridor_route_refs` | CorridorRoute refs associated with yard context. |
| `depot_ref` | Depot ref, if depot-adjacent relation exists. |
| `siding_refs` | Siding refs, if siding/track relations are separately supported. |
| `transport_facility_ref` | TransportFacility or Settlements/Infrastructure ref, if separately materialized. |
| `operator_assignment_refs` | OperatorAssignment refs, if separately supported. |
| `operator_status_refs` | OperatorStatus refs, if separately supported. |
| `status_event_refs` | StatusEvent refs, if service/condition changes are separately supported. |
| `restriction_refs` | AccessRestriction or RestrictionEvent refs, if separately supported. |
| `geometry_ref` | Geometry reference or generalized geometry ref. Not sufficient identity by itself. |
| `precision_statement` | Statement of supported positional precision and source limitations. |
| `valid_time` | Interval during which the source asserts the yard relation applies. |
| `source_time` | Source creation, publication, map, timetable, roster, inventory, filing, or update time. |
| `retrieval_time` | KFM retrieval/freeze time. |
| `release_time` | KFM governed release time, if released. |
| `network_node_refs` | Derived NetworkNode refs, if materialized. |
| `network_edge_refs` | Derived NetworkEdge refs, if materialized. |
| `sensitivity_label` | Sensitivity/policy tier inherited from source, location, facility, and operational context. |
| `policy_decision_ref` | PolicyDecision governing use or publication. |
| `review_ref` | ReviewRecord or steward review ref. |
| `release_manifest_ref` | ReleaseManifest for public/semi-public exposure. |
| `rollback_ref` | RollbackCard or rollback target. |
| `limitations` | Caveats: yard role claim only; not rail segment identity, facility identity, property title, switching authority, active service, graph truth, or release authority. |

---

## Invariants

1. **Yard is a rail-role claim.** It records a source-scoped yard function or relation, not the whole physical, legal, or operational object.
2. **Rail Segment is separate.** Yard may cite rail alignment or track evidence, but rail-segment identity remains in `rail_segment.md`.
3. **Facility identity is separate.** Depot, siding, terminal, facility, settlement, building, parcel, and infrastructure identity remain outside this contract where applicable.
4. **Operator/status is separate.** Operator assignment, operator status, service state, restriction, route event, and status event semantics remain separate records.
5. **Legal and safety authority is out of scope.** Yard evidence does not confer switching permission, public access, legal routing, operational authority, inspection status, or safety guidance.
6. **Source role is preserved.** Timetables, maps, railroad rosters, inventories, local histories, inspection records, OCR hits, and model outputs do not collapse into one authority posture.
7. **Graph is derived.** Network nodes/edges may derive from yard evidence but do not replace it.
8. **Publication requires gates.** Public display requires EvidenceBundle, PolicyDecision, ReviewRecord, ReleaseManifest, correction path, and RollbackCard.

---

## Yard claim families

| Claim family | Meaning | Special guardrail |
|---|---|---|
| `classification_yard_claim` | Source asserts yard used for classification, sorting, blocking, or train makeup context. | Not current operating authority or dispatching instruction. |
| `storage_yard_claim` | Source asserts storage, set-out, or layover yard function. | Not proof of active use or ownership. |
| `terminal_yard_claim` | Source asserts terminal, junction, or endpoint yard context. | Terminal/facility identity remains separate. |
| `interchange_yard_claim` | Source asserts interchange or railroad-to-railroad exchange yard function. | Operator assignment/status and legal entity truth remain separate. |
| `industry_yard_claim` | Source asserts industry/customer/service yard. | Customer, parcel, and legal identity remain separate. |
| `depot_or_station_yard_claim` | Source associates yard with depot/station context. | Depot/station identity remains separate and often settlement/infrastructure-owned. |
| `historic_yard_claim` | Historical source asserts past yard location/function. | Preserve uncertainty and avoid current-service wording. |
| `candidate_yard` | OCR, map label, model, graph, or connector proposes yard. | Candidate until reviewed; no public truth without evidence/policy gates. |
| `released_public_yard` | Yard included in a governed public rail/facility layer. | Requires release manifest and rollback target. |

---

## Source-role and time rules

Yard records must carry source role and time as core meaning.

| Rule | Requirement |
|---|---|
| Source role is fixed at admission | Promotion never turns a map label, OCR hit, timetable mention, railroad roster, inventory row, local history note, or model output into current operational truth. |
| Yard valid time is distinct | The period asserted by the source, source publication/update time, KFM retrieval time, review time, release time, and correction time are separate. |
| Current-looking label is not current service | A yard name or line on a map does not prove active service, switching authority, public access, facility condition, or safety. |
| Facility ref is not ownership transfer | A depot/siding/transport-facility ref supports context but does not move facility identity into Roads/Rail/Trade. |
| Cross-lane evidence stays cited | Settlements/Infrastructure, People/Land, Hazards, Hydrology, Archaeology/Cultural Heritage, and legal/operator sources are cited through governed refs, not absorbed. |
| Release time is explicit | Public display must cite the release artifact and rollback target. |

---

## Lifecycle

```mermaid
flowchart LR
  CONTRACT["yard.md\nsemantic meaning"] --> SCHEMA["yard.schema.json\nNEEDS VERIFICATION"]
  SOURCE["SourceDescriptor + EvidenceRef"] --> RAW["data/raw"]
  RAW --> WQ["data/work or quarantine"]
  WQ --> YARD["Yard\nsource-scoped rail-role claim"]
  YARD --> VALID["ValidationReport\nrole + time + evidence"]
  VALID --> CAT["catalog + EvidenceBundle + triplet"]
  CAT --> REVIEW["PolicyDecision + ReviewRecord"]
  REVIEW --> RELEASE["ReleaseManifest + RollbackCard"]
  RELEASE --> PUB["governed API / map / Evidence Drawer / Focus Mode"]
  YARD -. "may cite" .-> SEG["RailSegment"]
  YARD -. "may cite" .-> FAC["Depot / Siding / TransportFacility"]
  YARD -. "may support" .-> GRAPH["NetworkNode / NetworkEdge\nderived only"]
```

Contracts describe meaning. They do not move data, validate schemas, execute source reconciliation, make policy decisions, close evidence, perform review, publish artifacts, render maps, prove operational authority, or authorize AI answers.

---

## Validation

Before this contract is treated as mature, maintainers should verify:

- [ ] the ADR-selected contract/schema slug and whether this file should remain under `contracts/domains/roads-rail-trade/` or migrate to `contracts/transport/`;
- [ ] paired schema exists and includes yard type, source role, source-native ID, geometry refs, precision statement, time axes, rail-segment refs, depot/siding/facility refs, operator/status/restriction refs, evidence, policy, review, release, and rollback refs;
- [ ] fixtures cover classification yards, storage yards, terminal yards, interchange yards, industry yards, depot/station yards, historic yards, candidate yards, and released public yards;
- [ ] tests prevent yard records from proving rail segment identity, depot/siding/facility identity, property title, active service, switching authority, legal access, safety, structural condition, or operator legal identity;
- [ ] tests preserve source role and time distinctions across timetables, maps, rosters, inventories, local histories, inspection records, OCR/model candidates, and historical sources;
- [ ] tests prevent geometry-only identity collapse and require deterministic `spec_hash` posture;
- [ ] tests prove graph projections derive from yard evidence and rollback/rebuild without rewriting yard truth;
- [ ] public DTOs and map/Focus Mode payloads require EvidenceBundle, PolicyDecision, ReviewRecord, ReleaseManifest, correction path, and RollbackCard;
- [ ] rollback invalidates derived layer descriptors, graph projections, API payloads, exports, Focus Mode states, movement story nodes, caches, and AI summaries that cited the yard.

---

## Rollback

Rollback or correction is required when this contract:

- claims yard schema, policy, fixtures, tests, source registry, lifecycle data, release, API, UI, graph, operator-status, or runtime behavior exists without proof;
- hides the `roads-rail-trade` vs `transport` slug conflict;
- treats yard evidence as rail-segment truth, facility identity, legal access, switching authority, active service, safety advice, structural condition, property title, graph truth, or publication approval;
- lets a timetable note, map label, OCR hit, local history note, railroad roster, inspection record, inventory row, or modeled output become stronger authority without evidence and review;
- collapses yard, rail segment, depot, siding, transport facility, operator assignment/status, access restriction, route membership, or graph node/edge into one object;
- publishes or renders unsupported yards through maps, graph views, Focus Mode, exports, or AI narrative.

Rollback target: revert this file to prior scaffold blob SHA `751f6b130348246e23a1580276cfa2c8159e116a`, record drift if authority boundaries were affected, and invalidate downstream derivatives that cited the weakened yard contract.

---

## Evidence basis

| Evidence | Status | Supports | Limit |
|---|---|---|---|
| Prior `contracts/domains/roads-rail-trade/yard.md` | `CONFIRMED` | Target file existed as a PROPOSED scaffold. | Scaffold did not define authoritative semantic contract content. |
| `schemas/contracts/v1/domains/roads-rail-trade/yard.schema.json` lookup | `CONFIRMED not found in this task` | Justifies `schema-missing` and PROPOSED field posture. | Does not rule out alternate schema homes such as `transport/`. |
| `docs/domains/roads-rail-trade/sublanes/rail.md` | `CONFIRMED doctrine / PROPOSED rail-specific realization` | Names Depot, Siding, Yard as rail-network facility types whose canonical identity remains settlement/infrastructure-owned; separates operator/status/restriction/graph surfaces. | Does not prove schema, validator, runtime, or public API maturity. |
| `contracts/domains/roads-rail-trade/siding.md` | `CONFIRMED sibling contract` | Provides adjacent rail-role/facility-boundary pattern and separation from rail-segment identity, facility identity, property title, switching authority, active service, graph truth, and publication approval. | Siding-specific; does not define Yard schema. |
| `contracts/domains/roads-rail-trade/transport_facility.md` | `CONFIRMED sibling contract` | Provides broader facility-role boundary and separation from canonical place/facility identity, property title, structural condition, live service, legal access, and publication approval. | Broader facility-role contract; does not define Yard schema. |
| `docs/domains/roads-rail-trade/OBJECT_FAMILIES.md` | `CONFIRMED object-family spine / PROPOSED field realization` | Gives deterministic identity posture for the broader transport object-family spine and names TransportFacility as a facility family. | Yard is confirmed in README/rail sublane, but not enumerated in the fourteen-family table. |
| Uploaded authoring prompt v2 | `CONFIRMED user-supplied guidance` | Requires evidence-grounded, visually polished, implementation-honest Markdown with verification and rollback posture. | Authoring guidance, not implementation proof. |

---

## Open questions

| ID | Question | Status |
|---|---|---|
| OQ-RRT-YARD-01 | Should `yard.md` remain at `contracts/domains/roads-rail-trade/` or migrate to `contracts/transport/` after slug ADR resolution? | OPEN / ADR NEEDED |
| OQ-RRT-YARD-02 | Which yard types, source roles, geometry refs, facility refs, and operator/status refs are canonical across current, historic, depot-adjacent, siding-adjacent, terminal, interchange, and industry yard contexts? | OPEN / SCHEMA REVIEW |
| OQ-RRT-YARD-03 | What evidence threshold distinguishes a yard role claim from a rail segment, siding, depot, terminal, transport facility, or settlement/infrastructure identity? | OPEN / DOMAIN REVIEW |
| OQ-RRT-YARD-04 | Which yard details should be public, generalized, restricted, or review-only due to infrastructure, safety, property, or operational sensitivity? | OPEN / POLICY REVIEW |
| OQ-RRT-YARD-05 | How should graph nodes/edges cite yards without becoming a second canonical rail-network store? | OPEN / GRAPH REVIEW |
| OQ-RRT-YARD-06 | How should rollback invalidate maps, graph views, Focus Mode, exports, and AI summaries that cited a withdrawn yard? | OPEN / RELEASE REVIEW |

<p align="right"><a href="#top">Back to top</a></p>
