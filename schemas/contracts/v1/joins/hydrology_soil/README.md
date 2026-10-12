# `schemas/contracts/v1/joins/hydrology_soil/` — Hydrology–Soil Join Schema Guardrail

<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/schemas-contracts-v1-joins-hydrology-soil-readme
title: schemas/contracts/v1/joins/hydrology_soil/ — Hydrology–Soil Join Schema Guardrail
type: readme; join-schema-index; cross-domain-guardrail; hydrology-soil-boundary
authority_class: join-schema-guardrail
version: v0.1
status: draft; empty-join-lane; hydrology-domain-present; soil-domain-present; no-current-join-schema-files-found; do-not-promote-without-ADR; NEEDS VERIFICATION before promotion
owners:
  - OWNER_TBD — Hydrology domain steward
  - OWNER_TBD — Soil domain steward
  - OWNER_TBD — Join steward
  - OWNER_TBD — Schema steward
  - OWNER_TBD — Contract steward
  - OWNER_TBD — Policy steward
  - OWNER_TBD — Release steward
  - OWNER_TBD — Validation steward
  - OWNER_TBD — Docs steward
created: NEEDS VERIFICATION — empty README existed before v0.1 expansion
updated: 2026-07-04
policy_label: public; schemas; contracts-v1; joins; hydrology-soil; cross-domain; evidence-bound; release-gated; rollback-aware; no-parallel-authority
tags: [kfm, schemas, contracts, v1, joins, hydrology, soil, hydrology-soil, watershed, huc, gauge, hydrograph, flow-observation, soil-map-unit, soil-moisture, hydrologic-soil-group, runoff, infiltration, cross-domain, join-lane, no-parallel-authority]
related:
  - ../../README.md
  - ../README.md
  - ../../domains/README.md
  - ../../domains/hydrology/README.md
  - ../../domains/hydrology/huc_unit.schema.json
  - ../../domains/hydrology/watershed.schema.json
  - ../../domains/hydrology/gauge_site.schema.json
  - ../../domains/hydrology/hydro_feature.schema.json
  - ../../domains/hydrology/hydrograph.schema.json
  - ../../domains/hydrology/flow_observation.schema.json
  - ../../domains/soil/README.md
  - ../../domains/soil/soil_map_unit.schema.json
  - ../../domains/soil/soil_moisture_reading.schema.json
  - ../../domains/soil/soil_moisture_units_time.schema.json
  - ../../domains/soil/soil_moisture_dedupe_key.schema.json
  - ../../domains/soil/domain_feature_identity.schema.json
  - ../../../../contracts/domains/hydrology/
  - ../../../../contracts/domains/soil/
  - ../../../../docs/domains/hydrology/
  - ../../../../docs/domains/soil/
  - ../../../../policy/domains/hydrology/
  - ../../../../policy/domains/soil/
  - ../../../../fixtures/domains/hydrology/
  - ../../../../fixtures/domains/soil/
  - ../../../../tests/domains/hydrology/
  - ../../../../tests/domains/soil/
notes:
  - "Expanded from an empty file at schemas/contracts/v1/joins/hydrology_soil/README.md."
  - "Current GitHub search did not surface schema files directly under this join lane beyond this README in the current check."
  - "Hydrology domain schema files were surfaced under schemas/contracts/v1/domains/hydrology/."
  - "Soil domain schema files were surfaced under schemas/contracts/v1/domains/soil/, including soil_map_unit and soil_moisture-related schemas."
  - "This README is a join-placement guardrail only; do not create canonical join schemas here without ADR, paired contracts, fixtures, validators, and steward review."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

![status](https://img.shields.io/badge/status-draft-yellow)
![root](https://img.shields.io/badge/root-schemas%2F-blue)
![family](https://img.shields.io/badge/family-joins-purple)
![join](https://img.shields.io/badge/join-hydrology--soil-blue)
![posture](https://img.shields.io/badge/posture-guardrail-orange)
![truth](https://img.shields.io/badge/truth-cite--or--abstain-success)

> **Purpose.** `schemas/contracts/v1/joins/hydrology_soil/` is an empty guardrail README for a possible Hydrology–Soil join schema lane.
>
> **One-line boundary.** This path may only define join-shape contracts if placement is accepted; it must not replace `schemas/contracts/v1/domains/hydrology/` or `schemas/contracts/v1/domains/soil/`.

---

## Quick jumps

[Status](#status) · [Placement decision](#placement-decision) · [Repo fit](#repo-fit) · [Current inventory](#current-inventory) · [Related surfaced lanes](#related-surfaced-lanes) · [Candidate join shapes](#candidate-join-shapes) · [What belongs here](#what-belongs-here) · [What does not belong here](#what-does-not-belong-here) · [Join guardrails](#join-guardrails) · [Migration rules](#migration-rules) · [Validation](#validation) · [Rollback](#rollback) · [Open questions](#open-questions)

---

## Status

| Question | Answer | Truth label |
|---|---|---|
| Does this README path exist? | Yes: `schemas/contracts/v1/joins/hydrology_soil/README.md`. It was empty before this expansion. | **CONFIRMED** |
| Are schema files currently present under this join lane? | Not found in the current GitHub search beyond this README. | **NEEDS VERIFICATION / search-limited** |
| Are Hydrology and Soil domain schema lanes present? | Yes. Both domain schema lanes were surfaced by search; the Soil README was inspected. | **CONFIRMED path evidence** |
| Is this join lane canonical? | Not proven. Treat as guardrail/index only until ADR or steward decision. | **NEEDS VERIFICATION / ADR-sensitive** |
| Can this lane store joined data, lifecycle records, receipts, proofs, or released outputs? | No. This path is schema documentation only, not lifecycle data, emitted records, proof storage, release records, or public artifact storage. | **CONFIRMED boundary** |

> [!IMPORTANT]
> A Hydrology–Soil join schema should describe relationship shape. It must not collapse Hydrology-owned watershed, gauge, hydrograph, flow, or water-observation meaning into Soil-owned map unit, soil moisture, hydrologic soil group, component, horizon, or evidence meaning.

---

## Placement decision

Current placement posture:

```text
Requested join guardrail:
  schemas/contracts/v1/joins/hydrology_soil/

Hydrology domain schema lane:
  schemas/contracts/v1/domains/hydrology/

Soil domain schema lane:
  schemas/contracts/v1/domains/soil/
```

Rationale:

- Domain schemas normally belong under `schemas/contracts/v1/domains/<domain>/...`.
- Hydrology owns water, watershed, gauge, hydrograph, flow, reach, HUC, and water-observation shapes.
- Soil owns soil map unit, soil moisture, soil identity, Soil-specific evidence, decision, release, and rollback shapes.
- This join lane may be useful for neutral relationship shapes, but it is not confirmed as accepted in this session.
- Any future schema here must be paired with contracts, fixtures, validators, registry entries, and review across both domains.

---

## Repo fit

```text
schemas/
└── contracts/
    └── v1/
        ├── README.md
        ├── joins/
        │   └── hydrology_soil/
        │       └── README.md                     # this file; join guardrail only
        └── domains/
            ├── hydrology/
            │   ├── README.md
            │   ├── huc_unit.schema.json
            │   ├── watershed.schema.json
            │   ├── gauge_site.schema.json
            │   ├── hydro_feature.schema.json
            │   └── hydrograph.schema.json
            └── soil/
                ├── README.md
                ├── soil_map_unit.schema.json
                ├── soil_moisture_reading.schema.json
                ├── soil_moisture_units_time.schema.json
                └── soil_moisture_dedupe_key.schema.json

contracts/
├── domains/hydrology/                             # semantic meaning; not machine shape
└── domains/soil/                                  # semantic meaning; not machine shape

policy/
fixtures/
tests/
release/
```

---

## Current inventory

| Path | Status | Note |
|---|---|---|
| `schemas/contracts/v1/joins/hydrology_soil/README.md` | **CONFIRMED present** | Empty file expanded by this README. |
| `schemas/contracts/v1/joins/hydrology_soil/*.schema.json` | **Not found in current search** | Do not create here without ADR, paired contracts, and validation plan. |
| `schemas/contracts/v1/domains/hydrology/README.md` | **CONFIRMED inspected** | Hydrology domain schema lane. |
| `schemas/contracts/v1/domains/soil/README.md` | **CONFIRMED inspected** | Soil domain schema lane. |
| Hydrology schema files | **CONFIRMED surfaced by search** | Includes watershed/HUC/gauge/hydrograph/flow/water observation/support schemas. |
| Soil schema files | **CONFIRMED surfaced by search** | Includes soil map unit, soil moisture, SSURGO source descriptor, identity, release, rollback, correction, decision, receipt, evidence, and support schemas. |

---

## Related surfaced lanes

| Path | Role signal | Posture |
|---|---|---|
| `schemas/contracts/v1/domains/hydrology/` | Hydrology-owned machine shape lane. | **PROPOSED / active domain lane** |
| `schemas/contracts/v1/domains/soil/` | Soil-owned machine shape lane. | **DRAFT / scaffolded schema lane** |
| `schemas/contracts/v1/joins/hydrology_soil/` | Possible neutral join schema lane. | **README-only guardrail** |

---

## Candidate join shapes

Candidate join schemas below require steward review, paired contracts, fixtures, validators, registry records, and release/policy review before promotion.

| Candidate schema | Purpose | Default posture |
|---|---|---|
| `hydrology_soil_join.schema.json` | Generic relationship between Hydrology feature refs and Soil feature refs. | **PROPOSED / not created** |
| `watershed_soil_context.schema.json` | Relationship shape between watershed/HUC refs and soil map unit or soil feature refs. | **PROPOSED / evidence-bound** |
| `soil_moisture_hydro_context.schema.json` | Relationship shape between soil moisture readings and Hydrology context refs. | **PROPOSED / time-sensitive** |
| `runoff_soil_context.schema.json` | Relationship shape for runoff/infiltration modeling context using Hydrology and Soil references. | **PROPOSED / model-sensitive** |
| `hydrology_soil_release_projection.schema.json` | Public/release projection for already-governed join outputs. | **PROPOSED / release-gated** |

> [!CAUTION]
> Candidate names are proposals only. Do not treat them as repo files, accepted contracts, or implementation proof until created, paired, fixture-tested, and reviewed.

---

## What belongs here

- This README.
- Join schema placement notes for Hydrology–Soil relationships.
- Future neutral join schema files if an accepted ADR or migration plan authorizes this lane.
- Links to paired contracts, fixtures, validators, schema registry records, policy references, release references, and tests.
- Drift notes preventing duplicate Hydrology or Soil schema authority.

---

## What does not belong here

- Hydrology-owned canonical schemas.
- Soil-owned canonical schemas.
- Semantic contract prose.
- Policy rules, exposure decisions, or release decisions.
- Lifecycle data, joined datasets, source records, catalog records, triplets, receipt instances, proof outputs, release records, correction notices, rollback cards, or public artifacts.
- Validator code, packages, pipelines, runtime code, UI/API implementation, map tiles, dashboards, screenshots, or generated summaries.
- Claims that a join is valid, complete, true, current, or public-ready merely because it validates against a schema.

---

## Join guardrails

| Boundary | Requirement |
|---|---|
| Domain ownership | Hydrology and Soil keep their own canonical shapes and semantic contracts. |
| Join neutrality | A join schema records relationship shape, not source truth for either side. |
| Reference discipline | Use stable references to domain-owned objects rather than duplicating domain fields. |
| Time discipline | Join outputs should preserve observation, measurement, retrieval, release, and correction time where applicable. |
| Evidence dependency | Join outputs need EvidenceBundle or equivalent support where claims depend on evidence. |
| Policy dependency | Joins that affect release, access, or public display must carry policy posture. |
| Release dependency | Public join projections must be release-gated and rollback-aware. |
| No parallel authority | Do not maintain identical join schema definitions under `joins/` and either domain lane without a mirror/migration rule. |

---

## Migration rules

Do not move or duplicate join schemas into this path unless a reviewed migration plan defines:

- source path;
- target path;
- owning root;
- reason for migration;
- schema `$id` changes;
- `$ref` and consumer updates;
- fixture and validator updates;
- schema registry updates;
- Hydrology and Soil steward review;
- policy review;
- release and rollback impact;
- deprecation/mirror window;
- tests proving no parallel authority remains.

---

## Validation

Recommended local validation sequence:

```bash
# Confirm this join lane remains README-only unless authorized.
find schemas/contracts/v1/joins/hydrology_soil -maxdepth 2 -type f | sort

# Inspect Hydrology/Soil related schema lanes.
find schemas/contracts/v1/domains/hydrology schemas/contracts/v1/domains/soil -maxdepth 4 -type f \
  | grep -Ei 'huc|watershed|gauge|hydrograph|flow|water|soil|moisture|ssurgo|map_unit|README' \
  | sort

# Detect duplicate hydrology-soil join authority.
find schemas/contracts/v1 -maxdepth 6 -type f \
  | grep -Ei 'hydrology.*soil|soil.*hydrology|watershed.*soil|soil.*watershed|moisture.*hydro|hydro.*moisture|runoff.*soil|soil.*runoff' \
  | sort

# Validate JSON syntax for related domain schemas.
find schemas/contracts/v1/domains/hydrology schemas/contracts/v1/domains/soil -name '*.schema.json' -print0 \
  | xargs -0 -r -I{} python -m json.tool {} >/dev/null

# Run project validators when available.
python tools/validate_all.py || true
pytest tests/schemas tests/contract tests/domains/hydrology tests/domains/soil tests/policy || true
```

Replace `|| true` with fail-closed CI behavior once validator and test paths are confirmed.

---

## Rollback

Rollback for this README is ordinary Git rollback: revert the commit that changed `schemas/contracts/v1/joins/hydrology_soil/README.md`.

Rollback for future join schema changes requires checking every downstream reference:

1. Revert or migrate schema files.
2. Restore canonical `$id` and `$ref` targets.
3. Restore paired contract links.
4. Restore fixtures, validators, schema registry records, and CI paths.
5. Restore Hydrology, Soil, policy, evidence, release, and receipt references.
6. Restore API/UI/MapLibre/Evidence Drawer consumers.
7. Preserve correction and rollback records if any public join surface was affected.

---

## Open questions

| Question | Status | Owner |
|---|---|---|
| Should Hydrology–Soil relationships live under `joins/`, a Hydrology extension, a Soil extension, or another cross-domain lane? | **NEEDS VERIFICATION / ADR-sensitive** | Schema steward + Hydrology steward + Soil steward |
| Should the slug be `hydrology_soil`, `hydrology-soil`, `soil-hydrology`, or another convention? | **NEEDS VERIFICATION / ADR-sensitive** | Schema steward + Join steward |
| Which contract lane should own neutral join semantics? | **NEEDS VERIFICATION** | Contract steward |
| Which fixtures prove that joins do not duplicate domain-owned fields? | **NEEDS VERIFICATION** | Validation steward |
| Which join projections are safe for public API/MapLibre/Focus Mode use? | **NEEDS VERIFICATION / release-gated** | Release steward + Policy steward |

---

## Maintainer notes

- Keep this path README-only until the join-home decision is resolved.
- Prefer references to Hydrology and Soil domain objects over copied fields.
- Do not let this join lane duplicate Hydrology or Soil schema authority.
- Preserve evidence, time, ownership, policy, release, correction, and rollback boundaries for all Hydrology–Soil join surfaces.
