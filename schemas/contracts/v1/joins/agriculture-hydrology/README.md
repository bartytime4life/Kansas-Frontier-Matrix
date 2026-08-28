# `schemas/contracts/v1/joins/agriculture-hydrology/` — Agriculture–Hydrology Join Schema Guardrail

<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/schemas-contracts-v1-joins-agriculture-hydrology-readme
title: schemas/contracts/v1/joins/agriculture-hydrology/ — Agriculture–Hydrology Join Schema Guardrail
type: readme; join-schema-index; cross-domain-guardrail; agriculture-hydrology-boundary
authority_class: join-schema-guardrail
version: v0.1
status: draft; empty-join-lane; agriculture-extension-already-present; hydrology-adjacent; no-current-join-schema-files-found; do-not-promote-without-ADR; NEEDS VERIFICATION before promotion
owners:
  - OWNER_TBD — Agriculture domain steward
  - OWNER_TBD — Hydrology domain steward
  - OWNER_TBD — Join steward
  - OWNER_TBD — Schema steward
  - OWNER_TBD — Contract steward
  - OWNER_TBD — Policy steward
  - OWNER_TBD — Release steward
  - OWNER_TBD — Validation steward
  - OWNER_TBD — Docs steward
created: NEEDS VERIFICATION — empty README existed before v0.1 expansion
updated: 2026-07-04
policy_label: public; schemas; contracts-v1; joins; agriculture-hydrology; cross-domain; extension-aware; evidence-bound; release-gated; rollback-aware; no-parallel-authority
tags: [kfm, schemas, contracts, v1, joins, agriculture, hydrology, agriculture-hydrology, hydrology-ext, irrigation, watershed, runoff, water-use-link, crop-observation, cross-domain, join-lane, no-parallel-authority]
related:
  - ../../README.md
  - ../README.md
  - ../../domains/README.md
  - ../../domains/agriculture/README.md
  - ../../domains/agriculture/hydrology-ext/README.md
  - ../../domains/agriculture/crop_observation.schema.json
  - ../../domains/agriculture/agriculture_feature_dto.schema.json
  - ../../domains/hydrology/README.md
  - ../../domains/hydrology/water_use_link.schema.json
  - ../../domains/hydrology/watershed.schema.json
  - ../../domains/hydrology/huc_unit.schema.json
  - ../../domains/hydrology/gauge_site.schema.json
  - ../../../../contracts/domains/agriculture/
  - ../../../../contracts/domains/hydrology/
  - ../../../../docs/domains/agriculture/
  - ../../../../docs/domains/hydrology/
  - ../../../../policy/domains/agriculture/
  - ../../../../policy/domains/hydrology/
  - ../../../../fixtures/domains/agriculture/
  - ../../../../fixtures/domains/hydrology/
  - ../../../../tests/domains/agriculture/
  - ../../../../tests/domains/hydrology/
notes:
  - "Expanded from an empty file at schemas/contracts/v1/joins/agriculture-hydrology/README.md."
  - "Current GitHub search did not surface schema files directly under this join lane beyond this README in the current check."
  - "An Agriculture-owned hydrology extension lane already exists at schemas/contracts/v1/domains/agriculture/hydrology-ext/README.md."
  - "Agriculture and Hydrology domain schema lanes are separate authority homes; this join path must not redefine either domain's canonical shapes."
  - "This README is a join-placement guardrail only; do not create canonical join schemas here without ADR, paired contracts, fixtures, validators, and steward review."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

![status](https://img.shields.io/badge/status-draft-yellow)
![root](https://img.shields.io/badge/root-schemas%2F-blue)
![family](https://img.shields.io/badge/family-joins-purple)
![join](https://img.shields.io/badge/join-agriculture--hydrology-green)
![posture](https://img.shields.io/badge/posture-guardrail-orange)
![truth](https://img.shields.io/badge/truth-cite--or--abstain-success)

> **Purpose.** `schemas/contracts/v1/joins/agriculture-hydrology/` is an empty guardrail README for a possible cross-domain Agriculture–Hydrology join schema lane.
>
> **One-line boundary.** This path may only define join-shape contracts if placement is accepted; it must not replace `schemas/contracts/v1/domains/agriculture/`, `schemas/contracts/v1/domains/agriculture/hydrology-ext/`, or `schemas/contracts/v1/domains/hydrology/`.

---

## Quick jumps

[Status](#status) · [Placement decision](#placement-decision) · [Repo fit](#repo-fit) · [Current inventory](#current-inventory) · [Related surfaced lanes](#related-surfaced-lanes) · [Candidate join shapes](#candidate-join-shapes) · [What belongs here](#what-belongs-here) · [What does not belong here](#what-does-not-belong-here) · [Join guardrails](#join-guardrails) · [Migration rules](#migration-rules) · [Validation](#validation) · [Rollback](#rollback) · [Open questions](#open-questions)

---

## Status

| Question | Answer | Truth label |
|---|---|---|
| Does this README path exist? | Yes: `schemas/contracts/v1/joins/agriculture-hydrology/README.md`. It was empty before this expansion. | **CONFIRMED** |
| Are schema files currently present under this join lane? | Not found in the current GitHub search beyond this README. | **NEEDS VERIFICATION / search-limited** |
| Is there an existing Agriculture/Hydrology extension lane? | Yes: `schemas/contracts/v1/domains/agriculture/hydrology-ext/README.md`. | **CONFIRMED** |
| Are Agriculture and Hydrology domain schema lanes present? | Yes. Both domain README paths were surfaced and inspected. | **CONFIRMED** |
| Is this join lane canonical? | Not proven. Treat as guardrail/index only until ADR or steward decision. | **NEEDS VERIFICATION / ADR-sensitive** |
| Can this lane store joined data, lifecycle records, or released outputs? | No. This path is schema documentation only, not lifecycle data, emitted records, proof, release, or public artifact storage. | **CONFIRMED boundary** |

> [!IMPORTANT]
> A join schema should describe relationship shape. It must not collapse Agriculture-owned crop/field/operation meaning into Hydrology-owned watershed/gauge/flow/water-use meaning, and it must not turn an extension lane into a second Hydrology authority.

---

## Placement decision

Current placement posture:

```text
Requested join guardrail:
  schemas/contracts/v1/joins/agriculture-hydrology/

Existing Agriculture-owned extension lane:
  schemas/contracts/v1/domains/agriculture/hydrology-ext/

Agriculture domain schema lane:
  schemas/contracts/v1/domains/agriculture/

Hydrology domain schema lane:
  schemas/contracts/v1/domains/hydrology/
```

Rationale:

- Domain schemas normally belong under `schemas/contracts/v1/domains/<domain>/...`.
- The Agriculture domain lane already has a `hydrology-ext/` child index for Agriculture-owned shapes that reference Hydrology.
- The Hydrology domain lane owns Hydrology schema shapes and records path-form drift that must remain visible before promotion.
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
        │   └── agriculture-hydrology/
        │       └── README.md                     # this file; join guardrail only
        └── domains/
            ├── agriculture/
            │   ├── README.md
            │   ├── crop_observation.schema.json
            │   ├── agriculture_feature_dto.schema.json
            │   └── hydrology-ext/
            │       └── README.md                 # Agriculture-owned Hydrology extension index
            └── hydrology/
                ├── README.md
                ├── watershed.schema.json
                ├── huc_unit.schema.json
                ├── gauge_site.schema.json
                └── water_use_link.schema.json

contracts/
├── domains/agriculture/                           # semantic meaning; not machine shape
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
| `schemas/contracts/v1/joins/agriculture-hydrology/README.md` | **CONFIRMED present** | Empty file expanded by this README. |
| `schemas/contracts/v1/joins/agriculture-hydrology/*.schema.json` | **Not found in current search** | Do not create here without ADR, paired contracts, and validation plan. |
| `schemas/contracts/v1/domains/agriculture/README.md` | **CONFIRMED present** | Agriculture domain schema lane. |
| `schemas/contracts/v1/domains/agriculture/hydrology-ext/README.md` | **CONFIRMED present** | Agriculture-owned Hydrology extension index. |
| `schemas/contracts/v1/domains/hydrology/README.md` | **CONFIRMED present** | Hydrology domain schema lane. |
| Agriculture schema files | **CONFIRMED surfaced by search** | Includes `crop_observation`, `agriculture_feature_dto`, receipts/release/support schemas. |
| Hydrology schema files | **CONFIRMED surfaced by search** | Includes `watershed`, `huc_unit`, `gauge_site`, `hydrograph`, `groundwater_well`, `water_level_observation`, `hydro-crosswalk-manifest`, and support schemas. |

---

## Related surfaced lanes

| Path | Role signal | Posture |
|---|---|---|
| `schemas/contracts/v1/domains/agriculture/` | Agriculture-owned machine shape lane. | **PROPOSED / active domain lane** |
| `schemas/contracts/v1/domains/agriculture/hydrology-ext/` | Agriculture-owned extension for bounded Hydrology references. | **DRAFT index / not Hydrology authority** |
| `schemas/contracts/v1/domains/hydrology/` | Hydrology-owned machine shape lane. | **PROPOSED / active domain lane** |
| `schemas/contracts/v1/joins/agriculture-hydrology/` | Possible neutral join schema lane. | **README-only guardrail** |

---

## Candidate join shapes

Candidate join schemas below require steward review, paired contracts, fixtures, validators, registry records, and release/policy review before promotion.

| Candidate schema | Purpose | Default posture |
|---|---|---|
| `agriculture_hydrology_join.schema.json` | Generic relationship between Agriculture feature and Hydrology feature references. | **PROPOSED / not created** |
| `irrigation_water_use_link.schema.json` | Agriculture-side irrigation/water-use relationship using Hydrology-owned references. | **PROPOSED / placement-sensitive** |
| `crop_watershed_context.schema.json` | Crop or agriculture feature context within watershed/HUC references. | **PROPOSED / evidence-bound** |
| `runoff_context_join.schema.json` | Relationship shape for agriculture surface context and Hydrology flow/runoff context. | **PROPOSED / model-sensitive** |
| `agriculture_hydro_release_projection.schema.json` | Public/release projection for already-governed join outputs. | **PROPOSED / release-gated** |

> [!CAUTION]
> Candidate names are proposals only. Do not treat them as repo files, accepted contracts, or implementation proof until created, paired, fixture-tested, and reviewed.

---

## What belongs here

- This README.
- Join schema placement notes for Agriculture–Hydrology relationships.
- Future neutral join schema files if an accepted ADR or migration plan authorizes this lane.
- Migration or mirror notes between `joins/agriculture-hydrology/` and `domains/agriculture/hydrology-ext/`.
- Links to paired contracts, fixtures, validators, schema registry records, policy references, release references, and tests.

---

## What does not belong here

- Agriculture-owned canonical schemas.
- Hydrology-owned canonical schemas.
- Agriculture extension schemas that properly belong under `domains/agriculture/hydrology-ext/`.
- Semantic contract prose.
- Policy rules, exposure decisions, or release decisions.
- Lifecycle data, joined datasets, source records, catalog records, triplets, receipt instances, proof outputs, release records, correction notices, rollback cards, or public artifacts.
- Validator code, packages, pipelines, runtime code, UI/API implementation, map tiles, dashboards, screenshots, or generated summaries.
- Claims that a join is valid, complete, true, or public-ready merely because it validates against a schema.

---

## Join guardrails

| Boundary | Requirement |
|---|---|
| Domain ownership | Agriculture and Hydrology keep their own canonical shapes and semantic contracts. |
| Join neutrality | A join schema records relationship shape, not source truth for either side. |
| Reference discipline | Use stable references to domain-owned objects rather than duplicating domain fields. |
| Evidence dependency | Join outputs need EvidenceBundle or equivalent support where claims depend on evidence. |
| Policy dependency | Joins that affect release, access, or public display must carry policy posture. |
| Release dependency | Public join projections must be release-gated and rollback-aware. |
| No parallel authority | Do not maintain identical join schema definitions under `joins/` and `domains/agriculture/hydrology-ext/` without a mirror/migration rule. |

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
- Agriculture and Hydrology steward review;
- policy review;
- release and rollback impact;
- deprecation/mirror window;
- tests proving no parallel authority remains.

---

## Validation

Recommended local validation sequence:

```bash
# Confirm this join lane remains README-only unless authorized.
find schemas/contracts/v1/joins/agriculture-hydrology -maxdepth 2 -type f | sort

# Inspect Agriculture/Hydrology related schema lanes.
find schemas/contracts/v1/domains/agriculture schemas/contracts/v1/domains/hydrology -maxdepth 4 -type f \
  | grep -Ei 'hydrology-ext|water_use|watershed|huc|gauge|crop|irrigation|runoff|README' \
  | sort

# Detect duplicate agriculture-hydrology join authority.
find schemas/contracts/v1 -maxdepth 6 -type f \
  | grep -Ei 'agriculture.*hydrology|hydrology.*agriculture|hydrology-ext|water_use|irrigation|runoff' \
  | sort

# Validate JSON syntax for related domain schemas.
find schemas/contracts/v1/domains/agriculture schemas/contracts/v1/domains/hydrology -name '*.schema.json' -print0 \
  | xargs -0 -r -I{} python -m json.tool {} >/dev/null

# Run project validators when available.
python tools/validate_all.py || true
pytest tests/schemas tests/contract tests/domains/agriculture tests/domains/hydrology tests/policy || true
```

Replace `|| true` with fail-closed CI behavior once validator and test paths are confirmed.

---

## Rollback

Rollback for this README is ordinary Git rollback: revert the commit that changed `schemas/contracts/v1/joins/agriculture-hydrology/README.md`.

Rollback for future join schema changes requires checking every downstream reference:

1. Revert or migrate schema files.
2. Restore canonical `$id` and `$ref` targets.
3. Restore paired contract links.
4. Restore fixtures, validators, schema registry records, and CI paths.
5. Restore Agriculture, Hydrology, policy, evidence, release, and receipt references.
6. Restore API/UI/MapLibre/Evidence Drawer consumers.
7. Preserve correction and rollback records if any public join surface was affected.

---

## Open questions

| Question | Status | Owner |
|---|---|---|
| Should Agriculture–Hydrology relationships live under `joins/` or remain Agriculture-owned under `domains/agriculture/hydrology-ext/`? | **NEEDS VERIFICATION / ADR-sensitive** | Schema steward + Agriculture steward + Hydrology steward |
| Which contract lane should own neutral join semantics? | **NEEDS VERIFICATION** | Contract steward |
| Which identifiers should join schemas reference from Agriculture and Hydrology? | **NEEDS VERIFICATION** | Domain stewards |
| Which fixtures prove that joins do not duplicate domain-owned fields? | **NEEDS VERIFICATION** | Validation steward |
| Which join projections are safe for public API/MapLibre/Focus Mode use? | **NEEDS VERIFICATION / release-gated** | Release steward + Policy steward |

---

## Maintainer notes

- Keep this path README-only until the join-home decision is resolved.
- Prefer references to Agriculture and Hydrology domain objects over copied fields.
- Do not let this join lane duplicate `domains/agriculture/hydrology-ext/` or Hydrology-owned schema authority.
- Preserve evidence, ownership, policy, release, correction, and rollback boundaries for all Agriculture–Hydrology join surfaces.
