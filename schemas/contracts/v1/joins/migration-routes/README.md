# `schemas/contracts/v1/joins/migration-routes/` — Migration Routes Join Schema Guardrail

<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/schemas-contracts-v1-joins-migration-routes-readme
title: schemas/contracts/v1/joins/migration-routes/ — Migration Routes Join Schema Guardrail
type: readme; join-schema-index; ambiguity-guardrail; route-migration-boundary
authority_class: join-schema-guardrail
version: v0.1
status: draft; empty-join-lane; ambiguous-route-meaning; fauna-migration-route-present; roads-rail-trade-route-lane-present; no-current-join-schema-files-found; do-not-promote-without-ADR; NEEDS VERIFICATION before promotion
owners:
  - OWNER_TBD — Join steward
  - OWNER_TBD — Schema steward
  - OWNER_TBD — Contract steward
  - OWNER_TBD — Fauna domain steward
  - OWNER_TBD — Roads/Rail/Trade domain steward
  - OWNER_TBD — Transport compatibility steward
  - OWNER_TBD — Sensitivity steward
  - OWNER_TBD — Policy steward
  - OWNER_TBD — Release steward
  - OWNER_TBD — Validation steward
  - OWNER_TBD — Docs steward
created: NEEDS VERIFICATION — empty README existed before v0.1 expansion
updated: 2026-07-04
policy_label: public; schemas; contracts-v1; joins; migration-routes; ambiguous-term; fauna-migration; route-network; cross-domain; sensitivity-aware; evidence-bound; release-gated; rollback-aware; no-parallel-authority
tags: [kfm, schemas, contracts, v1, joins, migration-routes, migration-route, fauna, roads-rail-trade, transport, roads, routes, corridors, route-membership, network-edge, cross-domain, guardrail, no-parallel-authority]
related:
  - ../../README.md
  - ../README.md
  - ../../domains/README.md
  - ../../domains/fauna/README.md
  - ../../domains/fauna/migration_route.schema.json
  - ../../domains/roads-rail-trade/README.md
  - ../../domains/transport/README.md
  - ../../domains/roads/README.md
  - ../../../../contracts/domains/fauna/
  - ../../../../contracts/domains/roads-rail-trade/
  - ../../../../contracts/domains/transport/
  - ../../../../docs/domains/fauna/
  - ../../../../docs/domains/roads-rail-trade/
  - ../../../../policy/domains/fauna/
  - ../../../../policy/domains/roads-rail-trade/
  - ../../../../fixtures/domains/fauna/
  - ../../../../fixtures/domains/roads-rail-trade/
  - ../../../../tests/domains/fauna/
  - ../../../../tests/domains/roads-rail-trade/
notes:
  - "Expanded from an empty file at schemas/contracts/v1/joins/migration-routes/README.md."
  - "Current GitHub search did not surface schema files directly under this join lane beyond this README in the current check."
  - "Search surfaced schemas/contracts/v1/domains/fauna/migration_route.schema.json and schemas/contracts/v1/domains/fauna/README.md, making ecological migration an existing domain concern."
  - "Search surfaced schemas/contracts/v1/domains/roads-rail-trade/README.md, schemas/contracts/v1/domains/transport/README.md, and schemas/contracts/v1/domains/roads/README.md, making route/corridor/network meaning slug-sensitive."
  - "This README is a placement and ambiguity guardrail only; do not create canonical migration-route join schemas here without ADR, paired contracts, fixtures, validators, and steward review."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

![status](https://img.shields.io/badge/status-draft-yellow)
![root](https://img.shields.io/badge/root-schemas%2F-blue)
![family](https://img.shields.io/badge/family-joins-purple)
![join](https://img.shields.io/badge/join-migration--routes-slategray)
![posture](https://img.shields.io/badge/posture-guardrail-orange)
![ambiguity](https://img.shields.io/badge/term-ambiguous-red)
![truth](https://img.shields.io/badge/truth-cite--or--abstain-success)

> **Purpose.** `schemas/contracts/v1/joins/migration-routes/` is an empty guardrail README for a possible cross-domain Migration Routes join schema lane.
>
> **One-line boundary.** This path must not become canonical until stewards decide whether “migration routes” means Fauna movement routes, human migration/corridor history, transport/trade routes, or a governed join among those concepts.

---

## Quick jumps

[Status](#status) · [Placement decision](#placement-decision) · [Repo fit](#repo-fit) · [Current inventory](#current-inventory) · [Related surfaced lanes](#related-surfaced-lanes) · [Candidate join shapes](#candidate-join-shapes) · [What belongs here](#what-belongs-here) · [What does not belong here](#what-does-not-belong-here) · [Join guardrails](#join-guardrails) · [Migration rules](#migration-rules) · [Validation](#validation) · [Rollback](#rollback) · [Open questions](#open-questions)

---

## Status

| Question | Answer | Truth label |
|---|---|---|
| Does this README path exist? | Yes: `schemas/contracts/v1/joins/migration-routes/README.md`. It was empty before this expansion. | **CONFIRMED** |
| Are schema files currently present under this join lane? | Not found in the current GitHub search beyond this README. | **NEEDS VERIFICATION / search-limited** |
| Is there an existing Fauna migration route schema surface? | Yes. Search surfaced `schemas/contracts/v1/domains/fauna/migration_route.schema.json`, and the Fauna README lists `migration_route.schema.json` as a candidate migration route shape. | **CONFIRMED path evidence** |
| Is there an existing route/corridor domain surface? | Yes. Search surfaced `schemas/contracts/v1/domains/roads-rail-trade/README.md`, and that README lists route/corridor candidates and slug conflict with transport. | **CONFIRMED path evidence** |
| Is this join lane canonical? | Not proven. Treat as guardrail/index only until ADR or steward decision. | **NEEDS VERIFICATION / ADR-sensitive** |
| Can this lane store route data, migration tracks, lifecycle records, or released outputs? | No. This path is schema documentation only, not lifecycle data, emitted records, release records, public artifacts, routing advice, or movement authority. | **CONFIRMED boundary** |

> [!IMPORTANT]
> “Migration routes” is ambiguous. KFM must not collapse ecological migration, human movement history, transport corridors, trade routes, derived network edges, or released public route summaries into one unreviewed schema home.

---

## Placement decision

Current placement posture:

```text
Requested join guardrail:
  schemas/contracts/v1/joins/migration-routes/

Existing ecological migration surface:
  schemas/contracts/v1/domains/fauna/migration_route.schema.json
  schemas/contracts/v1/domains/fauna/

Existing route/corridor schema lane:
  schemas/contracts/v1/domains/roads-rail-trade/

Related compatibility / conflict lanes surfaced by search:
  schemas/contracts/v1/domains/transport/
  schemas/contracts/v1/domains/roads/
```

Rationale:

- Domain schemas normally belong under `schemas/contracts/v1/domains/<domain>/...` unless an accepted exception says otherwise.
- Fauna already has a migration route schema surface, and Fauna carries sensitivity review requirements.
- Roads/Rail/Trade already owns route/corridor/route-membership candidate meaning, while its slug remains conflicted with `transport` in current evidence.
- This join lane may be useful for cross-domain relationship shapes, but it is not confirmed as accepted in this session.
- Any future schema here must be paired with contracts, fixtures, validators, registry entries, sensitivity/policy review, release review, and steward review across affected domains.

---

## Repo fit

```text
schemas/
└── contracts/
    └── v1/
        ├── README.md
        ├── joins/
        │   └── migration-routes/
        │       └── README.md                     # this file; join guardrail only
        └── domains/
            ├── fauna/
            │   ├── README.md
            │   └── migration_route.schema.json   # surfaced by search
            ├── roads-rail-trade/
            │   └── README.md                     # route/corridor schema index; slug-conflicted
            ├── transport/
            │   └── README.md                     # related compatibility/conflict lane
            └── roads/
                └── README.md                     # related compatibility/conflict lane

contracts/
├── domains/fauna/                                 # semantic meaning; not machine shape
└── domains/roads-rail-trade/                      # semantic meaning; not machine shape

policy/
fixtures/
tests/
release/
```

---

## Current inventory

| Path | Status | Note |
|---|---|---|
| `schemas/contracts/v1/joins/migration-routes/README.md` | **CONFIRMED present** | Empty file expanded by this README. |
| `schemas/contracts/v1/joins/migration-routes/*.schema.json` | **Not found in current search** | Do not create here without ADR, paired contracts, and validation plan. |
| `schemas/contracts/v1/domains/fauna/migration_route.schema.json` | **CONFIRMED surfaced by search** | Existing Fauna migration route schema surface; field maturity not inspected in this edit. |
| `schemas/contracts/v1/domains/fauna/README.md` | **CONFIRMED inspected** | Fauna schema lane; lists `migration_route.schema.json` as a candidate and keeps sensitivity discipline. |
| `schemas/contracts/v1/domains/roads-rail-trade/README.md` | **CONFIRMED inspected** | Route/corridor schema lane; slug conflict remains visible. |
| `schemas/contracts/v1/domains/transport/README.md` | **CONFIRMED surfaced by search** | Related compatibility/conflict route/transport lane; not opened in this edit. |
| `schemas/contracts/v1/domains/roads/README.md` | **CONFIRMED surfaced by search** | Related compatibility/conflict route/road lane; not opened in this edit. |

---

## Related surfaced lanes

| Path | Role signal | Posture |
|---|---|---|
| `schemas/contracts/v1/domains/fauna/` | Fauna-owned machine shape lane; includes migration route candidate/surface. | **PROPOSED / sensitivity-aware** |
| `schemas/contracts/v1/domains/roads-rail-trade/` | Roads/Rail/Trade-owned route/corridor schema lane. | **PROPOSED / slug-CONFLICTED** |
| `schemas/contracts/v1/domains/transport/` | Related transport compatibility or conflict surface. | **NEEDS VERIFICATION** |
| `schemas/contracts/v1/domains/roads/` | Related roads compatibility or conflict surface. | **NEEDS VERIFICATION** |
| `schemas/contracts/v1/joins/migration-routes/` | Possible neutral join schema lane. | **README-only guardrail** |

---

## Candidate join shapes

Candidate join schemas below require steward review, paired contracts, fixtures, validators, registry records, and sensitivity/policy/release review before promotion.

| Candidate schema | Purpose | Default posture |
|---|---|---|
| `migration_routes_join.schema.json` | Generic relationship between migration-route refs and route/corridor refs. | **PROPOSED / not created** |
| `fauna_route_corridor_join.schema.json` | Relationship shape between Fauna migration-route refs and corridor/landscape route context refs. | **PROPOSED / sensitivity-aware** |
| `historic_migration_route_context.schema.json` | Relationship shape for human/historical migration route interpretations and route/corridor evidence. | **PROPOSED / evidence-bound** |
| `route_membership_migration_context.schema.json` | Relationship between route-membership refs and migration context refs. | **PROPOSED / placement-sensitive** |
| `migration_routes_release_projection.schema.json` | Public/release projection for already-governed migration-route joins. | **PROPOSED / release-gated** |

> [!CAUTION]
> Candidate names are proposals only. Do not treat them as repo files, accepted contracts, or implementation proof until created, paired, fixture-tested, and reviewed.

---

## What belongs here

- This README.
- Join schema placement notes for migration-route relationships.
- Ambiguity notes separating Fauna migration, human/historical movement, transport/trade routes, and derived route graphs.
- Future neutral join schema files if an accepted ADR or migration plan authorizes this lane.
- Links to paired contracts, fixtures, validators, schema registry records, sensitivity references, policy references, release references, and tests.
- Drift notes preventing duplicate Fauna, Roads/Rail/Trade, Transport, or Roads schema authority.

---

## What does not belong here

- Fauna-owned canonical migration route schemas.
- Roads/Rail/Trade-owned canonical route, corridor, segment, route-membership, transport, or graph schemas.
- Compatibility schemas that belong under `transport/` or `roads/` if those lanes are later accepted.
- Semantic contract prose.
- Policy rules, sensitivity decisions, exposure decisions, release decisions, routing guidance, or legal route-status guidance.
- Lifecycle data, route datasets, movement tracks, telemetry, source records, catalog records, triplets, receipt instances, proof outputs, release records, correction notices, rollback cards, or public artifacts.
- Validator code, packages, pipelines, runtime code, UI/API implementation, map tiles, dashboards, screenshots, or generated summaries.
- Claims that a migration route is valid, complete, true, safe, current, or public-ready merely because it validates against a schema.

---

## Join guardrails

| Boundary | Requirement |
|---|---|
| Domain ownership | Fauna and Roads/Rail/Trade keep their own canonical shapes and semantic contracts. |
| Term clarity | State whether “migration” means animal movement, human/historical movement, model-derived movement, or another domain concept. |
| Join neutrality | A join schema records relationship shape, not source truth for either side. |
| Reference discipline | Use stable references to domain-owned objects rather than duplicating domain fields. |
| Sensitivity discipline | Sensitive route, occurrence, site, telemetry, or steward-controlled details require fail-closed review before release. |
| Evidence dependency | Join outputs need EvidenceBundle or equivalent support where claims depend on evidence. |
| Policy dependency | Joins that affect release, access, or public display must carry policy posture. |
| Release dependency | Public join projections must be release-gated and rollback-aware. |
| Graph discipline | Derived route graphs must not replace source-bound route, migration, corridor, segment, or membership records. |
| No parallel authority | Do not maintain identical join schema definitions under `joins/` and domain lanes without a mirror/migration rule. |

---

## Migration rules

Do not move or duplicate migration-route schemas into this path unless a reviewed migration plan defines:

- source path;
- target path;
- owning root;
- reason for migration;
- chosen meaning of “migration route”;
- schema `$id` changes;
- `$ref` and consumer updates;
- fixture and validator updates;
- schema registry updates;
- Fauna, Roads/Rail/Trade, and other affected steward review;
- sensitivity and policy review;
- release and rollback impact;
- deprecation/mirror window;
- tests proving no parallel authority remains.

---

## Validation

Recommended local validation sequence:

```bash
# Confirm this join lane remains README-only unless authorized.
find schemas/contracts/v1/joins/migration-routes -maxdepth 2 -type f | sort

# Inspect route/migration related schema lanes.
find schemas/contracts/v1/domains/fauna schemas/contracts/v1/domains/roads-rail-trade schemas/contracts/v1/domains/transport schemas/contracts/v1/domains/roads -maxdepth 4 -type f \
  | grep -Ei 'migration|route|corridor|segment|membership|transport|road|rail|README' \
  | sort

# Detect duplicate migration-route authority.
find schemas/contracts/v1 -maxdepth 6 -type f \
  | grep -Ei 'migration.*route|route.*migration|corridor|route_membership|network_edge' \
  | sort

# Validate JSON syntax for related domain schemas when present.
find schemas/contracts/v1/domains/fauna schemas/contracts/v1/domains/roads-rail-trade schemas/contracts/v1/domains/transport schemas/contracts/v1/domains/roads -name '*.schema.json' -print0 \
  | xargs -0 -r -I{} python -m json.tool {} >/dev/null

# Run project validators when available.
python tools/validate_all.py || true
pytest tests/schemas tests/contract tests/domains/fauna tests/domains/roads-rail-trade tests/policy || true
```

Replace `|| true` with fail-closed CI behavior once validator and test paths are confirmed.

---

## Rollback

Rollback for this README is ordinary Git rollback: revert the commit that changed `schemas/contracts/v1/joins/migration-routes/README.md`.

Rollback for future join schema changes requires checking every downstream reference:

1. Revert or migrate schema files.
2. Restore canonical `$id` and `$ref` targets.
3. Restore paired contract links.
4. Restore fixtures, validators, schema registry records, and CI paths.
5. Restore Fauna, Roads/Rail/Trade, Transport, Roads, policy, sensitivity, evidence, release, and receipt references.
6. Restore API/UI/MapLibre/Evidence Drawer consumers.
7. Preserve correction and rollback records if any public join surface was affected.

---

## Open questions

| Question | Status | Owner |
|---|---|---|
| Does “migration routes” mean Fauna migration, human/historical migration, transport/trade routes, or a cross-domain join? | **NEEDS VERIFICATION / ADR-sensitive** | Join steward + domain stewards |
| Should neutral migration-route relationships live under `joins/`, remain Fauna-owned, remain Roads/Rail/Trade-owned, or use another cross-domain lane? | **NEEDS VERIFICATION / ADR-sensitive** | Schema steward + Fauna steward + Roads/Rail/Trade steward |
| Should the slug be `migration-routes`, `migration_routes`, `fauna-migration-routes`, or another convention? | **NEEDS VERIFICATION / slug-sensitive** | Schema steward + Join steward |
| Which contract lane should own neutral migration-route join semantics? | **NEEDS VERIFICATION** | Contract steward |
| Which fixtures prove that joins do not duplicate domain-owned fields or expose sensitive details? | **NEEDS VERIFICATION** | Validation steward + Sensitivity steward |
| Which migration-route projections are safe for public API/MapLibre/Focus Mode use? | **NEEDS VERIFICATION / release-gated** | Release steward + Policy steward |

---

## Maintainer notes

- Keep this path README-only until the term and join-home decision are resolved.
- Prefer references to domain-owned migration, route, corridor, and membership objects over copied fields.
- Do not let this join lane duplicate Fauna, Roads/Rail/Trade, Transport, or Roads schema authority.
- Preserve evidence, sensitivity, ownership, policy, release, correction, and rollback boundaries for all migration-route join surfaces.
