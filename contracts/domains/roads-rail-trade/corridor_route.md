<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/contracts-domains-roads-rail-trade-corridor-route
title: Corridor Route Contract — Roads / Rail / Trade Routes
type: semantic-contract
version: v0.2
status: draft; PROPOSED; schema-missing; slug-CONFLICTED; NEEDS VERIFICATION before promotion
owners:
  - OWNER_TBD — Roads/Rail/Trade Routes domain steward
  - OWNER_TBD — Roads steward
  - OWNER_TBD — Rail steward
  - OWNER_TBD — Historic/trade-routes steward
  - OWNER_TBD — Contracts steward
  - OWNER_TBD — Source steward
  - OWNER_TBD — Evidence steward
  - OWNER_TBD — Schema steward
  - OWNER_TBD — Policy steward
  - OWNER_TBD — Release steward
  - OWNER_TBD — Docs steward
created: NEEDS VERIFICATION — scaffold existed before v0.2 expansion
updated: 2026-06-23
policy_label: public; contracts; roads-rail-trade; corridor-route; route-entity; source-role-aware; temporal-scope-aware; evidence-bound; route-segment-membership-separated; graph-projection-aware; release-gated; rollback-aware; not-segment; not-route-membership; not-live-routing; not-legal-designation-authority; not-publication-authority
tags: [kfm, contracts, roads-rail-trade, corridor-route, route, route-membership, road-segment, rail-segment, historic-route, trade-route-corridor, network-edge, movement-story-node, source-role, valid-time, EvidenceBundle, PolicyDecision, ReviewRecord, ReleaseManifest, RollbackCard]
related:
  - ./README.md
  - ./trade_route_corridor.md
  - ./route_event.md
  - ./status_event.md
  - ./access_restriction.md
  - ./road_segment.md
  - ./rail_segment.md
  - ../roads/README.md
  - ../../../docs/domains/roads-rail-trade/README.md
  - ../../../docs/domains/roads-rail-trade/CANONICAL_PATHS.md
  - ../../../docs/domains/roads-rail-trade/OBJECT_FAMILIES.md
  - ../../../docs/domains/roads-rail-trade/IDENTITY_MODEL.md
  - ../../../docs/domains/roads-rail-trade/SOURCES.md
  - ../../../docs/domains/roads-rail-trade/sublanes/roads.md
  - ../../../docs/domains/roads-rail-trade/sublanes/rail.md
  - ../../../docs/domains/roads-rail-trade/sublanes/trade-routes.md
  - ../../../docs/domains/roads-rail-trade/MAP_UI_CONTRACTS.md
  - ../../../docs/domains/roads-rail-trade/GRAPH_PROJECTIONS.md
  - ../../../docs/runbooks/roads-rail-trade/PROMOTION_RUNBOOK.md
  - ../../../docs/runbooks/roads-rail-trade/ROLLBACK_RUNBOOK.md
  - ../../../schemas/contracts/v1/domains/roads-rail-trade/corridor_route.schema.json
  - ../../../policy/domains/roads-rail-trade/
  - ../../../fixtures/domains/roads-rail-trade/corridor_route/
  - ../../../tests/domains/roads-rail-trade/
  - ../../../release/candidates/roads-rail-trade/
notes:
  - "Expanded from a PROPOSED scaffold at contracts/domains/roads-rail-trade/corridor_route.md."
  - "A paired schema at schemas/contracts/v1/domains/roads-rail-trade/corridor_route.schema.json was not found in this task. Field realization remains PROPOSED."
  - "CorridorRoute is treated as the route/designation/corridor entity itself. RouteMembership attaches segments to that route under a source role and temporal scope. RoadSegment and RailSegment remain separate evidence objects."
  - "Corridor routes are evidence-bound, source-role-aware, and time-scoped. They are not live routing, legal route-designation authority, graph truth, map publication, or release approval."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Corridor Route Contract — Roads / Rail / Trade Routes

> Semantic contract for `corridor_route`: the route, corridor, designation, line, trail, or named transport entity that segments may belong to through sourced, time-scoped `RouteMembership` assertions — without collapsing the route into its segments, graph edges, map linework, or public routing authority.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Root: contracts" src="https://img.shields.io/badge/root-contracts%2F-0a7ea4">
  <img alt="Domain: roads-rail-trade" src="https://img.shields.io/badge/domain-roads--rail--trade-slategray">
  <img alt="Schema: missing" src="https://img.shields.io/badge/schema-missing-red">
  <img alt="Truth: evidence first" src="https://img.shields.io/badge/truth-evidence--first-blue">
  <img alt="Boundary: route not segment" src="https://img.shields.io/badge/boundary-route__not__segment-orange">
  <img alt="Publication: release gated" src="https://img.shields.io/badge/publication-release--gated-orange">
</p>

`contracts/domains/roads-rail-trade/corridor_route.md`

## Quick jumps

[Status](#status) · [Meaning](#meaning) · [Repo fit](#repo-fit) · [Schema posture](#schema-posture) · [Accepted uses](#accepted-uses) · [Exclusions](#exclusions) · [Recommended fields](#recommended-fields) · [Invariants](#invariants) · [Corridor route families](#corridor-route-families) · [Source-role and time rules](#source-role-and-time-rules) · [Lifecycle](#lifecycle) · [Validation](#validation) · [Rollback](#rollback) · [Evidence basis](#evidence-basis) · [Open questions](#open-questions)

---

## Status

> [!IMPORTANT]
> **Status:** `draft` / semantic contract  
> **Owner:** `OWNER_TBD`  
> **Contract path:** `contracts/domains/roads-rail-trade/corridor_route.md`  
> **Schema path:** `schemas/contracts/v1/domains/roads-rail-trade/corridor_route.schema.json` — **not found in this task**  
> **Truth posture:** target path and scaffold are confirmed from current repo evidence. `CorridorRoute` is confirmed as a Roads / Rail / Trade Routes object-family term, but exact schema fields, validator behavior, fixture coverage, policy behavior, source registry behavior, release manifests, public API behavior, map rendering, graph behavior, and runtime behavior remain **NEEDS VERIFICATION**.

> [!CAUTION]
> This contract defines corridor-route meaning only. It does **not** certify legal route designation, public accessibility, current routing suitability, emergency detour status, map/API behavior, graph truth, or publication approval.

---

## Meaning

`corridor_route` records the semantic meaning of a route or corridor as an entity in its own right.

A corridor route may represent:

- a modern road route, highway, truck route, scenic byway, detour corridor, or road designation;
- a rail line, rail corridor, service corridor, or freight corridor grouping;
- a historic route, military road, emigrant route, mail route, cattle trail, stage route, or trade corridor when the object is treated as a route/corridor entity rather than one segment;
- a generalized route corridor used by public-safe map or Focus Mode surfaces;
- a parent route that receives sourced `RouteMembership` assertions from Road Segments, Rail Segments, crossings, facilities, or historic-route claims.

A corridor route is not the same thing as a segment. A route is the thing a designation, source, or interpretation refers to; a segment is a piece of road/rail alignment evidence; membership is the sourced, temporal relationship attaching a segment to the route.

---

## Repo fit

| Responsibility | Path or root | Relationship |
|---|---|---|
| Parent contract lane | `./README.md` | Defines this folder as semantic contracts only. |
| Trade/historic corridor relation | `./trade_route_corridor.md` | Related generalized or historic corridor semantics. |
| Route events/status/restrictions | `./route_event.md`, `./status_event.md`, `./access_restriction.md` | Time-bound changes and constraints on route/corridor use. |
| Segment contracts | `./road_segment.md`, `./rail_segment.md` where present | Segment evidence remains separate from route identity. |
| Road compatibility slice | `../roads/README.md` | Road-specific orientation; not canonical authority by itself. |
| Parent doctrine | `../../../docs/domains/roads-rail-trade/README.md` | Domain scope and object roster. |
| Object families | `../../../docs/domains/roads-rail-trade/OBJECT_FAMILIES.md` | `CorridorRoute`, `RouteMembership`, `Road Segment`, `Rail Segment` vocabulary and identity posture. |
| Road sublane | `../../../docs/domains/roads-rail-trade/sublanes/roads.md` | Route/segment/membership separation for road routes. |
| Schemas | `../../../schemas/contracts/v1/domains/roads-rail-trade/` or ADR-selected alternate | Machine shape; paired schema missing in this task. |
| Policy | `../../../policy/domains/roads-rail-trade/` or ADR-selected alternate | Allow/deny/restrict/abstain decisions. |
| Fixtures/tests | `../../../fixtures/domains/roads-rail-trade/`, `../../../tests/domains/roads-rail-trade/` | Behavior proof; not contract prose. |
| Source registry | `../../../data/registry/sources/roads-rail-trade/` | Source authority, cadence, rights, and caveats. |
| Release/rollback | `../../../release/candidates/roads-rail-trade/` and release roots | Promotion, release, correction, and rollback. |

---

## Schema posture

A direct paired schema was checked at:

```text
schemas/contracts/v1/domains/roads-rail-trade/corridor_route.schema.json
```

That file was **not found** in this task.

> [!WARNING]
> Because no paired schema was confirmed, every field below is **PROPOSED** semantic guidance. Do not treat it as machine-enforced until schema, fixtures, validator, policy tests, source registry records, release checks, and runtime behavior are verified.

---

## Accepted uses

| Use | Allowed? | Rule |
|---|---:|---|
| Defining route/corridor entity semantics | Yes | Must preserve route identity separate from segment and membership. |
| Grouping segment memberships | Yes | Use sourced `RouteMembership` assertions; do not embed segment membership as route truth. |
| Modeling modern road or rail designations | Conditional | Requires source role and valid-time support for designation claims. |
| Modeling historic or trade-route corridors | Conditional | Must preserve uncertainty, claim status, and cultural/sensitivity caveats. |
| Supporting map/Focus Mode display | Conditional | Requires EvidenceBundle, PolicyDecision, release state, and rollback target. |
| Supporting graph projection | Conditional | Graph edges are derived and must cite route/segment/membership evidence. |
| Certifying legal/current route designation | No | Requires authoritative source, valid time, policy, and caveat; KFM does not issue legal opinions. |
| Acting as live routing or detour authority | No | Requires separate real-time governance; denied by default. |

---

## Exclusions

`corridor_route` must not be used as:

| Misuse | Required outcome |
|---|---|
| Road Segment or Rail Segment | Use segment contracts for alignment evidence. |
| RouteMembership | Use a membership contract/object for segment-to-route relationships. |
| NetworkEdge or graph truth | Graph projections are downstream and derived. |
| AccessRestriction or StatusEvent | Use event/restriction contracts with valid time and source role. |
| Legal route-designation certificate | `ABSTAIN` unless authoritative source and caveat are present; still not legal advice. |
| Emergency detour or live route advisory | `DENY` unless governed as a real-time route system. |
| Public map/API payload | Use governed API/released artifacts only. |
| Publication approval | ReleaseManifest and RollbackCard remain separate. |

---

## Recommended fields

The following fields are **PROPOSED** until a schema is added and validated.

| Field | Meaning |
|---|---|
| `id` | Canonical corridor route identifier. |
| `version` | Contract/object version. |
| `spec_hash` | Deterministic hash over normalized corridor route content. |
| `domain` | Expected value: `roads-rail-trade` unless ADR selects another slug. |
| `route_name` | Source-stated name or label. |
| `route_designation` | Designation such as route number, line name, trail name, historic route name, or corridor label. |
| `route_type` | Road, rail, freight, historic, trade, military, emigrant, mail, cattle, scenic, detour, generalized, or other controlled type. |
| `source_ref` | SourceDescriptor/source registry reference. |
| `source_role` | Authority/administrative/observed/context/candidate/modeled/aggregate/synthetic/restricted role, as accepted by the lane. |
| `source_native_id` | Source-native route identifier if present and safe. |
| `temporal_scope` | Source, observed, valid, retrieval, release, and correction time posture. |
| `valid_time` | Interval during which the route/designation/corridor claim is asserted to apply. |
| `membership_refs` | RouteMembership refs, not embedded segment truth. |
| `segment_summary_ref` | Optional released/generalized summary of member segments. |
| `geometry_ref` | Generalized or released route geometry, if any; not canonical membership by itself. |
| `network_projection_refs` | Downstream NetworkEdge/graph refs, if any. |
| `historic_claim_refs` | Historic RouteClaim or TradeRouteCorridor refs, if applicable. |
| `evidence_refs` | EvidenceRefs or EvidenceBundle refs. |
| `policy_decision_ref` | PolicyDecision governing use or publication. |
| `review_ref` | ReviewRecord or steward review ref. |
| `release_manifest_ref` | ReleaseManifest for public/semi-public exposure. |
| `rollback_ref` | RollbackCard or rollback target. |
| `limitations` | Caveats: route not segment; membership separate; graph/map not truth; no live/legal routing authority. |

---

## Invariants

1. **Route is not segment.** A CorridorRoute cannot replace Road Segment or Rail Segment evidence.
2. **Membership is separate.** Segment-to-route inclusion belongs in RouteMembership with source role and valid time.
3. **Designation is source-scoped.** Route name, number, corridor label, or historic name must preserve source role and time scope.
4. **Geometry is derivative.** A route line or corridor geometry is a released/generalized representation, not the membership truth itself.
5. **Graph output is derived.** NetworkEdge and route traversal outputs cannot replace CorridorRoute, Segment, or RouteMembership records.
6. **Historic routes remain claims unless reviewed.** Historic/trade-route corridors must preserve uncertainty, evidence, sensitivity, and review status.
7. **Legal/live authority is denied by default.** KFM does not issue live routing, detour, legal designation, or permit advice through this contract.
8. **Release is separate.** Public surfaces require EvidenceBundle, PolicyDecision, review where required, ReleaseManifest, and RollbackCard.

---

## Corridor route families

| Family | Example | Boundary |
|---|---|---|
| Modern road route | Highway, county route, truck route, scenic byway. | Requires source-role support; not live routing/legal advice. |
| Modern rail route/line | Railroad line, branch, corridor, service route. | Operator status and rail segment evidence remain separate. |
| Freight corridor | Freight/logistics corridor grouping. | Corridor context is not raw movement proof. |
| Historic route | Military road, emigrant road, mail route, stage route, cattle trail. | Historical claim/corridor; not modern route status. |
| Trade route corridor | Generalized trade or movement corridor. | May require cultural sensitivity and generalized geometry. |
| Detour/temporary corridor | Temporary alternate route or construction detour. | Requires freshness and source cadence; not live advice by default. |
| Public-safe map corridor | Released generalized line/corridor for UI. | Requires release/caveat; not canonical membership truth. |

---

## Source-role and time rules

| Rule | Required behavior |
|---|---|
| Authority is source-bound | Agency, railroad, county, historical map, newspaper, OSM, GNIS, atlas, field observation, and modeled source roles must remain distinct. |
| Route designation needs source role | A label or number does not become legal route designation without role-appropriate source support. |
| Membership needs valid time | Segment inclusion must be time-scoped through RouteMembership when available. |
| Historic route needs caveat | Historic/trade route corridors must carry uncertainty, evidence limits, and sensitivity posture. |
| Geometry does not define membership | A line drawn through segments is not sufficient to prove route membership. |
| Times stay distinct | Source, observed, valid, retrieval, release, and correction times must not collapse into one date. |
| Corrections propagate | Route rename, redesignation, decommissioning, split, merge, or demotion must invalidate dependent memberships, graph edges, layers, exports, and AI summaries. |

---

## Lifecycle

```mermaid
flowchart TD
  SRC["Route/corridor source\nagency · railroad · map · atlas · historic source · model · context source"] --> RAW["RAW / WORK / QUARANTINE"]
  RAW --> NORM["Normalize CorridorRoute claim\nsource role + route type + valid time"]
  NORM --> CHECK{"schema + source role + evidence + policy + membership separation + release checks"}
  CHECK -->|fail| HOLD["HOLD / DENY / ABSTAIN / QUARANTINE"]
  CHECK -->|pass| PROC["PROCESSED CorridorRoute"]
  PROC --> CAT["CATALOG / TRIPLET\nEvidenceBundle refs"]
  CAT --> REVIEW["ReviewRecord + PolicyDecision"]
  REVIEW -->|approved| REL["ReleaseManifest + RollbackCard"]
  REVIEW -->|denied| DENY["DENY public use"]
  REL --> PUB["PUBLISHED public-safe derivative"]
  PROC -. attaches through .-> RM["RouteMembership\nsource-scoped + valid-time"]
  PROC -. derived .-> GRAPH["NetworkEdge / graph route\nDERIVED ONLY"]
  PROC -. correction .-> ROLLBACK["CorrectionNotice / RollbackCard"]
```

---

## Validation

Minimum validation expectations before promotion:

- [ ] paired schema exists or schema gap remains explicit;
- [ ] source role resolves to an admitted source registry record;
- [ ] CorridorRoute, Road/Rail Segment, RouteMembership, NetworkEdge, StatusEvent, and AccessRestriction are not collapsed;
- [ ] route designation/name/source-native ID preserve source context;
- [ ] valid/source/retrieval/release/correction times are separate;
- [ ] route geometry is labeled derivative/generalized/released and not membership truth;
- [ ] public layer/API/export requires EvidenceBundle, PolicyDecision, ReviewRecord, ReleaseManifest, and RollbackCard;
- [ ] graph projection uses route only as derived traversal/grouping evidence and cites source records;
- [ ] live routing, legal designation, permit, detour, and emergency advice are denied by default.

Negative fixtures should include:

- route name treated as legal designation without authority;
- geometry line treated as membership proof;
- RouteMembership embedded directly into CorridorRoute with no source/time;
- Road Segment identity collapsed into route identity;
- historic route corridor shown as modern road route;
- graph path emitted as canonical corridor truth;
- public layer missing ReleaseManifest or RollbackCard;
- stale detour/current route rendered as live routing advice.

---

## Rollback

Rollback or correction is required when:

- source role, route name, designation, source-native ID, route type, valid time, membership refs, geometry, or release caveat was wrong;
- a route was presented as legal/current/routing/emergency authority without support;
- geometry or graph output was used as membership truth;
- historic/trade-route uncertainty or sensitivity was removed;
- public map/API/export output leaked stale or unsupported route status;
- graph edges, route memberships, restrictions, status events, or AI summaries depended on an invalid route claim;
- ReleaseManifest, PolicyDecision, EvidenceBundle, source registry, or rollback target was missing or later corrected.

Rollback must identify affected route refs, membership refs, segment refs, graph derivatives, map layers, API/cache/export artifacts, AI summaries, release manifests, reason code, replacement/tombstone refs, and public correction notice if required.

---

## Evidence basis

| Evidence | Supports | Limit |
|---|---|---|
| `contracts/domains/roads-rail-trade/corridor_route.md` scaffold | Target file existed and was a planned PROPOSED scaffold. | Scaffold contained no semantic contract. |
| Missing direct schema check | A direct paired schema at `schemas/contracts/v1/domains/roads-rail-trade/corridor_route.schema.json` was not found in this task. | Does not rule out alternate `transport` schema path; slug conflict remains. |
| `docs/domains/roads-rail-trade/OBJECT_FAMILIES.md` | Confirms `CorridorRoute` and `RouteMembership`, with route as grouping and membership as associative object. | Field realization remains PROPOSED. |
| `docs/domains/roads-rail-trade/sublanes/roads.md` | Confirms modern roads include RouteMembership and CorridorRoute, and states route is an entity distinct from a segment. | Sublane convention remains PROPOSED / NEEDS VERIFICATION. |
| `contracts/domains/roads-rail-trade/README.md` | Contract-lane boundary and separation from schemas, policy, data, release, APIs, and map/runtime behavior. | Draft; slug conflict unresolved. |

---

## Open questions

| ID | Question | Status |
|---|---|---|
| OQ-RRT-CORRIDOR-01 | Is `CorridorRoute` the canonical route entity name for both modern road/rail routes and historic/trade corridors, or should historic corridors use separate contracts only? | OPEN / ADR NEEDED |
| OQ-RRT-CORRIDOR-02 | Which schema path wins for this object: `schemas/contracts/v1/domains/roads-rail-trade/`, `schemas/contracts/v1/transport/`, or another ADR-selected home? | OPEN / ADR NEEDED |
| OQ-RRT-CORRIDOR-03 | Which source families are authoritative for route designation, route renaming, decommissioning, and membership? | OPEN / SOURCE STEWARD REVIEW |
| OQ-RRT-CORRIDOR-04 | What geometry representation is allowed for public historic/trade routes without overstating certainty or sensitivity? | OPEN / POLICY REVIEW |
| OQ-RRT-CORRIDOR-05 | How should route corrections invalidate memberships, graph edges, map layers, exports, and AI summaries? | OPEN / ROLLBACK TEST NEEDED |

[Back to top](#top)
