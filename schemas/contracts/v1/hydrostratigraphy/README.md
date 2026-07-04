# `schemas/contracts/v1/hydrostratigraphy/` — Hydrostratigraphy Schema Placement Guardrail

<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/schemas-contracts-v1-hydrostratigraphy-readme
title: schemas/contracts/v1/hydrostratigraphy/ — Hydrostratigraphy Schema Placement Guardrail
type: readme; schema-alias-index; cross-domain-placement-guardrail; geology-hydrology-boundary
authority_class: placement-guardrail
version: v0.1
status: draft; empty-alias-index; cross-domain-home-unsettled; geology-home-currently-surfaced; hydrology-adjacent; no-current-root-schema-files-found; do-not-promote-without-ADR; NEEDS VERIFICATION before promotion
owners:
  - OWNER_TBD — Geology domain steward
  - OWNER_TBD — Hydrology domain steward
  - OWNER_TBD — Hydrostratigraphy steward
  - OWNER_TBD — Schema steward
  - OWNER_TBD — Contract steward
  - OWNER_TBD — Policy steward
  - OWNER_TBD — Release steward
  - OWNER_TBD — Validation steward
  - OWNER_TBD — Docs steward
created: NEEDS VERIFICATION — empty README existed before v0.1 expansion
updated: 2026-07-04
policy_label: public; schemas; contracts-v1; hydrostratigraphy; cross-domain; geology-adjacent; hydrology-adjacent; aquifer; confining-unit; groundwater; well-log; borehole; evidence-bound; release-gated; rollback-aware; no-parallel-authority
tags: [kfm, schemas, contracts, v1, hydrostratigraphy, hydrostratigraphic-unit, aquifer, confining-unit, groundwater, geology, hydrology, well-log, borehole, cross-domain, placement-guardrail, no-parallel-authority]
related:
  - ../README.md
  - ../domains/README.md
  - ../domains/geology/README.md
  - ../domains/geology/hydrostratigraphic_unit.schema.json
  - ../domains/hydrology/README.md
  - ../domains/hydrology/groundwater_well.schema.json
  - ../domains/hydrology/water_level_observation.schema.json
  - ../../../../docs/domains/geology/FILE_SYSTEM_PLAN.md
  - ../../../../docs/domains/geology/OBJECT_FAMILIES.md
  - ../../../../docs/domains/geology/EXPANSION_PLAN.md
  - ../../../../contracts/domains/geology/
  - ../../../../contracts/domains/hydrology/
  - ../../../../policy/domains/geology/
  - ../../../../policy/domains/hydrology/
  - ../../../../fixtures/domains/geology/
  - ../../../../fixtures/domains/hydrology/
  - ../../../../tests/domains/geology/
  - ../../../../tests/domains/hydrology/
  - ../../../../release/candidates/geology/
  - ../../../../release/candidates/hydrology/
notes:
  - "Expanded from an empty file at schemas/contracts/v1/hydrostratigraphy/README.md."
  - "Current GitHub search did not surface schema files directly under schemas/contracts/v1/hydrostratigraphy/ beyond this README in the current check."
  - "The closest confirmed schema is schemas/contracts/v1/domains/geology/hydrostratigraphic_unit.schema.json, which is a PROPOSED scaffold with empty properties and additionalProperties true."
  - "Hydrology schema search surfaced groundwater_well.schema.json and water_level_observation.schema.json under schemas/contracts/v1/domains/hydrology/, making this path hydrology-adjacent."
  - "This README is a placement guardrail only; it must not become a parallel canonical Hydrostratigraphy schema home without ADR or migration note."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

![status](https://img.shields.io/badge/status-draft-yellow)
![root](https://img.shields.io/badge/root-schemas%2F-blue)
![family](https://img.shields.io/badge/family-hydrostratigraphy-cyan)
![posture](https://img.shields.io/badge/posture-placement__guardrail-orange)
![canonical](https://img.shields.io/badge/canonical-NEEDS__ADR-yellow)
![truth](https://img.shields.io/badge/truth-cite--or--abstain-success)

> **Purpose.** `schemas/contracts/v1/hydrostratigraphy/` is an empty top-level guardrail README for the unresolved Hydrostratigraphy schema-home question.
>
> **One-line boundary.** Current Hydrostratigraphy-like schema shape was surfaced under `schemas/contracts/v1/domains/geology/hydrostratigraphic_unit.schema.json`; this top-level path must not become a parallel canonical schema home without an accepted ADR or migration plan.

---

## Quick jumps

[Status](#status) · [Placement decision](#placement-decision) · [Repo fit](#repo-fit) · [Current inventory](#current-inventory) · [Related surfaced schemas](#related-surfaced-schemas) · [What belongs here](#what-belongs-here) · [What does not belong here](#what-does-not-belong-here) · [Migration rules](#migration-rules) · [Validation](#validation) · [Rollback](#rollback) · [Open questions](#open-questions)

---

## Status

| Question | Answer | Truth label |
|---|---|---|
| Does this README path exist? | Yes: `schemas/contracts/v1/hydrostratigraphy/README.md`. It was empty before this expansion. | **CONFIRMED** |
| Are schema files currently present directly under `schemas/contracts/v1/hydrostratigraphy/`? | Not found in the current GitHub search beyond this README. | **NEEDS VERIFICATION / search-limited** |
| Where is the closest confirmed Hydrostratigraphy-like schema? | `schemas/contracts/v1/domains/geology/hydrostratigraphic_unit.schema.json`. | **CONFIRMED path evidence** |
| Is the closest schema mature? | No. It is a `PROPOSED` scaffold with empty properties and `additionalProperties: true`. | **CONFIRMED scaffold** |
| Is Hydrostratigraphy cross-domain? | Yes, by responsibility: it is geology-owned shape in current evidence and hydrology-adjacent for groundwater/well/water-level use. | **PROPOSED / evidence-supported** |
| Can this top-level folder become canonical now? | Not without ADR, steward decision, migration note, fixtures, validators, and consumer update plan. | **NEEDS VERIFICATION** |

> [!IMPORTANT]
> Hydrostratigraphy sits between geology and hydrology. Do not duplicate `hydrostratigraphic_unit` here while the Geology domain lane already contains a scaffold, and do not use this folder to replace Hydrology groundwater, well, observation, or water-level schema authority.

---

## Placement decision

Current placement posture:

```text
Empty top-level guardrail path:
  schemas/contracts/v1/hydrostratigraphy/

Closest surfaced schema home:
  schemas/contracts/v1/domains/geology/hydrostratigraphic_unit.schema.json

Hydrology-adjacent schema lane:
  schemas/contracts/v1/domains/hydrology/
```

Rationale:

- Domain-specific schema placement normally belongs under `schemas/contracts/v1/domains/<domain>/...` unless an accepted exception says otherwise.
- Search did not find files directly under `schemas/contracts/v1/hydrostratigraphy/`.
- Search did find `hydrostratigraphic_unit.schema.json` under the Geology domain lane.
- Search also surfaced Hydrology groundwater-adjacent schemas such as `groundwater_well.schema.json` and `water_level_observation.schema.json` under the Hydrology domain lane.
- A top-level Hydrostratigraphy family may be reasonable later, but it is not confirmed as the accepted schema home in this session.

---

## Repo fit

```text
schemas/
└── contracts/
    └── v1/
        ├── README.md
        ├── hydrostratigraphy/
        │   └── README.md                         # this file; placement guardrail only
        └── domains/
            ├── geology/
            │   ├── README.md
            │   └── hydrostratigraphic_unit.schema.json
            └── hydrology/
                ├── README.md
                ├── groundwater_well.schema.json
                └── water_level_observation.schema.json

contracts/
├── domains/geology/                               # semantic meaning; not machine shape
└── domains/hydrology/                             # semantic meaning; not machine shape

policy/
fixtures/
tests/
release/
```

---

## Current inventory

| Path | Status | Note |
|---|---|---|
| `schemas/contracts/v1/hydrostratigraphy/README.md` | **CONFIRMED present** | Empty file expanded by this README. |
| `schemas/contracts/v1/hydrostratigraphy/*.schema.json` | **Not found in current search** | Do not create here without ADR or migration note. |
| `schemas/contracts/v1/domains/geology/hydrostratigraphic_unit.schema.json` | **CONFIRMED present** | PROPOSED scaffold; empty `properties`; `additionalProperties: true`. |
| `schemas/contracts/v1/domains/geology/README.md` | **CONFIRMED present** | Geology alias README inventory records `hydrostratigraphic_unit.schema.json` as hydrology-adjacent and NEEDS VERIFICATION. |
| `schemas/contracts/v1/domains/hydrology/README.md` | **CONFIRMED surfaced by search** | Hydrology domain schema index; not opened in this edit. |
| `schemas/contracts/v1/domains/hydrology/groundwater_well.schema.json` | **CONFIRMED surfaced by search** | Groundwater-adjacent Hydrology schema; field maturity not inspected. |
| `schemas/contracts/v1/domains/hydrology/water_level_observation.schema.json` | **CONFIRMED surfaced by search** | Water-level observation schema; field maturity not inspected. |

---

## Related surfaced schemas

Current search surfaced these relevant schema paths:

| Surfaced path | Role signal | Posture |
|---|---|---|
| `schemas/contracts/v1/domains/geology/hydrostratigraphic_unit.schema.json` | Hydrostratigraphic unit shape. | **PROPOSED scaffold / cross-domain boundary** |
| `schemas/contracts/v1/domains/hydrology/groundwater_well.schema.json` | Groundwater well shape. | **NEEDS VERIFICATION / hydrology-owned** |
| `schemas/contracts/v1/domains/hydrology/water_level_observation.schema.json` | Water-level observation shape. | **NEEDS VERIFICATION / hydrology-owned** |
| `schemas/contracts/v1/domains/geology/borehole_reference.schema.json` | Borehole reference shape. | **NEEDS VERIFICATION / geology-owned** |
| `schemas/contracts/v1/domains/geology/well_log_reference.schema.json` | Well-log reference shape. | **NEEDS VERIFICATION / geology-owned** |

> [!CAUTION]
> The presence of these files does not prove field completeness, accepted schema status, fixture coverage, validator wiring, policy behavior, release readiness, or public API readiness.

---

## What belongs here

- This README.
- Alias, migration, mirror, deprecation, or schema-home conflict notes for `schemas/contracts/v1/hydrostratigraphy/`.
- Pointers to the accepted Hydrostratigraphy schema home once settled.
- Drift notes explaining why schema files should not be added directly here without review.

---

## What does not belong here

- Canonical Hydrostratigraphy JSON Schema files unless an accepted ADR/migration authorizes this path.
- Duplicate Geology schemas already owned by `schemas/contracts/v1/domains/geology/`.
- Duplicate Hydrology schemas already owned by `schemas/contracts/v1/domains/hydrology/`.
- Semantic contract prose.
- Policy rules, sensitivity decisions, exposure decisions, or release decisions.
- Lifecycle data, source registry records, well logs, borehole files, groundwater observation records, catalog records, triplets, receipt instances, proof outputs, release records, correction notices, rollback cards, or public artifacts.
- Validator code, packages, pipelines, runtime code, UI/API implementation, map tiles, dashboards, screenshots, or generated summaries.
- Claims that a hydrostratigraphy object is complete, authoritative, or public-ready merely because it validates against a schema.

---

## Migration rules

Do not move or duplicate Hydrostratigraphy schemas into this top-level path unless a reviewed migration plan defines:

- source path;
- target path;
- owning root;
- reason for migration;
- schema `$id` changes;
- `$ref` and consumer updates;
- fixture and validator updates;
- schema registry updates;
- policy review;
- release and rollback impact;
- Geology/Hydrology domain impacts;
- deprecation/mirror window;
- tests proving no parallel authority remains.

---

## Validation

Recommended local validation sequence:

```bash
# Confirm this guardrail path remains README-only unless migration is authorized.
find schemas/contracts/v1/hydrostratigraphy -maxdepth 2 -type f | sort

# Inspect related Geology and Hydrology schema lanes.
find schemas/contracts/v1/domains/geology schemas/contracts/v1/domains/hydrology -maxdepth 3 -type f \
  | grep -Ei 'hydrostrat|groundwater|well_log|borehole|water_level|README' \
  | sort

# Detect duplicate hydrostratigraphy authority.
find schemas/contracts/v1 -maxdepth 6 -type f \
  | grep -Ei 'hydrostrat|groundwater|well_log|borehole|water_level' \
  | sort

# Validate JSON syntax for related schemas.
find schemas/contracts/v1/domains/geology schemas/contracts/v1/domains/hydrology -name '*.schema.json' -print0 \
  | xargs -0 -r -I{} python -m json.tool {} >/dev/null

# Run project validators when available.
python tools/validate_all.py || true
pytest tests/schemas tests/contract tests/domains/geology tests/domains/hydrology tests/policy || true
```

Replace `|| true` with fail-closed CI behavior once validator and test paths are confirmed.

---

## Rollback

Rollback for this README is ordinary Git rollback: revert the commit that changed `schemas/contracts/v1/hydrostratigraphy/README.md`.

Rollback for any future migration into this path requires checking every downstream reference:

1. Revert or migrate schema files.
2. Restore canonical `$id` and `$ref` targets.
3. Restore paired contract links.
4. Restore fixtures, validators, schema registry records, and CI paths.
5. Restore Geology, Hydrology, policy, evidence, release, and receipt references.
6. Restore API/UI/MapLibre/Evidence Drawer consumers.
7. Preserve correction and rollback records if any public hydrostratigraphy surface was affected.

---

## Open questions

| Question | Status | Owner |
|---|---|---|
| Should `schemas/contracts/v1/hydrostratigraphy/` become an accepted cross-domain schema family or remain README-only? | **NEEDS VERIFICATION / ADR-sensitive** | Schema steward + Geology steward + Hydrology steward |
| Should `hydrostratigraphic_unit.schema.json` remain under Geology or be migrated/profiled into a cross-domain family? | **NEEDS VERIFICATION / migration-sensitive** | Geology steward + Hydrology steward |
| Which contract path should own hydrostratigraphic unit semantics? | **NEEDS VERIFICATION** | Contract steward |
| Which fixtures prove distinction between hydrostratigraphic unit, aquifer, well, borehole, and water-level observation? | **NEEDS VERIFICATION** | Validation steward |
| Which hydrostratigraphy-derived surfaces are safe for public API/MapLibre/Focus Mode use? | **NEEDS VERIFICATION / release-gated** | Release steward + Policy steward |

---

## Maintainer notes

- Keep this path README-only until the Hydrostratigraphy schema-home question is resolved.
- Do not let `schemas/contracts/v1/hydrostratigraphy/` duplicate Geology or Hydrology schema authority.
- Preserve evidence, uncertainty, cross-domain ownership, policy, release, correction, and rollback boundaries for all Hydrostratigraphy surfaces.
