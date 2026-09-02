# `schemas/contracts/v1/transport/` — Transport Schema Compatibility Index

<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/schemas-contracts-v1-transport-readme
title: schemas/contracts/v1/transport/ — Transport Schema Compatibility Index
type: readme; compatibility-index; schema-boundary; roads-rail-trade-placement-guardrail
authority_class: schema-family-guardrail
version: v0.2
status: draft; flat-transport-compatibility-path; roads-rail-decision-envelope-scaffold-present; roads-rail-trade-domain-lane-present; slug-conflict-visible; PROPOSED; NEEDS VERIFICATION before promotion
owners:
  - OWNER_TBD — Roads/Rail/Trade domain steward
  - OWNER_TBD — Transport compatibility steward
  - OWNER_TBD — Schema steward
  - OWNER_TBD — Contract steward
  - OWNER_TBD — Validation steward
  - OWNER_TBD — Docs steward
created: NEEDS VERIFICATION — scaffold existed before v0.2 expansion
updated: 2026-07-04
policy_label: public; schemas; contracts-v1; transport; roads-rail-trade; compatibility-path; schema-boundary; no-parallel-authority
tags: [kfm, schemas, contracts, v1, transport, roads-rail-trade, roads, rail, trade-routes, decision-envelope, compatibility, no-parallel-authority]
related:
  - ../README.md
  - ./roads_rail_decision_envelope.schema.json
  - ../domains/roads-rail-trade/README.md
  - ../trade-routes/README.md
  - ../network/README.md
  - ../crossings/README.md
  - ../../../../docs/domains/roads-rail-trade/README.md
  - ../../../../docs/domains/roads-rail-trade/sublanes/trade_routes.md
  - ../../../../contracts/domains/roads-rail-trade/
  - ../../../../fixtures/
  - ../../../../tests/
notes:
  - "Expanded from a short scaffold at schemas/contracts/v1/transport/README.md."
  - "Current GitHub search surfaced roads_rail_decision_envelope.schema.json directly under this flat transport path."
  - "The inspected roads_rail_decision_envelope.schema.json is a PROPOSED empty scaffold with empty properties, additionalProperties true, and contract_doc null."
  - "schemas/contracts/v1/domains/roads-rail-trade/README.md records unresolved roads-rail-trade vs transport and domains/ vs flat-path drift."
  - "This flat transport path is a compatibility index only and must not become parallel canonical schema authority without ADR or migration review."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

![status](https://img.shields.io/badge/status-draft-yellow)
![root](https://img.shields.io/badge/root-schemas%2F-blue)
![family](https://img.shields.io/badge/family-transport-slategray)
![posture](https://img.shields.io/badge/posture-compatibility-orange)
![truth](https://img.shields.io/badge/truth-cite--or--abstain-success)

> **Purpose.** `schemas/contracts/v1/transport/` is a flat compatibility index for transport-related schema placement that overlaps the Roads / Rail / Trade domain lane.
>
> **One-line boundary.** This path defines machine-checkable shape only if accepted. It does not replace `schemas/contracts/v1/domains/roads-rail-trade/`, store transport data, create registry records, publish artifacts, or resolve the transport-vs-roads-rail-trade slug conflict by itself.

---

## Status

| Question | Answer | Truth label |
|---|---|---|
| Does this README path exist? | Yes. It was a short scaffold before this expansion. | **CONFIRMED** |
| Are schema files present directly under this flat path? | Yes. Search surfaced `roads_rail_decision_envelope.schema.json`. | **CONFIRMED path presence** |
| Is the direct schema field-complete? | Not proven. The inspected schema is a PROPOSED empty scaffold with empty `properties`, `additionalProperties: true`, and `contract_doc: null`. | **CONFIRMED scaffold / NEEDS VERIFICATION** |
| Is there an inspected Roads/Rail/Trade domain schema lane? | Yes. `schemas/contracts/v1/domains/roads-rail-trade/README.md` is the inspected parent domain schema index. | **CONFIRMED path evidence** |
| Is transport the confirmed canonical slug? | No. The inspected domain README records unresolved `roads-rail-trade` vs `transport` and `domains/` vs flat-path drift. | **CONFIRMED conflict / NEEDS VERIFICATION** |
| Can this flat folder store lifecycle data, source records, proofs, catalog records, release records, runtime code, map products, or transport payloads? | No. This is a schema compatibility folder and may only define machine-checkable shape if accepted here later. | **CONFIRMED boundary** |

---

## Authority and placement

Current placement posture:

```text
schemas/contracts/v1/transport/                       # this flat compatibility lane
schemas/contracts/v1/transport/roads_rail_decision_envelope.schema.json
schemas/contracts/v1/domains/roads-rail-trade/        # inspected parent domain schema lane
schemas/contracts/v1/trade-routes/                    # flat trade-routes compatibility guardrail
contracts/domains/roads-rail-trade/                   # semantic meaning; not schema shape
```

Adjacent authority remains separate:

- `schemas/contracts/v1/domains/roads-rail-trade/` owns the parent Roads/Rail/Trade schema lane unless an ADR or migration note says otherwise.
- `contracts/domains/roads-rail-trade/` owns semantic meaning.
- `docs/domains/roads-rail-trade/` owns human-facing domain documentation and placement notes.
- `fixtures/` and `tests/` prove examples and behavior where present.
- `data/` owns lifecycle records and emitted data products where present.
- `release/` owns release records where present.

This README does not amend ADR-0001, Directory Rules, transport slug governance, Roads/Rail/Trade placement, validators, or release gates.

---

## Repo fit

```text
schemas/
└── contracts/
    └── v1/
        ├── transport/
        │   ├── README.md                         # this file; flat compatibility index
        │   └── roads_rail_decision_envelope.schema.json
        ├── trade-routes/
        │   └── README.md                         # flat compatibility guardrail
        └── domains/
            └── roads-rail-trade/
                └── README.md                     # parent domain schema index

docs/
└── domains/
    └── roads-rail-trade/                          # domain docs and placement notes

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
| `schemas/contracts/v1/transport/README.md` | **CONFIRMED present** | Scaffold expanded by this README. |
| `schemas/contracts/v1/transport/roads_rail_decision_envelope.schema.json` | **PROPOSED empty scaffold** | Draft 2020-12 object; `$id` is `kfm://schemas/contracts/v1/transport/roads_rail_decision_envelope.schema.json`; empty `properties`; `additionalProperties: true`; source doc points to `docs/domains/roads-rail-trade/API_CONTRACTS.md`; `contract_doc: null`. |
| `schemas/contracts/v1/domains/roads-rail-trade/README.md` | **CONFIRMED parent schema lane** | Draft / PROPOSED / slug-conflicted schema index; records `roads-rail-trade` vs `transport` and `domains/` vs flat-path drift. |
| `schemas/contracts/v1/trade-routes/README.md` | **CONFIRMED compatibility guardrail** | Flat trade-routes path is compatibility-only and points back to the parent domain lane. |

---

## Drift risks

| Risk | Evidence signal | Required posture |
|---|---|---|
| Flat transport vs domain lane | `transport/` exists with a scaffold, while `domains/roads-rail-trade/` is the inspected domain schema lane. | **Needs migration decision** |
| Slug conflict | Roads/Rail/Trade documentation records `roads-rail-trade` vs `transport` conflict. | **Keep conflict visible** |
| Empty scaffold maturity | `roads_rail_decision_envelope.schema.json` has no fields yet. | **Do not imply validator-ready schema** |
| Flat sibling overlap | `trade-routes/` also exists as a flat compatibility guardrail. | **Avoid parallel schema authority** |
| Decision-envelope placement | Decision-envelope shapes may overlap runtime, governance, review, or domain schema lanes. | **Needs placement review** |

---

## What belongs here

- This README.
- Compatibility notes for the flat `transport/` path.
- The current `roads_rail_decision_envelope.schema.json` scaffold until placement is resolved.
- Migration notes if this path is retained, retired, or made a profile lane.
- Pointers to the parent Roads/Rail/Trade schema lane, semantic contracts, fixtures, validators, and tests.
- Future schema files only after accepted ADR or migration review.

---

## What does not belong here

- New canonical transport schema families while the parent Roads/Rail/Trade domain schema lane remains the active home.
- Contract prose beyond README boundary notes.
- Lifecycle data, source records, catalog records, proof outputs, emitted records, release records, map artifacts, dashboards, screenshots, or generated summaries.
- Road, rail, route, corridor, facility, source payload, package code, validator code, runtime code, UI/API implementation, or graph projection outputs.
- Claims that a transport object or decision envelope is complete, reviewed, release-ready, or public-ready merely because it validates against a schema in this folder.

---

## Compatibility rules

| Rule | Requirement |
|---|---|
| Keep parent lane visible | Prefer `schemas/contracts/v1/domains/roads-rail-trade/` unless an ADR or migration note changes placement. |
| Shape is not domain truth | Schema validation constrains object shape; it does not prove transport, road, rail, route, or corridor claims. |
| Flat path is not a shortcut | `transport/` must not bypass domain, contract, fixture, validator, data, or release responsibilities. |
| Decision envelope needs placement review | Decision-envelope schemas should be checked against domain, runtime, governance, and review families before promotion. |
| Roots remain separate | Schemas, contracts, docs, fixtures, tests, data, release, packages, and validators keep separate authority. |
| No parallel authority | Equivalent transport, roads-rail-trade, route, corridor, network, and decision-envelope shapes must not drift across flat, domain, runtime, governance, and docs lanes without migration notes. |

---

## Promotion checklist

This flat Transport path should not advance beyond compatibility posture unless:

- [ ] Placement is resolved: this lane, parent domain lane, runtime/governance/review lane, or another approved profile lane.
- [ ] Relationship to `schemas/contracts/v1/domains/roads-rail-trade/` is documented.
- [ ] `transport` vs `roads-rail-trade` slug decision is documented.
- [ ] Paired semantic contracts exist or approved profiles are documented.
- [ ] Required fields are defined for any schema added here.
- [ ] Valid and invalid fixtures exist.
- [ ] Validators and CI coverage exist.
- [ ] Migration notes exist for overlapping transport, route, corridor, network, and decision-envelope surfaces.

---

## Validation

```bash
find schemas/contracts/v1/transport -maxdepth 4 -type f | sort

find schemas/contracts/v1/transport schemas/contracts/v1/domains/roads-rail-trade schemas/contracts/v1/trade-routes schemas/contracts/v1/network schemas/contracts/v1/crossings -maxdepth 5 -type f 2>/dev/null \
  | grep -Ei 'transport|road|rail|route|corridor|trade|decision|network|crossing' \
  | sort

find schemas/contracts/v1/transport -name '*.json' -print0 \
  | xargs -0 -r -I{} python -m json.tool {} >/dev/null

python tools/validate_all.py || true
pytest tests/schemas tests/contract || true
```

Replace `|| true` with fail-closed CI behavior once validator and test paths are confirmed.

---

## Rollback

Rollback for this README is ordinary Git rollback: revert the commit that changed `schemas/contracts/v1/transport/README.md`.

Future schema rollback must restore `$id`, `$ref`, paired contracts, fixtures, validators, registry records, CI paths, and downstream consumers.

---

## Open questions

| Question | Status | Owner |
|---|---|---|
| Should `transport/` remain a flat compatibility lane, become a profile lane, or be retired? | **NEEDS VERIFICATION / ADR-sensitive** | Schema steward + Roads/Rail/Trade steward |
| Should canonical schemas live only under `schemas/contracts/v1/domains/roads-rail-trade/`? | **NEEDS VERIFICATION** | Roads/Rail/Trade steward + Schema steward |
| Where should `roads_rail_decision_envelope.schema.json` live if it matures? | **NEEDS VERIFICATION / placement-sensitive** | Schema steward + Contract steward |
| Which fixtures prove decision-envelope behavior without creating parallel domain authority? | **NEEDS VERIFICATION** | Validation steward |

---

## Maintainer notes

- Keep this folder in compatibility posture until schema-home placement is resolved.
- Do not add canonical schemas here while the parent Roads/Rail/Trade domain lane remains the active schema home unless ADR or migration notes explicitly allow it.
- Keep lifecycle records, emitted records, code, and release records outside `schemas/`.
