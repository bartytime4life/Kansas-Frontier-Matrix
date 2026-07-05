# `schemas/contracts/v1/trade-routes/` — Trade Routes Schema Compatibility Guardrail

<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/schemas-contracts-v1-trade-routes-readme
title: schemas/contracts/v1/trade-routes/ — Trade Routes Schema Compatibility Guardrail
type: readme; compatibility-index; schema-boundary; trade-routes-placement-guardrail
authority_class: schema-family-guardrail
version: v0.1
status: draft; empty-flat-schema-path; no-current-trade-routes-schema-files-found; parent-domain-schema-lane-present; documentation-sublane-adjacent; PROPOSED; NEEDS VERIFICATION before promotion
owners:
  - OWNER_TBD — Roads/Rail/Trade domain steward
  - OWNER_TBD — Trade routes steward
  - OWNER_TBD — Schema steward
  - OWNER_TBD — Contract steward
  - OWNER_TBD — Validation steward
  - OWNER_TBD — Docs steward
created: NEEDS VERIFICATION — empty README existed before v0.1 expansion
updated: 2026-07-04
policy_label: public; schemas; contracts-v1; trade-routes; roads-rail-trade; compatibility-path; no-parallel-authority
tags: [kfm, schemas, contracts, v1, trade-routes, roads-rail-trade, transport, route-claims, corridors, compatibility, no-parallel-authority]
related:
  - ../README.md
  - ../domains/roads-rail-trade/README.md
  - ../network/README.md
  - ../crossings/README.md
  - ../../../docs/domains/roads-rail-trade/sublanes/trade_routes.md
  - ../../../docs/domains/roads-rail-trade/README.md
  - ../../../contracts/domains/roads-rail-trade/
  - ../../../fixtures/
  - ../../../tests/
notes:
  - "Expanded from an empty file at schemas/contracts/v1/trade-routes/README.md."
  - "Current GitHub search did not surface schema files directly under schemas/contracts/v1/trade-routes/ beyond this README."
  - "schemas/contracts/v1/domains/roads-rail-trade/README.md is the inspected parent Roads/Rail/Trade domain schema lane."
  - "docs/domains/roads-rail-trade/sublanes/trade_routes.md describes trade routes as a documentation sublane and says executable artifacts continue under parent responsibility roots."
  - "This flat path is a compatibility guardrail only and must not become a parallel canonical schema home without ADR or migration review."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

![status](https://img.shields.io/badge/status-draft-yellow)
![root](https://img.shields.io/badge/root-schemas%2F-blue)
![family](https://img.shields.io/badge/family-trade--routes-slategray)
![posture](https://img.shields.io/badge/posture-compatibility-orange)
![truth](https://img.shields.io/badge/truth-cite--or--abstain-success)

> **Purpose.** `schemas/contracts/v1/trade-routes/` is a flat compatibility guardrail for trade-route schema placement.
>
> **One-line boundary.** This path defines schema-placement guidance only. It does not replace the parent `schemas/contracts/v1/domains/roads-rail-trade/` schema lane, store route data, create a new sublane authority, or publish route products.

---

## Status

| Question | Answer | Truth label |
|---|---|---|
| Does this README path exist? | Yes. It was empty before this expansion. | **CONFIRMED** |
| Are schema files present directly under this flat path? | Not found in the current GitHub search beyond this README. | **NEEDS VERIFICATION / search-limited** |
| Is there an inspected parent domain schema lane? | Yes. `schemas/contracts/v1/domains/roads-rail-trade/README.md` is the inspected parent domain schema index. | **CONFIRMED path evidence** |
| Is the parent domain lane field-complete? | Not proven. Its README states concrete schema inventory remains **NEEDS VERIFICATION**. | **CONFIRMED scaffold / NEEDS VERIFICATION** |
| Is the trade-routes sublane canonical as a separate schema home? | No. The inspected trade-routes doc treats the sublane as documentation-only and says executable artifacts continue under the parent responsibility roots. | **CONFIRMED boundary / NEEDS VERIFICATION for future ADR** |
| Can this flat folder store lifecycle data, source records, proofs, catalog records, release records, runtime code, map products, or route payloads? | No. This is a schema compatibility folder and may only define machine-checkable shape if accepted here later. | **CONFIRMED boundary** |

---

## Authority and placement

Current placement posture:

```text
schemas/contracts/v1/trade-routes/                 # this flat compatibility guardrail
schemas/contracts/v1/domains/roads-rail-trade/     # inspected parent Roads/Rail/Trade schema lane
docs/domains/roads-rail-trade/sublanes/trade_routes.md  # trade-route documentation sublane
contracts/domains/roads-rail-trade/                # semantic meaning; not schema shape
```

Adjacent authority remains separate:

- `schemas/contracts/v1/domains/roads-rail-trade/` owns the parent domain schema lane unless an ADR or migration note says otherwise.
- `contracts/domains/roads-rail-trade/` owns semantic meaning.
- `docs/domains/roads-rail-trade/` owns human-facing domain documentation and sublane notes.
- `fixtures/` and `tests/` prove examples and behavior where present.
- `data/` owns lifecycle records and emitted data products where present.
- `release/` owns release records where present.

This README does not amend ADR-0001, Directory Rules, Roads/Rail/Trade placement, sublane terminology, validators, or release gates.

---

## Repo fit

```text
schemas/
└── contracts/
    └── v1/
        ├── trade-routes/
        │   └── README.md                         # this file; flat compatibility guardrail
        └── domains/
            └── roads-rail-trade/
                └── README.md                     # parent domain schema index

docs/
└── domains/
    └── roads-rail-trade/
        └── sublanes/
            └── trade_routes.md                   # documentation sublane; not schema home

contracts/
└── domains/
    └── roads-rail-trade/                          # semantic meaning

fixtures/
tests/
data/
release/
```

---

## Current inventory

| Path | Current posture | Notes |
|---|---|---|
| `schemas/contracts/v1/trade-routes/README.md` | **CONFIRMED present** | Empty file expanded by this README. |
| `schemas/contracts/v1/trade-routes/*.schema.json` | **Not found in current search** | Do not create here without placement review. |
| `schemas/contracts/v1/domains/roads-rail-trade/README.md` | **CONFIRMED parent schema lane** | Draft / PROPOSED / slug-conflicted schema index; concrete schema inventory remains **NEEDS VERIFICATION**. |
| `docs/domains/roads-rail-trade/sublanes/trade_routes.md` | **CONFIRMED documentation sublane** | Describes trade-route and historic-corridor scope, but says sublanes do not split lifecycle/schema/policy homes. |

---

## Candidate shapes

Candidate names below are proposals only and should not be treated as current files.

| Candidate schema | Likely parent lane | Status |
|---|---|---|
| `trade_route_corridor.schema.json` | `schemas/contracts/v1/domains/roads-rail-trade/` | **NEEDS VERIFICATION** |
| `historic_route_claim.schema.json` | `schemas/contracts/v1/domains/roads-rail-trade/` | **NEEDS VERIFICATION** |
| `corridor_route.schema.json` | `schemas/contracts/v1/domains/roads-rail-trade/` | **NEEDS VERIFICATION** |
| `route_membership.schema.json` | `schemas/contracts/v1/domains/roads-rail-trade/` | **NEEDS VERIFICATION** |
| `movement_story_node.schema.json` | `schemas/contracts/v1/domains/roads-rail-trade/` or docs/profile decision | **NEEDS VERIFICATION** |

---

## What belongs here

- This README.
- Compatibility notes for the flat `trade-routes/` path.
- Migration notes if this path is retained, retired, or made a profile lane.
- Pointers to the parent Roads/Rail/Trade schema lane, semantic contracts, fixtures, validators, and tests.
- Future schema files only after accepted ADR or migration review.

---

## What does not belong here

- New canonical Trade Routes schema families while the parent Roads/Rail/Trade domain schema lane remains the active home.
- Contract prose beyond README boundary notes.
- Lifecycle data, source records, catalog records, proof outputs, emitted records, release records, map artifacts, dashboards, screenshots, or generated summaries.
- Route geometry payloads, source payloads, domain data, package code, validator code, runtime code, UI/API implementation, or graph projection outputs.
- Claims that a route object is complete, reviewed, release-ready, or public-ready merely because it validates against a schema in this folder.

---

## Compatibility rules

| Rule | Requirement |
|---|---|
| Keep parent lane visible | Prefer `schemas/contracts/v1/domains/roads-rail-trade/` unless an ADR or migration note changes placement. |
| Shape is not route truth | Schema validation constrains object shape; it does not prove route claims. |
| Sublane is not new root | Documentation sublanes must not split schema, data, policy, or release homes without governance review. |
| Roots remain separate | Schemas, contracts, docs, fixtures, tests, data, release, packages, and validators keep separate authority. |
| No parallel authority | Equivalent route, corridor, membership, network, and domain shapes must not drift across flat, domain, network, and docs lanes without migration notes. |

---

## Promotion checklist

This flat Trade Routes path should not advance beyond compatibility posture unless:

- [ ] Placement is resolved: this lane, parent domain lane, network lane, or another approved profile lane.
- [ ] Relationship to `schemas/contracts/v1/domains/roads-rail-trade/` is documented.
- [ ] Sublane terminology and path convention are accepted or migrated.
- [ ] Paired semantic contracts exist or approved profiles are documented.
- [ ] Required fields are defined for any schema added here.
- [ ] Valid and invalid fixtures exist.
- [ ] Validators and CI coverage exist.
- [ ] Migration notes exist for overlapping route, corridor, and network surfaces.

---

## Validation

```bash
find schemas/contracts/v1/trade-routes -maxdepth 4 -type f | sort

find schemas/contracts/v1/domains/roads-rail-trade schemas/contracts/v1/network schemas/contracts/v1/crossings -maxdepth 5 -type f 2>/dev/null \
  | grep -Ei 'route|corridor|trade|membership|network|crossing' \
  | sort

find schemas/contracts/v1/trade-routes -name '*.json' -print0 \
  | xargs -0 -r -I{} python -m json.tool {} >/dev/null

python tools/validate_all.py || true
pytest tests/schemas tests/contract || true
```

Replace `|| true` with fail-closed CI behavior once validator and test paths are confirmed.

---

## Rollback

Rollback for this README is ordinary Git rollback: revert the commit that changed `schemas/contracts/v1/trade-routes/README.md`.

Future schema rollback must restore `$id`, `$ref`, paired contracts, fixtures, validators, registry records, CI paths, and downstream consumers.

---

## Open questions

| Question | Status | Owner |
|---|---|---|
| Should this flat path remain empty, become a redirect/index, host a profile, or be retired? | **NEEDS VERIFICATION / ADR-sensitive** | Schema steward + Trade routes steward |
| Should trade-route schemas live only under the parent Roads/Rail/Trade domain lane? | **NEEDS VERIFICATION** | Roads/Rail/Trade steward + Schema steward |
| Which route/corridor objects need schema files first? | **NEEDS VERIFICATION** | Trade routes steward + Validation steward |
| Which fixtures prove route-claim behavior without turning a geometry into authority? | **NEEDS VERIFICATION** | Validation steward |

---

## Maintainer notes

- Keep this folder in compatibility posture until schema-home placement is resolved.
- Do not add canonical schemas here while the parent Roads/Rail/Trade domain lane remains the active schema home unless ADR or migration notes explicitly allow it.
- Keep lifecycle records, emitted records, code, and release records outside `schemas/`.
