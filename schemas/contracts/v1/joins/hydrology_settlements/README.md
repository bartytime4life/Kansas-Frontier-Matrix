# `schemas/contracts/v1/joins/hydrology_settlements/` — Hydrology–Settlements Join Schema Guardrail

<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/schemas-contracts-v1-joins-hydrology-settlements-readme
title: schemas/contracts/v1/joins/hydrology_settlements/ — Hydrology–Settlements Join Schema Guardrail
type: readme; join-schema-index; cross-domain-guardrail; hydrology-settlements-boundary
authority_class: join-schema-guardrail
version: v0.1
status: draft; empty-join-lane; hydrology-domain-present; settlements-infrastructure-domain-present; settlement-slug-conflict-visible; no-current-join-schema-files-found; do-not-promote-without-ADR; NEEDS VERIFICATION before promotion
owners:
  - OWNER_TBD — Hydrology domain steward
  - OWNER_TBD — Settlements/Infrastructure domain steward
  - OWNER_TBD — Settlement compatibility steward
  - OWNER_TBD — Join steward
  - OWNER_TBD — Schema steward
  - OWNER_TBD — Contract steward
  - OWNER_TBD — Policy steward
  - OWNER_TBD — Release steward
  - OWNER_TBD — Validation steward
  - OWNER_TBD — Docs steward
created: NEEDS VERIFICATION — empty README existed before v0.1 expansion
updated: 2026-07-04
policy_label: public; schemas; contracts-v1; joins; hydrology-settlements; cross-domain; settlement-slug-conflict; settlements-infrastructure; evidence-bound; release-gated; rollback-aware; no-parallel-authority
tags: [kfm, schemas, contracts, v1, joins, hydrology, settlements, settlements-infrastructure, watershed, huc, gauge, hydrograph, hydro-feature, settlement, place-identity, service-area, cross-domain, join-lane, no-parallel-authority]
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
  - ../../domains/settlement/README.md
  - ../../domains/settlements-infrastructure/README.md
  - ../../domains/settlements-infrastructure/domain_feature_identity.schema.json
  - ../../domains/settlements-infrastructure/domain_layer_descriptor.schema.json
  - ../../domains/settlements-infrastructure/runtime/README.md
  - ../../../../contracts/domains/hydrology/
  - ../../../../contracts/domains/settlement/
  - ../../../../contracts/domains/settlements-infrastructure/
  - ../../../../docs/domains/hydrology/
  - ../../../../docs/domains/settlements-infrastructure/
  - ../../../../policy/domains/hydrology/
  - ../../../../policy/domains/settlements-infrastructure/
  - ../../../../fixtures/domains/hydrology/
  - ../../../../fixtures/domains/settlements-infrastructure/
  - ../../../../tests/domains/hydrology/
  - ../../../../tests/domains/settlements-infrastructure/
notes:
  - "Expanded from an empty file at schemas/contracts/v1/joins/hydrology_settlements/README.md."
  - "Current GitHub search did not surface schema files directly under this join lane beyond this README in the current check."
  - "Hydrology domain schema files were surfaced under schemas/contracts/v1/domains/hydrology/."
  - "Settlements/Infrastructure schema files were surfaced under schemas/contracts/v1/domains/settlements-infrastructure/."
  - "The singular settlement path exists as a compatibility index and points to settlements-infrastructure as the broader working schema lane."
  - "This README is a join-placement guardrail only; do not create canonical join schemas here without ADR, paired contracts, fixtures, validators, and steward review."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

![status](https://img.shields.io/badge/status-draft-yellow)
![root](https://img.shields.io/badge/root-schemas%2F-blue)
![family](https://img.shields.io/badge/family-joins-purple)
![join](https://img.shields.io/badge/join-hydrology--settlements-blue)
![posture](https://img.shields.io/badge/posture-guardrail-orange)
![truth](https://img.shields.io/badge/truth-cite--or--abstain-success)

> **Purpose.** `schemas/contracts/v1/joins/hydrology_settlements/` is an empty guardrail README for a possible Hydrology–Settlements join schema lane.
>
> **One-line boundary.** This path may only define join-shape contracts if placement is accepted; it must not replace `schemas/contracts/v1/domains/hydrology/`, `schemas/contracts/v1/domains/settlements-infrastructure/`, or the singular `schemas/contracts/v1/domains/settlement/` compatibility index.

---

## Quick jumps

[Status](#status) · [Placement decision](#placement-decision) · [Repo fit](#repo-fit) · [Current inventory](#current-inventory) · [Related surfaced lanes](#related-surfaced-lanes) · [Candidate join shapes](#candidate-join-shapes) · [What belongs here](#what-belongs-here) · [What does not belong here](#what-does-not-belong-here) · [Join guardrails](#join-guardrails) · [Migration rules](#migration-rules) · [Validation](#validation) · [Rollback](#rollback) · [Open questions](#open-questions)

---

## Status

| Question | Answer | Truth label |
|---|---|---|
| Does this README path exist? | Yes: `schemas/contracts/v1/joins/hydrology_settlements/README.md`. It was empty before this expansion. | **CONFIRMED** |
| Are schema files currently present under this join lane? | Not found in the current GitHub search beyond this README. | **NEEDS VERIFICATION / search-limited** |
| Are Hydrology and Settlements/Infrastructure schema lanes present? | Yes. Hydrology, singular Settlement compatibility, and Settlements/Infrastructure schema lanes were surfaced and inspected. | **CONFIRMED path evidence** |
| Is the singular `settlement` slug canonical? | Not settled. The singular `settlement/` README identifies itself as a compatibility index and points to `settlements-infrastructure/` as the broader working lane. | **CONFIRMED conflict-visible** |
| Is this join lane canonical? | Not proven. Treat as guardrail/index only until ADR or steward decision. | **NEEDS VERIFICATION / ADR-sensitive** |
| Can this lane store joined data, lifecycle records, or released outputs? | No. This path is schema documentation only, not lifecycle data, emitted records, release records, or public artifact storage. | **CONFIRMED boundary** |

> [!IMPORTANT]
> A Hydrology–Settlements join schema should describe relationship shape. It must not collapse Hydrology-owned watershed, gauge, flow, or water-observation meaning into Settlements/Infrastructure-owned place, facility, service-area, or asset meaning.

---

## Placement decision

Current placement posture:

```text
Requested join guardrail:
  schemas/contracts/v1/joins/hydrology_settlements/

Hydrology domain schema lane:
  schemas/contracts/v1/domains/hydrology/

Settlements/Infrastructure working schema lane:
  schemas/contracts/v1/domains/settlements-infrastructure/

Singular settlement compatibility index:
  schemas/contracts/v1/domains/settlement/
```

Rationale:

- Domain schemas normally belong under `schemas/contracts/v1/domains/<domain>/...`.
- Hydrology owns water, watershed, gauge, hydrograph, flow, and water-observation shapes.
- Settlements/Infrastructure is the broader working schema lane for settlement/infrastructure surfaces.
- The singular `settlement/` path is conflict-visible and compatibility-oriented, not a proven canonical home.
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
        │   └── hydrology_settlements/
        │       └── README.md                     # this file; join guardrail only
        └── domains/
            ├── hydrology/
            │   ├── README.md
            │   ├── huc_unit.schema.json
            │   ├── watershed.schema.json
            │   ├── gauge_site.schema.json
            │   └── hydrograph.schema.json
            ├── settlement/
            │   └── README.md                     # compatibility index
            └── settlements-infrastructure/
                ├── README.md
                ├── runtime/
                │   └── README.md
                ├── domain_feature_identity.schema.json
                └── domain_layer_descriptor.schema.json

contracts/
├── domains/hydrology/                             # semantic meaning; not machine shape
├── domains/settlement/                            # compatibility surface
└── domains/settlements-infrastructure/            # working semantic lane

policy/
fixtures/
tests/
release/
```

---

## Current inventory

| Path | Status | Note |
|---|---|---|
| `schemas/contracts/v1/joins/hydrology_settlements/README.md` | **CONFIRMED present** | Empty file expanded by this README. |
| `schemas/contracts/v1/joins/hydrology_settlements/*.schema.json` | **Not found in current search** | Do not create here without ADR, paired contracts, and validation plan. |
| `schemas/contracts/v1/domains/hydrology/README.md` | **CONFIRMED inspected** | Hydrology domain schema lane. |
| `schemas/contracts/v1/domains/settlement/README.md` | **CONFIRMED inspected** | Singular compatibility index, not confirmed canonical. |
| `schemas/contracts/v1/domains/settlements-infrastructure/README.md` | **CONFIRMED inspected** | Broader working schema lane, still PROPOSED scaffold. |
| Hydrology schema files | **CONFIRMED surfaced by search** | Includes watershed/HUC/gauge/hydrograph/flow/water observation/support schemas. |
| Settlements/Infrastructure schema files | **CONFIRMED surfaced by search** | Includes domain identity, layer, runtime, release, rollback, correction, and support schemas. |

---

## Related surfaced lanes

| Path | Role signal | Posture |
|---|---|---|
| `schemas/contracts/v1/domains/hydrology/` | Hydrology-owned machine shape lane. | **PROPOSED / active domain lane** |
| `schemas/contracts/v1/domains/settlements-infrastructure/` | Settlements/Infrastructure working machine shape lane. | **PROPOSED scaffold** |
| `schemas/contracts/v1/domains/settlement/` | Singular settlement compatibility index. | **PROPOSED / CONFLICTED** |
| `schemas/contracts/v1/joins/hydrology_settlements/` | Possible neutral join schema lane. | **README-only guardrail** |

---

## Candidate join shapes

Candidate join schemas below require steward review, paired contracts, fixtures, validators, registry records, and release/policy review before promotion.

| Candidate schema | Purpose | Default posture |
|---|---|---|
| `hydrology_settlements_join.schema.json` | Generic relationship between Hydrology feature refs and settlement/infrastructure refs. | **PROPOSED / not created** |
| `settlement_watershed_context.schema.json` | Relationship shape between settlement/place refs and watershed/HUC refs. | **PROPOSED / evidence-bound** |
| `facility_hydrology_context.schema.json` | Relationship shape between facility/service-area refs and Hydrology context refs. | **PROPOSED / placement-sensitive** |
| `gauge_settlement_context.schema.json` | Relationship shape between gauge/hydrograph refs and settlement/infrastructure refs. | **PROPOSED / freshness-aware** |
| `hydrology_settlements_release_projection.schema.json` | Public/release projection for already-governed join outputs. | **PROPOSED / release-gated** |

> [!CAUTION]
> Candidate names are proposals only. Do not treat them as repo files, accepted contracts, or implementation proof until created, paired, fixture-tested, and reviewed.

---

## What belongs here

- This README.
- Join schema placement notes for Hydrology–Settlements relationships.
- Future neutral join schema files if an accepted ADR or migration plan authorizes this lane.
- Links to paired contracts, fixtures, validators, schema registry records, policy references, release references, and tests.
- Drift notes preventing duplicate Hydrology, Settlement, or Settlements/Infrastructure schema authority.

---

## What does not belong here

- Hydrology-owned canonical schemas.
- Settlement or Settlements/Infrastructure-owned canonical schemas.
- Semantic contract prose.
- Policy rules, exposure decisions, or release decisions.
- Lifecycle data, joined datasets, source records, catalog records, triplets, receipt instances, proof outputs, release records, correction notices, rollback cards, or public artifacts.
- Validator code, packages, pipelines, runtime code, UI/API implementation, map tiles, dashboards, screenshots, or generated summaries.
- Claims that a join is valid, complete, true, current, or public-ready merely because it validates against a schema.

---

## Join guardrails

| Boundary | Requirement |
|---|---|
| Domain ownership | Hydrology and Settlements/Infrastructure keep their own canonical shapes and semantic contracts. |
| Slug discipline | Keep the singular `settlement/` compatibility status visible until the slug decision is settled. |
| Join neutrality | A join schema records relationship shape, not source truth for either side. |
| Reference discipline | Use stable references to domain-owned objects rather than duplicating domain fields. |
| Time/freshness discipline | Join outputs should preserve observation, retrieval, release, and correction time where applicable. |
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
- Hydrology and Settlements/Infrastructure steward review;
- policy review;
- release and rollback impact;
- deprecation/mirror window;
- tests proving no parallel authority remains.

---

## Validation

Recommended local validation sequence:

```bash
# Confirm this join lane remains README-only unless authorized.
find schemas/contracts/v1/joins/hydrology_settlements -maxdepth 2 -type f | sort

# Inspect Hydrology/Settlement related schema lanes.
find schemas/contracts/v1/domains/hydrology schemas/contracts/v1/domains/settlement schemas/contracts/v1/domains/settlements-infrastructure -maxdepth 4 -type f \
  | grep -Ei 'huc|watershed|gauge|hydrograph|flow|water|settlement|infrastructure|facility|service|runtime|README' \
  | sort

# Detect duplicate hydrology-settlements join authority.
find schemas/contracts/v1 -maxdepth 6 -type f \
  | grep -Ei 'hydrology.*settlement|settlement.*hydrology|watershed.*settlement|gauge.*settlement|facility.*hydro|hydro.*facility' \
  | sort

# Validate JSON syntax for related domain schemas.
find schemas/contracts/v1/domains/hydrology schemas/contracts/v1/domains/settlements-infrastructure -name '*.schema.json' -print0 \
  | xargs -0 -r -I{} python -m json.tool {} >/dev/null

# Run project validators when available.
python tools/validate_all.py || true
pytest tests/schemas tests/contract tests/domains/hydrology tests/domains/settlements-infrastructure tests/policy || true
```

Replace `|| true` with fail-closed CI behavior once validator and test paths are confirmed.

---

## Rollback

Rollback for this README is ordinary Git rollback: revert the commit that changed `schemas/contracts/v1/joins/hydrology_settlements/README.md`.

Rollback for future join schema changes requires checking every downstream reference:

1. Revert or migrate schema files.
2. Restore canonical `$id` and `$ref` targets.
3. Restore paired contract links.
4. Restore fixtures, validators, schema registry records, and CI paths.
5. Restore Hydrology, Settlement, Settlements/Infrastructure, policy, evidence, release, and receipt references.
6. Restore API/UI/MapLibre/Evidence Drawer consumers.
7. Preserve correction and rollback records if any public join surface was affected.

---

## Open questions

| Question | Status | Owner |
|---|---|---|
| Should Hydrology–Settlements relationships live under `joins/`, a Hydrology extension, a Settlements/Infrastructure extension, or another cross-domain lane? | **NEEDS VERIFICATION / ADR-sensitive** | Schema steward + Hydrology steward + Settlements/Infrastructure steward |
| Should the slug be `hydrology_settlements`, `hydrology-settlements`, `settlements-hydrology`, or another convention? | **NEEDS VERIFICATION / ADR-sensitive** | Schema steward + Join steward |
| Should join schemas reference singular `settlement/` compatibility objects or only the broader `settlements-infrastructure/` lane? | **NEEDS VERIFICATION / slug-sensitive** | Schema steward + Settlements/Infrastructure steward |
| Which contract lane should own neutral join semantics? | **NEEDS VERIFICATION** | Contract steward |
| Which fixtures prove that joins do not duplicate domain-owned fields? | **NEEDS VERIFICATION** | Validation steward |
| Which join projections are safe for public API/MapLibre/Focus Mode use? | **NEEDS VERIFICATION / release-gated** | Release steward + Policy steward |

---

## Maintainer notes

- Keep this path README-only until the join-home decision is resolved.
- Prefer references to Hydrology and Settlements/Infrastructure domain objects over copied fields.
- Do not let this join lane duplicate Hydrology, Settlement, or Settlements/Infrastructure schema authority.
- Preserve evidence, time/freshness, ownership, policy, release, correction, and rollback boundaries for all Hydrology–Settlements join surfaces.
