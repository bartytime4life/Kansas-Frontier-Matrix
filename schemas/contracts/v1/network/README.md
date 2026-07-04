# `schemas/contracts/v1/network/` — Network Schema Placement Guardrail

<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/schemas-contracts-v1-network-readme
title: schemas/contracts/v1/network/ — Network Schema Placement Guardrail
type: readme; schema-alias-index; placement-guardrail; graph-network-boundary
authority_class: placement-guardrail
version: v0.1
status: draft; empty-alias-index; shared-network-home-unsettled; roads-rail-trade-network-meaning-surfaced; roads-compatibility-network-candidates-surfaced; no-current-root-schema-files-found; do-not-promote-without-ADR; NEEDS VERIFICATION before promotion
owners:
  - OWNER_TBD — Network steward
  - OWNER_TBD — Graph steward
  - OWNER_TBD — Roads/Rail/Trade domain steward
  - OWNER_TBD — Transport compatibility steward
  - OWNER_TBD — Schema steward
  - OWNER_TBD — Contract steward
  - OWNER_TBD — Policy steward
  - OWNER_TBD — Release steward
  - OWNER_TBD — Validation steward
  - OWNER_TBD — Docs steward
created: NEEDS VERIFICATION — empty README existed before v0.1 expansion
updated: 2026-07-04
policy_label: public; schemas; contracts-v1; network; graph; route-network; topology; network-node; network-edge; route-membership; graph-projection; derived-network; evidence-bound; policy-aware; release-gated; rollback-aware; no-parallel-authority
tags: [kfm, schemas, contracts, v1, network, graph, topology, network-node, network-edge, route-membership, roads-rail-trade, transport, routing, graph-projection, derived-network, no-parallel-authority]
related:
  - ../README.md
  - ../domains/README.md
  - ../domains/roads-rail-trade/README.md
  - ../domains/roads/README.md
  - ../domains/transport/README.md
  - ../../../../contracts/domains/roads-rail-trade/network_node.md
  - ../../../../contracts/domains/roads-rail-trade/route_membership.md
  - ../../../../contracts/domains/roads-rail-trade/trade_route_corridor.md
  - ../../../../contracts/domains/roads-rail-trade/freight_corridor.md
  - ../../../../contracts/domains/roads-rail-trade/road_segment.md
  - ../../../../contracts/domains/roads-rail-trade/rail_segment.md
  - ../../../../contracts/domains/roads-rail-trade/domain_feature_identity.md
  - ../../../../contracts/domains/roads-rail-trade/domain_layer_descriptor.md
  - ../../../../docs/domains/roads-rail-trade/FILE_SYSTEM_PLAN.md
  - ../../../../docs/domains/roads-rail-trade/CANONICAL_PATHS.md
  - ../../../../docs/domains/roads-rail-trade/
  - ../../../../policy/domains/roads-rail-trade/
  - ../../../../fixtures/domains/roads-rail-trade/
  - ../../../../tests/domains/roads-rail-trade/
  - ../../../../release/candidates/roads-rail-trade/
notes:
  - "Expanded from an empty file at schemas/contracts/v1/network/README.md."
  - "Current GitHub search did not surface schema files directly under schemas/contracts/v1/network/ beyond this README in the current check."
  - "Search surfaced Roads/Rail/Trade semantic contracts such as network_node, route_membership, route/corridor, road_segment, and rail_segment."
  - "schemas/contracts/v1/domains/roads-rail-trade/README.md lists network_edge.schema.json as a candidate derived graph projection shape, not canonical route/segment truth."
  - "schemas/contracts/v1/domains/roads/README.md lists network_node.schema.json and network_edge.schema.json as NEEDS VERIFICATION candidates and marks roads as a compatibility index under roads-rail-trade."
  - "This README is a placement guardrail only; do not create canonical network schemas here without ADR, paired contracts, fixtures, validators, and steward review."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

![status](https://img.shields.io/badge/status-draft-yellow)
![root](https://img.shields.io/badge/root-schemas%2F-blue)
![family](https://img.shields.io/badge/family-network-slategray)
![posture](https://img.shields.io/badge/posture-placement__guardrail-orange)
![canonical](https://img.shields.io/badge/canonical-NEEDS__ADR-yellow)
![truth](https://img.shields.io/badge/truth-cite--or--abstain-success)

> **Purpose.** `schemas/contracts/v1/network/` is an empty top-level guardrail README for a possible shared Network schema family.
>
> **One-line boundary.** Current evidence places route/network meaning in Roads/Rail/Trade and roads compatibility surfaces; this path must not become a parallel canonical network schema home without an accepted ADR or migration plan.

---

## Quick jumps

[Status](#status) · [Placement decision](#placement-decision) · [Repo fit](#repo-fit) · [Current inventory](#current-inventory) · [Related surfaced lanes](#related-surfaced-lanes) · [Candidate network shapes](#candidate-network-shapes) · [What belongs here](#what-belongs-here) · [What does not belong here](#what-does-not-belong-here) · [Network guardrails](#network-guardrails) · [Migration rules](#migration-rules) · [Validation](#validation) · [Rollback](#rollback) · [Open questions](#open-questions)

---

## Status

| Question | Answer | Truth label |
|---|---|---|
| Does this README path exist? | Yes: `schemas/contracts/v1/network/README.md`. It was empty before this expansion. | **CONFIRMED** |
| Are schema files currently present directly under `schemas/contracts/v1/network/`? | Not found in the current GitHub search beyond this README. | **NEEDS VERIFICATION / search-limited** |
| Where is the closest confirmed network/route meaning surfaced? | Roads/Rail/Trade contracts and schema README surfaces, plus the `roads/` compatibility index. | **CONFIRMED path evidence** |
| Is Roads/Rail/Trade schema placement settled? | No. The Roads/Rail/Trade schema README records `roads-rail-trade` vs `transport` and flat-vs-domain path drift. | **CONFIRMED conflict-visible** |
| Is a top-level shared network schema family accepted? | Not proven. Treat this path as README-only until ADR or steward decision. | **NEEDS VERIFICATION / ADR-sensitive** |
| Can this path store routing outputs, graph databases, released network products, or public map/API artifacts? | No. This is schema documentation only, not lifecycle data, graph storage, runtime output, release storage, or publication surface. | **CONFIRMED boundary** |

> [!IMPORTANT]
> Network schemas must not collapse source-bound roads, rail segments, corridors, route membership, facilities, modeled graph edges, released summaries, or runtime routing outputs into one unreviewed authority.

---

## Placement decision

Current placement posture:

```text
Empty top-level guardrail path:
  schemas/contracts/v1/network/

Closest surfaced route/network schema lane:
  schemas/contracts/v1/domains/roads-rail-trade/

Related compatibility / orientation lane:
  schemas/contracts/v1/domains/roads/

Related conflict / compatibility lane:
  schemas/contracts/v1/domains/transport/
```

Rationale:

- Domain schemas normally belong under `schemas/contracts/v1/domains/<domain>/...` unless an accepted exception says otherwise.
- Roads/Rail/Trade currently carries route, corridor, segment, membership, transport facility, and candidate `network_edge` meaning.
- The `roads/` path is a compatibility index and lists `network_node` and `network_edge` as candidates, while pointing back to the broader Roads/Rail/Trade lane.
- A shared top-level network family may be useful later for cross-domain graph shapes, but that acceptance was not verified in this session.
- Any future schema here must be paired with semantic contracts, fixtures, validators, registry entries, policy/release review, and steward review across affected domains.

---

## Repo fit

```text
schemas/
└── contracts/
    └── v1/
        ├── README.md
        ├── network/
        │   └── README.md                         # this file; placement guardrail only
        └── domains/
            ├── roads-rail-trade/
            │   └── README.md                     # route/network domain schema lane; slug-conflicted
            ├── roads/
            │   └── README.md                     # compatibility index
            └── transport/
                └── README.md                     # related compatibility/conflict lane

contracts/
└── domains/
    └── roads-rail-trade/                          # semantic route/network meaning; not machine shape
        ├── network_node.md
        ├── route_membership.md
        ├── trade_route_corridor.md
        ├── freight_corridor.md
        ├── road_segment.md
        └── rail_segment.md

policy/
fixtures/
tests/
data/
release/
```

---

## Current inventory

| Path | Status | Note |
|---|---|---|
| `schemas/contracts/v1/network/README.md` | **CONFIRMED present** | Empty file expanded by this README. |
| `schemas/contracts/v1/network/*.schema.json` | **Not found in current search** | Do not create here without ADR, paired contracts, and validation plan. |
| `schemas/contracts/v1/domains/roads-rail-trade/README.md` | **CONFIRMED inspected** | Draft route/network domain schema lane; PROPOSED / slug-CONFLICTED. |
| `schemas/contracts/v1/domains/roads/README.md` | **CONFIRMED inspected** | Road-specific compatibility index under Roads/Rail/Trade; lists network candidates. |
| `schemas/contracts/v1/domains/transport/README.md` | **CONFIRMED surfaced previously** | Related compatibility/conflict lane; not opened in this edit. |
| Roads/Rail/Trade network contracts | **CONFIRMED surfaced by search** | Includes `network_node.md`, `route_membership.md`, corridor, road, rail, and facility surfaces. |

---

## Related surfaced lanes

| Path | Role signal | Posture |
|---|---|---|
| `schemas/contracts/v1/domains/roads-rail-trade/` | Route, corridor, segment, membership, and candidate graph projection schema lane. | **PROPOSED / slug-CONFLICTED** |
| `schemas/contracts/v1/domains/roads/` | Road-specific compatibility index. | **PROPOSED / CONFLICTED** |
| `schemas/contracts/v1/domains/transport/` | Related compatibility/conflict surface. | **NEEDS VERIFICATION** |
| `schemas/contracts/v1/network/` | Possible shared network schema family. | **README-only guardrail** |

---

## Candidate network shapes

Candidate schemas below require steward review, paired contracts, fixtures, validators, registry records, and release/policy review before promotion.

| Candidate schema | Purpose | Default posture |
|---|---|---|
| `network_node.schema.json` | Shared graph/network node shape. | **PROPOSED / not created here** |
| `network_edge.schema.json` | Shared graph/network edge shape. | **PROPOSED / not created here** |
| `network_membership.schema.json` | Relationship between source-bound route/segment/facility records and derived network topology. | **PROPOSED / placement-sensitive** |
| `network_projection_manifest.schema.json` | Manifest for derived network projection runs and inputs. | **PROPOSED / evidence-bound** |
| `network_validation_report.schema.json` | Shape for validation output about topology, connectivity, dangling edges, and reference integrity. | **PROPOSED / proof-adjacent** |
| `public_safe_network_summary.schema.json` | Release-facing network summary descriptor. | **PROPOSED / release-gated** |

> [!CAUTION]
> Candidate names are proposals only. Do not treat them as repo files, accepted contracts, implementation proof, routing authority, or graph materialization evidence until created, paired, fixture-tested, and reviewed.

---

## What belongs here

- This README.
- Placement notes for a possible shared network schema family.
- Future neutral network/graph schema files if an accepted ADR or migration plan authorizes this lane.
- Profile notes explaining how domain route/network schemas relate to shared network shapes.
- Links to paired contracts, fixtures, validators, schema registry records, policy references, evidence references, release references, correction references, and rollback references.
- Migration notes if network schemas are moved, profiled, aliased, or consolidated across `network/`, `roads-rail-trade/`, `roads/`, and `transport/` lanes.

---

## What does not belong here

- Roads/Rail/Trade-owned canonical schemas unless a reviewed shared-network profile is accepted.
- Roads-owned or transport-owned compatibility schemas unless an accepted migration authorizes this path.
- Semantic contract prose beyond README boundary notes.
- Policy rules, exposure decisions, release decisions, routing guidance, legal route-status guidance, or emergency access guidance.
- Lifecycle data, graph databases, routing outputs, route datasets, source records, catalog records, triplets, receipt instances, proof outputs, release records, correction notices, rollback cards, public API artifacts, map artifacts, dashboards, screenshots, or generated summaries.
- Validator code, packages, pipelines, runtime code, UI/API implementation, or graph materialization code.
- Claims that a network is valid, complete, connected, routable, current, public-safe, release-approved, or authoritative merely because an object validates against a schema.

---

## Network guardrails

| Boundary | Requirement |
|---|---|
| Source-bound vs derived | Source-bound roads, rails, routes, corridors, facilities, and crossings remain distinct from derived network nodes/edges. |
| Graph is not truth | A graph projection is a derived representation, not canonical source truth. |
| Routing is not schema | A schema does not provide routing advice, legal route status, emergency access, or operational instructions. |
| Domain ownership remains intact | Roads/Rail/Trade and adjacent domains keep their canonical shapes and semantic contracts. |
| Reference discipline | Network objects should reference domain-owned records instead of copying domain fields. |
| Evidence dependency | Network claims need EvidenceBundle or equivalent support where claims depend on evidence. |
| Policy dependency | Networks that affect access, exposure, public display, or sensitive places need policy posture. |
| Release dependency | Public network projections must be release-gated and rollback-aware. |
| No parallel authority | Do not maintain equivalent network schemas under `network/` and domain lanes without a mirror/migration rule. |

---

## Migration rules

Do not move or duplicate network schemas into this path unless a reviewed migration plan defines:

- source path;
- target path;
- owning root;
- reason for migration;
- chosen meaning of shared `network`;
- schema `$id` changes;
- `$ref` and consumer updates;
- fixture and validator updates;
- schema registry updates;
- affected domain steward review;
- policy review;
- release and rollback impact;
- deprecation/mirror window;
- tests proving no parallel authority remains.

---

## Validation

Recommended local validation sequence:

```bash
# Confirm this guardrail path remains README-only unless authorized.
find schemas/contracts/v1/network -maxdepth 2 -type f | sort

# Inspect network-related domain schema lanes.
find schemas/contracts/v1/domains/roads-rail-trade schemas/contracts/v1/domains/roads schemas/contracts/v1/domains/transport -maxdepth 4 -type f \
  | grep -Ei 'network|graph|route|corridor|segment|membership|node|edge|transport|README' \
  | sort

# Detect duplicate network authority.
find schemas/contracts/v1 -maxdepth 7 -type f \
  | grep -Ei 'network_node|network_edge|network|graph_projection|route_membership|corridor_route|road_segment|rail_segment' \
  | sort

# Validate JSON syntax for related domain schemas when present.
find schemas/contracts/v1/domains/roads-rail-trade schemas/contracts/v1/domains/roads schemas/contracts/v1/domains/transport -name '*.schema.json' -print0 \
  | xargs -0 -r -I{} python -m json.tool {} >/dev/null

# Run project validators when available.
python tools/validate_all.py || true
pytest tests/schemas tests/contract tests/domains/roads-rail-trade tests/policy tests/release || true
```

Replace `|| true` with fail-closed CI behavior once validator and test paths are confirmed.

---

## Rollback

Rollback for this README is ordinary Git rollback: revert the commit that changed `schemas/contracts/v1/network/README.md`.

Rollback for future network schema changes requires checking every downstream reference:

1. Revert or migrate schema files.
2. Restore canonical `$id` and `$ref` targets.
3. Restore paired contract links.
4. Restore fixtures, validators, schema registry records, and CI paths.
5. Restore domain, policy, evidence, release, correction, and receipt references.
6. Restore API/UI/MapLibre/graph consumers.
7. Preserve correction and rollback records if any public network surface was affected.

---

## Open questions

| Question | Status | Owner |
|---|---|---|
| Should `schemas/contracts/v1/network/` become an accepted shared network schema family or remain README-only? | **NEEDS VERIFICATION / ADR-sensitive** | Schema steward + Network steward + domain stewards |
| Should `network_node` and `network_edge` remain Roads/Rail/Trade candidates, move to shared `network/`, or use explicit profiles? | **NEEDS VERIFICATION / migration-sensitive** | Roads/Rail/Trade steward + Network steward |
| How should `roads-rail-trade`, `roads`, and `transport` slug conflicts affect network schema placement? | **NEEDS VERIFICATION / slug-sensitive** | Schema steward + Transport compatibility steward |
| Which contract lane owns shared network semantics? | **NEEDS VERIFICATION** | Contract steward |
| Which fixtures prove the distinction between source-bound routes and derived network topology? | **NEEDS VERIFICATION** | Validation steward |
| Which network projections are safe for public API/MapLibre/Focus Mode use? | **NEEDS VERIFICATION / release-gated** | Release steward + Policy steward |

---

## Maintainer notes

- Keep this path README-only until the shared network-home decision is resolved.
- Prefer references to domain-owned route, segment, corridor, facility, and membership objects over copied fields.
- Do not let this lane duplicate Roads/Rail/Trade, roads, or transport schema authority.
- Preserve source-role separation, graph/projection boundaries, evidence, policy, release, correction, and rollback boundaries for every network surface.
