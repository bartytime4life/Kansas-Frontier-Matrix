<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/dashboards-domain-roads-rail-trade
title: Roads / Rail / Trade Routes Dashboard Specification
type: standard
version: v0.2.0
status: draft
owners: "@bartytime4life (CODEOWNERS review route); Roads/Rail/Trade, source/evidence, policy/sensitivity, UI/metric, correction, and release stewards NEEDS VERIFICATION"
created: 2026-05-26
updated: 2026-08-21
policy_label: public
owning_root: docs/
responsibility: Dashboard specification and review guidance only; not source, evidence, policy, runtime, release, deployment, or publication authority.
truth_posture: CONFIRMED current repository evidence / PROPOSED indicators and runtime bindings / UNKNOWN deployed dashboard and production telemetry / NEEDS VERIFICATION positive domain-health claims
related:
  - ./README.md
  - ../README.md
  - ../DASHBOARD_CATALOG.md
  - ../operational/SLO_LIVE_FEEDS.md
  - ../operational/REALTIME_FEED_FRESHNESS.md
  - ../../domains/roads-rail-trade/README.md
  - ../../../contracts/domains/roads-rail-trade/corridor_route.md
  - ../../../schemas/contracts/v1/domains/roads-rail-trade/corridor_route.schema.json
  - ../../../schemas/contracts/v1/domains/roads-rail-trade/frontier_route_trust_status.schema.json
  - ../../../policy/domains/roads-rail-trade/README.md
tags: [kfm, dashboards, domain, roads, rail, trade-routes, transport, evidence, trust-projection, governance-health, specification]
notes:
  - Same-path modernization of the Roads / Rail / Trade Routes dashboard specification; no dashboard route, source admission, policy activation, release, deployment, or publication is created.
  - Current repository evidence confirms bounded, synthetic CorridorRoute and FrontierRouteTrustStatus validation plus shared Evidence Drawer convergence and a pure Explorer trust-overlay helper; broader domain validation, active policy, proof, release, and production telemetry remain held or unverified.
  - Current-status, closure, detour, safe-passage, legal-access, bridge-condition, rail-status, and operational-navigation claims remain outside this dashboard's authority.
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Roads / Rail / Trade Routes Dashboard Specification

A repository-grounded specification for a review-facing Roads / Rail / Trade
Routes dashboard that reports evidence, source-role, validation, public-safety,
correction, and release posture without becoming route truth, policy, operating
authority, or publication authority.

> [!IMPORTANT]
> **Current status.** Repository evidence confirms one bounded,
> fixture-first `CorridorRoute` semantic-validation slice, one closed
> `FrontierRouteTrustStatus` projection with deterministic negative fixtures, a
> pure Explorer trust-overlay helper, and a shared Evidence Drawer convergence
> seam. It does **not** confirm an admitted Roads/Rail/Trade source descriptor,
> executable live connector, active policy evaluator, routed dashboard,
> production telemetry, emitted proof, release candidate, deployment, or
> publication.

> [!CAUTION]
> **This dashboard is not operational transportation guidance.** It must not
> present current navigation, closure, detour, safe-passage, legal-access,
> bridge-condition, rail-status, emergency, dispatch, regulatory, or operating
> instructions. Those claims require current competent-authority evidence and
> separate policy, review, release, and public-safety controls.

> [!NOTE]
> Live-feed service health belongs in
> [`SLO_LIVE_FEEDS.md`](../operational/SLO_LIVE_FEEDS.md) and
> [`REALTIME_FEED_FRESHNESS.md`](../operational/REALTIME_FEED_FRESHNESS.md).
> This domain specification may compose a released transport-feed roll-up later;
> it does not duplicate those operational contracts or imply that a live feed is
> admitted today.

## Contents

1. [Domain scope](#1-domain-scope)
2. [Indicator subset](#2-indicator-subset)
3. [Domain-specific indicators](#3-domain-specific-indicators-proposed)
4. [Ownership](#4-ownership)
5. [Implementation pointer](#5-implementation-pointer)
6. [Review cadence](#6-review-cadence)
7. [Open questions](#7-open-questions)
8. [Evidence basis and citations](#8-evidence-basis--citations)

---

<a id="1-domain-scope"></a>

## 1. Domain scope

The dashboard covers aggregate governance-health posture for modern and historic
roads, rail, trade routes, transport facilities, restrictions, route events,
operator assertions, derived graph projections, public-safe map carriers, and
their correction and release dependencies.

It may report:

- source-registry, rights, source-role, cadence, and evidence-closure state;
- deterministic validation outcomes for bounded transport contracts and
  projections;
- separation of route, segment, membership, geometry, operator, restriction,
  facility, and graph-projection meanings;
- audience-safe trust projections and Evidence Drawer convergence;
- proof, release, correction, withdrawal, and rollback readiness;
- stale, incomplete, conflicting, held, denied, and error states; and
- documentation, contract/schema slug, registry-topology, and implementation
  drift.

It must not:

- treat a source-registry README, connector README, fixture, schema, test,
  workflow, badge, map layer, graph edge, AI summary, or dashboard card as
  transport truth;
- upgrade context, aggregate, community, modeled, derived, or historic-corpus
  material into current official authority;
- collapse `CorridorRoute`, `RoadSegment`, `RailSegment`, `RouteMembership`,
  embedded geometry, `NetworkEdge`, or a rendered line into one object;
- infer current road, rail, crossing, bridge, operator, access, or restriction
  status from stale or non-authoritative support;
- expose restricted geometry, private-access context, sensitive facilities,
  cultural corridors, archaeology, living-person or land information, or
  over-precise historic-route reconstructions;
- read RAW, WORK, QUARANTINE, PROCESSED, CATALOG, TRIPLETS, internal registries,
  or unreviewed candidate stores directly from an ordinary public client; or
- interpret a green workflow, pull request, merge, or rendered panel as
  promotion, release, deployment, or publication.

### Source-role and cross-lane boundaries

The dashboard preserves the owning domain and source role for every relationship:

| Context | Roads/Rail/Trade may display | Authority that remains elsewhere |
|:---|:---|:---|
| Settlements and infrastructure | Transport function, route relationship, and released public-safe facility context | Physical asset and settlement identity |
| Hydrology | Released water-crossing and corridor context | Waterbody, flow, flood, and hydrologic evidence |
| Hazards | Released hazard context affecting a transport claim | Alert, warning, emergency, and hazard-event authority |
| Archaeology and cultural heritage | Generalized, reviewed historic-route relationship | Site identity, exact location, sovereignty, and cultural sensitivity |
| People, land, and title | Released aggregate context where policy permits | Living-person, ownership, title, and private-access truth |
| Agriculture and trade | Released corridor and movement context | Farm, commodity, transaction, operator, and proprietary truth |

A cross-lane relation is a cited, time-scoped, policy-reviewed relationship. It
does not transfer source authority or ownership.

[↑ Back to top](#top)

---

<a id="2-indicator-subset"></a>

## 2. Indicator subset

These indicators are bounded dashboard specifications. They do not create a
metric producer, telemetry source, executable policy, review decision, proof, or
release.

| ID | Indicator | Computation and healthy posture | Governed input | Current repository state |
|:---|:---|:---|:---|:---|
| `RRT-DB-01` | Source-admission closure | Report required source families by `ADMITTED`, `HELD`, `DENIED`, `WITHDRAWN`, or `UNKNOWN`, with rights, role, time, and correction completeness. Never calculate a positive coverage rate from README presence. | SourceDescriptor and activation records from the accepted source registry | **HOLD:** [`data/registry/sources/roads-rail-trade/`](../../../data/registry/sources/roads-rail-trade/README.md) and [`connectors/domains/roads-rail-trade/`](../../../connectors/domains/roads-rail-trade/README.md) contain boundary documentation and `.gitkeep`, not admitted descriptors or executable connectors. |
| `RRT-DB-02` | `CorridorRoute` validation disposition | Count deterministic `PASS`, `ABSTAIN`, `DENY`, and `ERROR` outcomes by safe reason family while preserving route identity, date uncertainty, geometry accuracy, source role, evidence state, confidence, and change state. | `CorridorRoute` contract, schema, validator, fixtures, and validation report | **PARTIAL / FIXTURE-ONLY:** the bounded profile exists; it does not establish real-route truth, source admission, policy approval, legal designation, routing authority, or release. |
| `RRT-DB-03` | Route/segment/membership/graph anti-collapse | Count rejected candidates that merge distinct object families or promote derived geometry/graph output to canonical truth. Healthy posture is zero accepted anti-collapse violations, with denominator and test scope visible. | Contract/schema findings, fixture polarity, graph-projection validation | **PARTIAL:** `CorridorRoute` negative checks exist; broader RoadSegment, RailSegment, RouteMembership, facility, event, restriction, and NetworkEdge schemas remain candidate backlog or scaffolds. |
| `RRT-DB-04` | Trust-projection integrity | Report schema and cross-field results for unique `kfm_id`, decision/visibility parity, release binding, collection-decision consistency, bounded input, and public/steward audience separation. | `FrontierRouteTrustStatus` validator output and immutable fixture snapshot | **PARTIAL / FIXTURE-ONLY:** closed schema, validator, fixtures, Python tests, Explorer tests, and a read-only workflow exist. No production projection or authenticated upstream decision is verified. |
| `RRT-DB-05` | Public-audience release protection | Numerator: public projection entries with `decision=publish`, public-catalog visibility, non-null release identity, and governed evidence/policy references. Denominator: all eligible public entries in the same immutable snapshot. Any unresolved or non-publish entry is excluded upstream, not hidden in the browser. | Public-safe trust projection and Explorer trust-overlay result | **PARTIAL:** pure TypeScript helpers fail closed and are fixture-tested; no routed layer, production payload, live store, or released route collection is verified. |
| `RRT-DB-06` | Evidence Drawer convergence | Report whether claim-bearing transport payloads use the shared closed Evidence Drawer schema and shared renderer with finite `ANSWER`, `ABSTAIN`, `DENY`, or `ERROR` outcomes. | Domain projection schema, shared UI schema, shared Evidence Drawer adapter, convergence test | **PARTIAL:** the domain component delegates to the shared renderer and deterministic convergence tests exist; no dashboard route or production EvidenceBundle resolution is verified. |
| `RRT-DB-07` | Proof, release, correction, and rollback readiness | Show explicit `HOLD` until an emitted proof, candidate identity, immutable artifact pointer, EvidenceBundle closure, policy/review records, correction path, and rollback target exist. Absence of a failure is not readiness. | Domain workflow, proof inventory, release candidate inventory, correction and rollback records | **CONFIRMED HOLD:** proof and candidate directories contain only boundary README material (plus `.gitkeep` where applicable), and the domain workflow explicitly records proof and release-dry-run holds. |
| `RRT-DB-08` | Authority and path drift | Report unresolved `roads-rail-trade` versus `transport`, domain-nested versus flat schema/contract, hyphen versus underscore app-path, and subtype-first versus domain-first registry relationships without choosing a winner in presentation code. | Accepted ADRs, Directory Rules, path/alias registers, domain docs, drift register | **CONFLICTED / OPEN:** current files expose the naming and topology tensions; this dashboard does not authorize migration, alias acceptance, or parallel writable authority. |

### Measurement envelope

Every displayed measurement should carry, or resolve to, the following fields:

| Field | Requirement |
|:---|:---|
| Metric identity | Stable indicator ID and specification version. |
| Snapshot identity | Immutable run, report, projection, or artifact reference; never an unqualified “latest.” |
| Time | Observation, valid/effective, retrieval, calculation, release, and correction time where material. |
| Population | Explicit numerator, denominator, exclusions, and completeness state. |
| Source role | Authority, official, administrative, observed, context, aggregate, modeled, synthetic, or derived role as accepted by the governing vocabulary. |
| Evidence | EvidenceRefs and audience-appropriate EvidenceBundle resolution state. |
| Decision state | Validator outcome, policy result, review state, and release state kept as separate fields. |
| Audience and sensitivity | Public, steward, or other accepted audience plus generalization, restriction, and rights posture. |
| Correction | Supersession, withdrawal, CorrectionNotice, invalidation scope, and rollback target. |
| Presentation state | `AVAILABLE`, `NO_DATA`, `STALE`, `INCOMPLETE`, or `ERROR` as proposed UI states, separate from policy and validator outcomes. |

When the denominator or snapshot is incomplete, the dashboard withholds a
percentage and displays `INCOMPLETE` or `NO_DATA`. When current authority,
rights, policy, evidence, or release state is unresolved, the dashboard displays a
bounded hold, abstention, denial, or error rather than a reassuring default.

[↑ Back to top](#top)

---

<a id="3-domain-specific-indicators-proposed"></a>

## 3. Domain-specific indicators (PROPOSED)

The following candidates require an accepted metric contract and a verified
producer before runtime use:

| Candidate | Purpose | Minimum dependency | Safe failure behavior |
|:---|:---|:---|:---|
| Historic-route edition and uncertainty closure | Identify claims that lack a pinned corpus edition, method, geometry-accuracy statement, date uncertainty, confidence, or supersession link. | Admitted source descriptor, `CorridorRoute` contract, immutable source snapshot, evidence and correction lineage. | `INCOMPLETE` or `ABSTAIN`; never draw a precise line from weak or conflicting support. |
| Current-status authority and freshness | Detect road, rail, bridge, crossing, operator, access, or restriction claims whose source-valid time or competent authority is missing or stale. | Accepted current-status contract, official authority source, freshness policy, valid-time semantics, and release binding. | `STALE`, `HOLD`, or `DENY`; never imply live operating guidance. |
| Transport-feed SLO composition | Roll up released agency-feed service health without duplicating operational SLO definitions. | Verified admitted feed plus the contracts in [`SLO_LIVE_FEEDS.md`](../operational/SLO_LIVE_FEEDS.md) and [`REALTIME_FEED_FRESHNESS.md`](../operational/REALTIME_FEED_FRESHNESS.md). | `NO_DATA` or `HOLD`; no agency or feed is named as active without registry and runtime evidence. |
| Graph-projection divergence | Detect a NetworkEdge or graph path whose source objects, evidence, time, policy, or release identity no longer match the projection. | Accepted graph contract, deterministic projection receipt, source-object hashes, and invalidation map. | Remove the projection from eligible presentation and open correction review. |
| Cross-lane ownership integrity | Count relations that overwrite settlement, infrastructure, hydrology, hazards, archaeology, people/land, agriculture, or trade authority. | Cross-lane relation contract, owner-domain references, EvidenceBundle and policy checks. | `DENY` the relation projection; preserve each owning lane. |
| Public geometry and attribute protection | Verify that public route/facility carriers contain only reviewed, release-approved geometry and attributes and cannot reconstruct restricted access, sensitive infrastructure, cultural routes, or private activity. | Public-safe profile, policy decision, transformation receipt, adversarial fixtures, review and release record. | `DENY` the carrier before client delivery; expose no transform secret or protected detail. |
| Correction-cascade completeness | Measure whether a correction or withdrawal invalidates affected projections, catalogs, layers, caches, exports, stories, Evidence Drawer payloads, and AI receipts. | CorrectionNotice, dependency graph, release manifest, invalidation receipt, and rollback exercise. | Mark downstream surfaces `STALE` or withdrawn until closure is proven. |

[↑ Back to top](#top)

---

<a id="4-ownership"></a>

## 4. Ownership

| Responsibility | Current disposition |
|:---|:---|
| Repository review route | **CONFIRMED:** the default [`CODEOWNERS`](../../../.github/CODEOWNERS) route is `@bartytime4life`. Routing does not prove stewardship, review, or approval. |
| Roads / Rail / Trade domain steward | **NEEDS VERIFICATION:** no accountable identity is assigned by this specification. |
| Source and evidence steward | **NEEDS VERIFICATION:** required for source role, rights, cadence, authority, and EvidenceBundle closure. |
| Policy and sensitivity reviewer | **NEEDS VERIFICATION:** required before current-status, access, restricted-geometry, infrastructure, cultural-route, or public-safe claims. |
| Governance-health / metric steward | **NEEDS VERIFICATION:** required to approve metric meaning, populations, time windows, completeness states, and correction behavior. |
| Explorer / dashboard owner | **NEEDS VERIFICATION:** bounded Explorer helper files exist, but no routed dashboard owner or telemetry producer is confirmed. |
| Correction and release stewards | **NEEDS VERIFICATION:** required for withdrawal, invalidation, rollback, candidate review, and release decisions. |
| Independent reviewer | **NEEDS VERIFICATION:** generator, author, repository reviewer, policy reviewer, and release approver are not assumed to be the same role. |

No documentation author, generated receipt, workflow, or dashboard surface may
self-approve a policy-significant change.

[↑ Back to top](#top)

---

<a id="5-implementation-pointer"></a>

## 5. Implementation pointer

### Current repository evidence

| Surface | Verified state | Boundary |
|:---|:---|:---|
| [`docs/domains/roads-rail-trade/README.md`](../../domains/roads-rail-trade/README.md) | Detailed draft domain dossier and cross-lane boundary. | Human doctrine; some path descriptions are stale or conflicted and do not prove runtime. |
| [`corridor_route.md`](../../../contracts/domains/roads-rail-trade/corridor_route.md), [schema](../../../schemas/contracts/v1/domains/roads-rail-trade/corridor_route.schema.json), [validator](../../../tools/validators/domains/roads-rail-trade/validate_corridor_route.py), and [test](../../../tests/schemas/test_corridor_route_contract.py) | One bounded, synthetic `CorridorRoute` contract/schema/validator profile. | Fixture-only; no live source, route truth, legal designation, policy approval, release, or publication. |
| [`domain-roads-rail-trade.yml`](../../../.github/workflows/domain-roads-rail-trade.yml) | Read-only no-network readiness and CorridorRoute validation definition; explicit broader-validation, proof, and release holds. | Workflow definition and any passing run are not truth, policy, proof, release, or publication authority. |
| [`frontier_route_trust_status.schema.json`](../../../schemas/contracts/v1/domains/roads-rail-trade/frontier_route_trust_status.schema.json), [validator](../../../tools/validators/domains/roads-rail-trade/validate_frontier_route_trust_status.py), [Python test](../../../tests/validators/test_validate_frontier_route_trust_status.py), and [workflow](../../../.github/workflows/frontier-route-trust-status.yml) | Closed, deterministic, no-network trust-projection profile with exact positive and negative fixture polarity. | Carries already-governed dispositions only; it does not calculate policy, resolve evidence, authenticate review, or authorize release. |
| [`layers.ts`](../../../apps/explorer-web/src/features/domains/roads_rail_trade/layers.ts) and [Explorer test](../../../apps/explorer-web/tests/frontier-routes-trust-overlay.test.ts) | Pure audience-aware `kfm_id` join, fail-closed public filtering, and deterministic style-expression helpers. | No fetch, dashboard route, source access, policy calculation, release, or publication. |
| [`EvidenceDrawer.tsx`](../../../apps/explorer-web/src/features/domains/roads_rail_trade/EvidenceDrawer.tsx), [domain schema](../../../schemas/contracts/v1/domains/roads-rail-trade/evidence_drawer_payload.schema.json), [test](../../../tests/validators/domains/roads-rail-trade/test_evidence_drawer_convergence.py), and [workflow](../../../.github/workflows/roads-rail-trade-evidence-drawer-convergence.yml) | Domain adapter delegates to the shared closed Evidence Drawer renderer and finite shared payload. | Confirms convergence seam only, not a routed dashboard or production EvidenceBundle lookup. |
| [`policy/domains/roads-rail-trade/README.md`](../../../policy/domains/roads-rail-trade/README.md) | Repository-grounded inventory of 16 Rego stubs/scaffolds and evaluator/review/consumer gaps. | No active policy bundle, authenticated decision, native rule coverage, governed consumer, or production enforcement. |
| [`data/registry/sources/roads-rail-trade/`](../../../data/registry/sources/roads-rail-trade/README.md) and [`connectors/domains/roads-rail-trade/`](../../../connectors/domains/roads-rail-trade/README.md) | Registry and connector boundary documentation. | No admitted descriptor instance or executable connector is present in those directories at the inspected tree. |
| [`data/proofs/roads-rail-trade/`](../../../data/proofs/roads-rail-trade/README.md) and [`release/candidates/roads-rail-trade/`](../../../release/candidates/roads-rail-trade/README.md) | Proof and candidate boundary documentation. | No emitted domain proof or candidate record is present at the inspected tree. |

### Proposed governed read path

```text
admitted source + immutable source snapshot
  -> validated domain candidate
  -> EvidenceRef / EvidenceBundle resolution
  -> policy and review decision
  -> proof / release / correction / rollback closure
  -> governed public-safe projection
  -> Explorer trust overlay and shared Evidence Drawer
  -> dashboard metric snapshot
```

No dashboard route, metric store, telemetry adapter, current-status source,
production EvidenceBundle resolver, or released transport collection was confirmed
in this update.

[↑ Back to top](#top)

---

<a id="6-review-cadence"></a>

## 6. Review cadence

Use event-driven review rather than an unsupported fixed calendar interval.
Review this specification when:

- an accepted source descriptor, live connector, feed, corpus edition, or source
  role changes;
- the route, segment, membership, facility, restriction, status, graph, trust
  projection, Evidence Drawer, or metric contract changes;
- the contract/schema slug, app-path grammar, registry topology, or accepted
  Directory Rules/ADR posture changes;
- a policy bundle, evaluator, authenticated decision, reviewer assignment, or
  governed consumer is introduced;
- a proof producer, release candidate, correction path, rollback target, public
  layer, dashboard route, metric producer, export, or AI surface is added; or
- an incident, source correction, withdrawal, stale-state event, or rollback
  reveals misleading, unsafe, or incomplete dashboard behavior.

### Repository-defined focused checks

```bash
python tools/validators/docs/link-check/check_links.py \
  --repo-root . \
  --format text \
  docs/dashboards/domain/roads-rail-trade.md
```

```bash
KFM_NO_NETWORK=1 PYTHONHASHSEED=0 TZ=UTC \
  python tools/validators/domains/roads-rail-trade/validate_corridor_route.py \
  --fixtures
```

```bash
KFM_NO_NETWORK=1 PYTHONHASHSEED=0 TZ=UTC \
  python -m unittest -q \
  tests.validators.test_validate_frontier_route_trust_status
```

```bash
pnpm --filter explorer-web exec vitest run \
  tests/frontier-routes-trust-overlay.test.ts
```

```bash
KFM_NO_NETWORK=1 PYTHONHASHSEED=0 TZ=UTC \
  python -m unittest discover \
  -s tests/validators/domains/roads-rail-trade \
  -p 'test_evidence_drawer_convergence.py' \
  -q
```

These commands are repository-defined validation surfaces. This documentation
change does not claim they were executed locally. Passing them proves only their
bounded contracts; it does not admit sources, activate policy, establish route or
operational truth, produce proof, approve release, deploy, or publish.

[↑ Back to top](#top)

---

<a id="7-open-questions"></a>

## 7. Open questions

- [ ] **OPEN-DASH-RRT-01 — Runtime and metric contract.** Which accepted
  dashboard route, metric-record contract, immutable snapshot identity, query
  producer, access control, and telemetry store will supply this surface?
- [ ] **OPEN-DASH-RRT-02 — Path and alias authority.** Which accepted decision
  resolves `roads-rail-trade` versus `transport`, domain-nested versus flat
  contract/schema paths, hyphen/underscore app naming, and source-registry
  topology without creating parallel writable authority?
- [ ] **OPEN-DASH-RRT-03 — Source admission.** Which source descriptors are
  actually admitted, rights-cleared, current, correction-aware, and suitable for
  historic, modern, regulatory, operational, or contextual claims?
- [ ] **OPEN-DASH-RRT-04 — Policy activation.** Which bundle, evaluator,
  authenticated finite outcome, reason-code vocabulary, obligation contract,
  receipt, and governed consumer make Roads/Rail/Trade policy operational?
- [ ] **OPEN-DASH-RRT-05 — Proof and release closure.** Which proof producer,
  candidate manifest, review record, release manifest, correction notice,
  invalidation map, and rollback exercise close the first public-safe slice?
- [ ] **OPEN-DASH-RRT-06 — Current-status authority.** What competent official
  source and freshness policy may support closures, restrictions, access,
  bridge conditions, operator status, or rail service without turning KFM into
  operating guidance?
- [ ] **OPEN-DASH-RRT-07 — Historic-route and sensitive-context review.** Which
  uncertainty, generalization, sovereignty, cultural-route, archaeology,
  private-access, infrastructure, and anti-reconstruction rules govern public
  geometry and attributes?
- [ ] **OPEN-DASH-RRT-08 — Operational SLO composition.** Which verified
  transport feeds, if any, may be rolled up from the operational dashboard
  contracts, and which steward owns their SLO and correction semantics?

[↑ Back to top](#top)

---

<a id="8-evidence-basis--citations"></a>

## 8. Evidence basis & citations

<details>
<summary><strong>Repository evidence ledger</strong></summary>

| Evidence | Status | Supports | Does not support |
|:---|:---|:---|:---|
| `main@b820a8a938db741018289c6131477f2ceaa052fc` | **CONFIRMED pinned repository snapshot** | Target bytes and all repository surfaces linked above. | Runtime behavior, current external facts, or future branch state. |
| [`docs/dashboards/README.md`](../README.md), [`domain/README.md`](./README.md), and [`DASHBOARD_CATALOG.md`](../DASHBOARD_CATALOG.md) | **CONFIRMED documentation lane** | Dashboard-spec boundary, placement hold, catalog relationship, and runtime non-authority. | A running dashboard, accepted metric, or release. |
| [`docs/domains/roads-rail-trade/README.md`](../../domains/roads-rail-trade/README.md) and contract/schema indexes | **CONFIRMED repository docs** | Domain scope, object families, source-role/cross-lane boundaries, and disclosed path conflicts. | Field-complete implementation or accepted path resolution. |
| CorridorRoute contract/schema/validator/fixtures/tests/workflow | **CONFIRMED bounded implementation surface** | Deterministic fixture-first semantics and negative proof for one object profile. | Real-route truth, source admission, policy, legal designation, routing, proof, or release. |
| FrontierRouteTrustStatus schema/validator/fixtures/tests/workflow and Explorer helper | **CONFIRMED bounded implementation surface** | Closed trust projection, cross-field validation, audience separation, deterministic joins, and fail-closed public filtering. | Authenticated upstream policy/review, production projection, layer route, or public release. |
| Evidence Drawer projection/component/test/workflow | **CONFIRMED convergence seam** | Shared closed schema and shared renderer delegation. | Production EvidenceBundle resolution or routed dashboard behavior. |
| Policy README and domain workflow holds | **CONFIRMED boundary evidence** | Inactive scaffold posture plus explicit broader-validation, proof, and release holds. | Active policy, full test coverage, proof, release, deployment, or publication. |
| Source-registry, connector, proof, and release-candidate directory listings | **CONFIRMED inventory evidence** | Boundary README and `.gitkeep`/README-only states at the pinned tree. | Admitted sources, executable connectors, emitted proofs, candidate records, or publication. |
| [`CODEOWNERS`](../../../.github/CODEOWNERS) and [ADR-0029](../../adr/ADR-0029-adopt-directory-governance-standard-v2.md) | **CONFIRMED review-route and placement authority** | `@bartytime4life` review routing and accepted Directory Rules v2 authority. | Independent stewardship, review occurrence, policy approval, release approval, or publication. |

</details>

### Truth-label summary

- **CONFIRMED:** existing target path; current repository snapshot; bounded
  CorridorRoute, trust-projection, Explorer overlay, and Evidence Drawer
  convergence files; inactive policy inventory; explicit proof/release holds;
  empty source-descriptor/connector/proof/candidate implementation lanes as
  described above; CODEOWNERS route; accepted Directory Rules decision.
- **PROPOSED:** metric definitions, calculations, presentation states, owners,
  dashboard route, telemetry, review triggers, and future operational
  composition.
- **UNKNOWN:** production sources, effective policy evaluation, routed
  dashboard, live metric population, authenticated review, emitted proof,
  release parity, deployment, and publication.
- **NEEDS VERIFICATION:** every positive domain-health claim before use, all
  accountable steward identities, current external source authority and rights,
  public-safe geometry/attribute policy, correction propagation, and runtime
  observation.

[↑ Back to top](#top)

---

<sub>Roads / Rail / Trade Routes dashboard specification. Documentation reports
governance-health posture; contracts define meaning, schemas define shape,
policy decides, review records disposition, release artifacts authorize use, and
correction/rollback preserve reversibility. A dashboard, map, graph, test,
workflow, receipt, or AI explanation is never sovereign truth.</sub>
