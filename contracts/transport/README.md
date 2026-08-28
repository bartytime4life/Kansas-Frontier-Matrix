<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/contracts-transport-readme
title: contracts/transport — Transport Compatibility Guard README
type: readme
version: v0.1
status: draft; compatibility-guard; slug-conflict-visible; no-parallel-authority; domain-path-variance
owners: OWNER_TBD — Roads/Rail/Trade domain steward · Transport steward · Contracts steward · Schema steward · Policy steward · Release steward · Docs steward · Directory Rules reviewer
created: 2026-06-24
updated: 2026-06-24
policy_label: public; contracts; transport; compatibility; roads-rail-trade; no-parallel-authority; slug-conflicted; evidence-bound; release-gated
tags: [kfm, contracts, transport, roads-rail-trade, roads, rail, trade-routes, compatibility, slug-conflict, domain-placement, no-parallel-authority, semantic-contracts]
related:
  - ../README.md
  - ../domains/roads-rail-trade/README.md
  - ../domains/roads/README.md
  - ../../docs/domains/roads-rail-trade/README.md
  - ../../docs/domains/roads-rail-trade/CANONICAL_PATHS.md
  - ../../docs/domains/roads-rail-trade/OBJECT_FAMILIES.md
  - ../../docs/domains/roads-rail-trade/IDENTITY_MODEL.md
  - ../../docs/domains/roads-rail-trade/GRAPH_PROJECTIONS.md
  - ../../schemas/contracts/v1/domains/roads-rail-trade/
  - ../../schemas/contracts/v1/transport/
  - ../../policy/domains/roads-rail-trade/
  - ../../fixtures/domains/roads-rail-trade/
  - ../../tests/domains/roads-rail-trade/
  - ../../release/candidates/roads-rail-trade/
notes:
  - "This file replaces a blank placeholder at `contracts/transport/README.md`."
  - "The inspected working transport-related semantic contract lane is `contracts/domains/roads-rail-trade/`."
  - "The inspected roads/rail/trade README explicitly records a slug conflict between `roads-rail-trade` and `transport` and does not settle it by ADR."
  - "This top-level `contracts/transport/` path is a compatibility guard only and must not become a parallel transport contract root."
  - "Contracts define semantic meaning; schemas, policy, fixtures, tests, source registries, data lifecycle, release artifacts, APIs, map rendering, graph outputs, packages, and runtime behavior remain in separate roots."
  - "Rollback target for this replacement is previous blank blob SHA `8b137891791fe96927ad78e64b0aad7bded08bdc`."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# contracts/transport

> Compatibility guard for the top-level `contracts/transport/` path. Current inspected transport-related contract work belongs under [`../domains/roads-rail-trade/`](../domains/roads-rail-trade/). This folder exists only to prevent stale or doctrine-derived `transport` references from becoming a parallel Roads/Rail/Trade authority before a slug ADR resolves the naming conflict.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Path: compatibility guard" src="https://img.shields.io/badge/path-compatibility__guard-lightgrey">
  <img alt="Canonical observed lane: roads-rail-trade" src="https://img.shields.io/badge/observed__lane-roads--rail--trade-blue">
  <img alt="Slug: conflicted" src="https://img.shields.io/badge/slug-CONFLICTED-red">
  <img alt="Posture: no parallel authority" src="https://img.shields.io/badge/posture-no__parallel__authority-critical">
</p>

**Status:** draft compatibility guard  
**Path:** `contracts/transport/README.md`  
**Observed working transport-related contract lane:** `contracts/domains/roads-rail-trade/`  
**Slug posture:** CONFLICTED / NEEDS ADR OR STEWARD REVIEW  
**Possible schema homes:** `schemas/contracts/v1/domains/roads-rail-trade/` or `schemas/contracts/v1/transport/` after ADR  
**Policy home:** `policy/domains/roads-rail-trade/` or ADR-selected successor  
**Truth posture:** CONFIRMED placeholder was blank · CONFIRMED current repo search found Roads/Rail/Trade transport object contracts under `contracts/domains/roads-rail-trade/` · CONFIRMED the inspected Roads/Rail/Trade README records a `roads-rail-trade` versus `transport` slug conflict · PROPOSED top-level guard until stale links are migrated or an ADR resolves the naming variance

## Quick jumps

[Purpose](#purpose) · [Authority split](#authority-split) · [Accepted contents](#accepted-contents) · [Exclusions](#exclusions) · [Migration posture](#migration-posture) · [Validation checklist](#validation-checklist) · [Rollback](#rollback)

---

## Purpose

This README exists because `contracts/transport/` exists as a top-level folder, but current repo evidence places transport-related domain semantic contracts under `contracts/domains/roads-rail-trade/`.

Use this path only as a compatibility guard and navigation pointer.

Do not add canonical transport object contracts here unless an accepted ADR resolves the slug conflict and migrates existing paths with backlink and rollback handling.

---

## Authority split

| Responsibility | Correct home | Rule |
|---|---|---|
| Roads/Rail/Trade semantic contracts | `contracts/domains/roads-rail-trade/` | Current inspected working lane for transport-related object meaning. |
| This top-level path | `contracts/transport/` | Compatibility guard only. |
| Road-specific compatibility slice | `contracts/domains/roads/` | Existing related slice; not global transport authority by itself. |
| Machine shape | `schemas/contracts/v1/domains/roads-rail-trade/` or `schemas/contracts/v1/transport/` after ADR | JSON Schema belongs under `schemas/`. |
| Policy/admissibility | `policy/domains/roads-rail-trade/` or ADR-selected policy home | Policy owns allow/deny/restrict/abstain. |
| Fixtures/tests | `fixtures/domains/roads-rail-trade/`, `tests/domains/roads-rail-trade/` or accepted roots | Proof/examples stay outside contracts. |
| Source registry | `data/registry/sources/roads-rail-trade/` or accepted registry roots | Source authority, cadence, rights, and caveats stay outside contracts. |
| Data lifecycle | `data/raw`, `data/work`, `data/quarantine`, `data/processed`, `data/catalog`, `data/published` | Contracts do not store data. |
| Release/correction/rollback | `release/candidates/roads-rail-trade/` and release roots | Publication is a governed state transition. |
| Public API/UI/map/graph/runtime | governed API/UI/map/graph/runtime roots | Downstream consumers only. |

---

## Accepted contents

Only conservative guard material belongs here:

| Accepted item | Purpose |
|---|---|
| `README.md` | Explain that this is not the canonical transport contract home. |
| `MIGRATION.md` | Optional temporary plan to resolve `transport` versus `roads-rail-trade` links. |
| `BACKLINKS.md` | Optional audit of stale links pointing here. |
| `ADR_POINTER.md` | Optional pointer to an accepted ADR if one resolves the slug conflict. |

Any content here must remain pointer-only and steward-reviewed.

---

## Exclusions

| Do not put this here | Correct home | Reason |
|---|---|---|
| Road, rail, trade-route, crossing, bridge, ferry, network, corridor, operator, route-membership, or status-event contracts | `contracts/domains/roads-rail-trade/` unless ADR selects another home | Avoids duplicate semantic authority. |
| JSON Schemas | `schemas/contracts/v1/domains/roads-rail-trade/` or ADR-selected schema home | Schemas own shape. |
| Policy rules | `policy/domains/roads-rail-trade/` or related policy roots | Policy owns decisions. |
| Source descriptors or source registry records | source registry/data registry roots | Contracts do not admit or store sources. |
| RAW/WORK/QUARANTINE/PROCESSED/CATALOG/PUBLISHED data | data lifecycle roots | Contracts do not store lifecycle data. |
| Graph projections, route networks, PMTiles, map styles, APIs, UI components | graph/map/API/UI/release roots | Delivery and projections are downstream. |
| Fixtures, tests, validators, packages, pipelines | `fixtures/`, `tests/`, `tools/validators/`, package/pipeline roots | Enforceability and execution stay separate. |
| Emergency routing, legal road status, or safety advice | governed source/API/policy/release paths | KFM must not imply live legal/safety authority without explicit support. |

---

## Migration posture

Preferred future state before any canonical use of `contracts/transport/`:

```text
contracts/transport/README.md                      # removed or retained only as compatibility guard
contracts/domains/roads-rail-trade/                # current observed semantic contract lane
schemas/contracts/v1/domains/roads-rail-trade/     # current observed schema candidate lane
schemas/contracts/v1/transport/                    # possible ADR-selected successor, not assumed
policy/domains/roads-rail-trade/                   # policy/admissibility lane
```

Before deleting this guard, search for stale backlinks that still point to `contracts/transport/`.

---

## Validation checklist

- [ ] Verify no canonical transport object contracts are added under `contracts/transport/`.
- [ ] Verify transport-related semantic contracts are routed to `contracts/domains/roads-rail-trade/` unless ADR says otherwise.
- [ ] Verify schema-home conflict is resolved by ADR before treating `schemas/contracts/v1/transport/` as canonical.
- [ ] Verify policy remains under `policy/domains/roads-rail-trade/` or ADR-selected successor.
- [ ] Verify source registry records, lifecycle data, release artifacts, packages, pipelines, fixtures, tests, and validators remain in their own roots.
- [ ] Search for stale top-level `contracts/transport/` references before deletion or migration.

---

## Rollback

Rollback is required if this path is used as canonical transport-object meaning, schema authority, policy authority, source registry authority, lifecycle storage, graph projection storage, release approval, runtime/API authority, public map/UI truth, emergency-routing authority, or legal/safety-status authority.

Rollback target for this replacement: previous blank blob SHA `8b137891791fe96927ad78e64b0aad7bded08bdc`.

<p align="right"><a href="#top">Back to top</a></p>
