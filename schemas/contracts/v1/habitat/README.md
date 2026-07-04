# `schemas/contracts/v1/habitat/` — Habitat Schema Alias Guardrail

<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/schemas-contracts-v1-habitat-readme
title: schemas/contracts/v1/habitat/ — Habitat Schema Alias Guardrail
type: readme; schema-alias-index; drift-guardrail; habitat-domain-boundary
authority_class: alias-guardrail
version: v0.1
status: draft; empty-alias-index; domain-home-elsewhere; child-guardrail-present; no-current-root-schema-files-found; do-not-promote-without-ADR; NEEDS VERIFICATION before promotion
owners:
  - OWNER_TBD — Habitat domain steward
  - OWNER_TBD — Schema steward
  - OWNER_TBD — Contract steward
  - OWNER_TBD — Receipt steward
  - OWNER_TBD — Policy steward
  - OWNER_TBD — Release steward
  - OWNER_TBD — Validation steward
  - OWNER_TBD — Docs steward
created: NEEDS VERIFICATION — empty README existed before v0.1 expansion
updated: 2026-07-04
policy_label: public; schemas; contracts-v1; habitat; alias-guardrail; domain-home-elsewhere; land-cover; ecoregions; receipts; release-gated; rollback-aware; no-parallel-authority
tags: [kfm, schemas, contracts, v1, habitat, alias, guardrail, domain-schema-lane, land-cover, ecoregions, habitat-patch, suitability-model, connectivity, stewardship-zone, uncertainty, receipts, no-parallel-authority]
related:
  - ../README.md
  - ../domains/README.md
  - ../domains/habitat/README.md
  - ../domains/habitat/land_cover/README.md
  - ../domains/habitat/ecoregions/README.md
  - ./receipts/README.md
  - ../../../../docs/domains/habitat/README.md
  - ../../../../contracts/domains/habitat/
  - ../../../../policy/domains/habitat/
  - ../../../../fixtures/domains/habitat/
  - ../../../../tests/domains/habitat/
  - ../../../../release/candidates/habitat/
notes:
  - "Expanded from an empty file at schemas/contracts/v1/habitat/README.md."
  - "Active Habitat schema work is under schemas/contracts/v1/domains/habitat/, including parent README, land_cover and ecoregions child indexes, and many schema files surfaced by search."
  - "schemas/contracts/v1/habitat/receipts/README.md is a guardrail only and should not become a parallel receipt schema home without ADR, migration note, or receipt-home decision."
  - "This file is an alias/guardrail index only; it must not become a parallel canonical Habitat schema home without ADR or migration note."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

![status](https://img.shields.io/badge/status-draft-yellow)
![root](https://img.shields.io/badge/root-schemas%2F-blue)
![family](https://img.shields.io/badge/family-habitat-green)
![posture](https://img.shields.io/badge/posture-alias__guardrail-orange)
![canonical](https://img.shields.io/badge/canonical-domain__lane__elsewhere-critical)
![truth](https://img.shields.io/badge/truth-cite--or--abstain-success)

> **Purpose.** `schemas/contracts/v1/habitat/` is a top-level alias/guardrail README for Habitat schema placement.
>
> **One-line boundary.** The active Habitat schema lane is `schemas/contracts/v1/domains/habitat/`. Do not add canonical Habitat schema files directly under `schemas/contracts/v1/habitat/` unless an accepted ADR, migration note, or compatibility plan authorizes this path.

---

## Quick jumps

[Status](#status) · [Placement decision](#placement-decision) · [Repo fit](#repo-fit) · [Current inventory](#current-inventory) · [Active domain-lane inventory](#active-domain-lane-inventory) · [Child guardrails](#child-guardrails) · [What belongs here](#what-belongs-here) · [What does not belong here](#what-does-not-belong-here) · [Migration rules](#migration-rules) · [Validation](#validation) · [Rollback](#rollback) · [Open questions](#open-questions)

---

## Status

| Question | Answer | Truth label |
|---|---|---|
| Does this README path exist? | Yes: `schemas/contracts/v1/habitat/README.md`. It was empty before this expansion. | **CONFIRMED** |
| Are canonical schema files currently present directly under `schemas/contracts/v1/habitat/`? | Not found in the current GitHub search beyond README/guardrail paths. | **NEEDS VERIFICATION / search-limited** |
| Where is current Habitat schema activity? | `schemas/contracts/v1/domains/habitat/` surfaced a README, child schema indexes, and many schema files. | **CONFIRMED path evidence** |
| Is this top-level `habitat/` path canonical? | Not proven. Treat as alias/guardrail only. | **NEEDS VERIFICATION / do-not-promote-without-ADR** |
| Does this folder have a child guardrail? | Yes. `schemas/contracts/v1/habitat/receipts/README.md` exists as a receipt-placement guardrail. | **CONFIRMED** |
| Can this path store Habitat lifecycle data or public artifacts? | No. Schema docs must not store lifecycle data, source records, receipts, proofs, release records, map tiles, or public artifacts. | **CONFIRMED boundary** |

> [!IMPORTANT]
> Habitat is a domain lane, not a top-level schema family, unless an accepted ADR says otherwise. Keep authoritative Habitat schema work under `schemas/contracts/v1/domains/habitat/` and use this file to prevent accidental duplicate schema authority.

---

## Placement decision

Current placement posture:

```text
Preferred / active Habitat domain schema lane:
  schemas/contracts/v1/domains/habitat/

Do-not-use-as-canonical without ADR:
  schemas/contracts/v1/habitat/

Receipt-placement guardrail:
  schemas/contracts/v1/habitat/receipts/
```

Rationale:

- Domain-specific schemas should live under `schemas/contracts/v1/domains/<domain>/...` unless an accepted exception says otherwise.
- The existing Habitat domain schema README identifies `schemas/contracts/v1/domains/habitat/` as the draft Habitat domain schema lane.
- Current search surfaced many Habitat schemas under the domain lane and no canonical schema files directly under this top-level path.
- Maintaining both paths as independent schema homes would create `$id`, validator, fixture, release, and rollback drift.
- The `receipts/` child under this top-level path is itself a guardrail, not a receipt authority.

---

## Repo fit

```text
schemas/
└── contracts/
    └── v1/
        ├── README.md
        ├── habitat/
        │   ├── README.md                         # this file; alias/guardrail only
        │   └── receipts/
        │       └── README.md                     # receipt-placement guardrail only
        └── domains/
            └── habitat/
                ├── README.md                     # active Habitat domain schema index
                ├── land_cover/
                │   └── README.md                 # Habitat Land Cover child schema index
                ├── ecoregions/
                │   └── README.md                 # Habitat Ecoregions child schema index
                └── *.schema.json                 # current Habitat schema files surfaced by search

contracts/
└── domains/habitat/                               # semantic meaning; not machine shape

policy/
└── domains/habitat/                               # admissibility/policy posture; not schema shape

fixtures/
tests/
release/
```

---

## Current inventory

| Path | Status | Note |
|---|---|---|
| `schemas/contracts/v1/habitat/README.md` | **CONFIRMED present** | Empty file expanded by this README. |
| `schemas/contracts/v1/habitat/*.schema.json` | **Not found in current search** | Do not create here without ADR or migration note. |
| `schemas/contracts/v1/habitat/receipts/README.md` | **CONFIRMED present** | Guardrail-only receipt sublane README. |
| `schemas/contracts/v1/habitat/receipts/*.schema.json` | **Not found in current search** | Do not create here without ADR, migration note, or receipt-home decision. |
| `schemas/contracts/v1/domains/habitat/README.md` | **CONFIRMED present** | Active Habitat domain schema index. |
| `schemas/contracts/v1/domains/habitat/land_cover/README.md` | **CONFIRMED present** | Habitat Land Cover child schema index. |
| `schemas/contracts/v1/domains/habitat/ecoregions/README.md` | **CONFIRMED present** | Habitat Ecoregions child schema index. |
| `schemas/contracts/v1/domains/habitat/*.schema.json` | **CONFIRMED surfaced by search** | Many schema files were found; each file's maturity still requires per-file verification. |

---

## Active domain-lane inventory

Current search surfaced the following Habitat schema names under `schemas/contracts/v1/domains/habitat/`. This is a search-derived inventory, not a complete mounted-checkout manifest.

| Surfaced path | Role signal | Posture |
|---|---|---|
| `README.md` | Habitat domain schema index. | **CONFIRMED present** |
| `land_cover/README.md` | Land-cover child schema index. | **CONFIRMED present** |
| `ecoregions/README.md` | Ecoregions child schema index. | **CONFIRMED present** |
| `habitat_patch.schema.json` | Habitat patch shape. | **NEEDS VERIFICATION** |
| `ecological_system.schema.json` | Ecological system shape. | **NEEDS VERIFICATION** |
| `stewardship_zone.schema.json` | Stewardship zone shape. | **NEEDS VERIFICATION** |
| `suitability_model.schema.json` | Suitability model shape. | **NEEDS VERIFICATION** |
| `connectivity_edge.schema.json` | Connectivity edge shape. | **NEEDS VERIFICATION** |
| `habitat_quality_score.schema.json` | Habitat quality score shape. | **NEEDS VERIFICATION** |
| `restoration_opportunity.schema.json` | Restoration opportunity shape. | **NEEDS VERIFICATION** |
| `uncertainty_surface.schema.json` | Uncertainty surface shape. | **NEEDS VERIFICATION** |
| `land_cover_observation.schema.json` | Land-cover observation shape. | **NEEDS VERIFICATION** |
| `land_cover/observation.schema.json` | Land-cover observation child-lane shape. | **PROPOSED / possible profile or duplicate** |
| `land_cover/class_scheme.schema.json` | Land-cover class scheme shape. | **NEEDS VERIFICATION** |
| `land_cover/crosswalk.schema.json` | Land-cover crosswalk shape. | **NEEDS VERIFICATION** |
| `land_cover/change_summary.schema.json` | Land-cover change summary shape. | **NEEDS VERIFICATION** |
| `land_cover/uncertainty.schema.json` | Land-cover uncertainty shape. | **NEEDS VERIFICATION** |
| `habitat-fauna-join.schema.json` | Habitat/Fauna join shape. | **NEEDS VERIFICATION / cross-domain-sensitive** |
| Support schemas | `run_receipt`, `model_run_receipt`, `geoprivacy_transform_receipt`, `release_manifest`, `rollback_card`, `correction_notice`, `promotion_decision`, `decision_envelope`, `habitat_decision_envelope`, `source_state_hash`, `catalog_matrix`, `layer_manifest`, `evidence_bundle`, `evidence-bundle`, `evidence_drawer_payload`, `domain_observation`, `domain_feature_identity`, `domain_validation_report`, `domain_layer_descriptor`. | **NEEDS VERIFICATION** |

> [!CAUTION]
> The presence of files in the domain lane does not prove field completeness, accepted schema status, fixture coverage, validator wiring, policy behavior, release readiness, or public-safety approval.

---

## Child guardrails

| Child path | Current posture | Rule |
|---|---|---|
| `schemas/contracts/v1/habitat/receipts/` | Guardrail-only README. | Do not use as canonical Habitat receipt schema home without ADR, migration note, or receipt-home decision. |

If future top-level child paths are added under `schemas/contracts/v1/habitat/`, treat them as guardrails unless a reviewed placement decision says otherwise.

---

## What belongs here

- This README.
- Alias, migration, mirror, deprecation, or placement notes for `schemas/contracts/v1/habitat/` if needed.
- Guardrail child README files that prevent accidental duplicate schema homes.
- Pointers to the accepted Habitat schema home.
- Drift notes explaining why schema files should not be added directly here without review.

---

## What does not belong here

- Canonical Habitat JSON Schema files unless an accepted ADR/migration authorizes this path.
- Habitat domain schemas that belong under `schemas/contracts/v1/domains/habitat/`.
- Semantic contract prose.
- Policy rules, sensitivity decisions, redaction decisions, exposure decisions, or release decisions.
- Emitted receipt instances, proof outputs, lifecycle data, source registry records, catalog records, triplets, release records, correction notices, withdrawal notices, rollback cards, or public artifacts.
- Validator code, packages, pipelines, runtime code, UI/API implementation, map tiles, dashboards, screenshots, or generated summaries.
- Claims that a Habitat schema is complete or public-safe without fixtures, validators, registry records, policy review, and release support.

---

## Migration rules

Do not move or duplicate Habitat schemas into this top-level path unless a reviewed migration plan defines:

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
- child-lane impact;
- deprecation/mirror window;
- tests proving no parallel authority remains.

---

## Validation

Recommended local validation sequence:

```bash
# Confirm this alias path remains README/guardrail-only unless migration is authorized.
find schemas/contracts/v1/habitat -maxdepth 3 -type f | sort

# Inspect the active Habitat domain schema lane.
find schemas/contracts/v1/domains/habitat -maxdepth 4 -type f | sort

# Detect duplicate Habitat schema authority across top-level and domain paths.
find schemas/contracts/v1 -maxdepth 6 -type f \
  | grep -Ei '/habitat/|/domains/habitat/' \
  | sort

# Validate JSON syntax for the active domain lane.
find schemas/contracts/v1/domains/habitat -name '*.schema.json' -print0 \
  | xargs -0 -r -I{} python -m json.tool {} >/dev/null

# Run project validators when available.
python tools/validate_all.py || true
pytest tests/schemas tests/contract tests/domains/habitat tests/policy tests/release || true
```

Replace `|| true` with fail-closed CI behavior once validator and test paths are confirmed.

---

## Rollback

Rollback for this README is ordinary Git rollback: revert the commit that changed `schemas/contracts/v1/habitat/README.md`.

Rollback for any future migration into this path requires checking every downstream reference:

1. Revert or migrate schema files.
2. Restore canonical `$id` and `$ref` targets.
3. Restore paired contract links.
4. Restore fixtures, validators, schema registry records, and CI paths.
5. Restore policy, evidence, release, domain, and receipt references.
6. Restore Habitat API/UI/MapLibre/Evidence Drawer consumers.
7. Preserve correction and rollback records if any public Habitat surface was affected.

---

## Open questions

| Question | Status | Owner |
|---|---|---|
| Should `schemas/contracts/v1/habitat/` remain README/guardrail-only as an alias path? | **PROPOSED** | Schema steward + Habitat steward |
| Is there any accepted ADR authorizing top-level domain schema folders outside `domains/<domain>/`? | **NEEDS VERIFICATION** | Schema steward |
| Should top-level `habitat/receipts/` remain a guardrail or become an accepted receipt sublane? | **NEEDS VERIFICATION / ADR-sensitive** | Habitat steward + Receipt steward + Schema steward |
| Which Habitat domain schemas are field-complete and fixture-tested? | **NEEDS VERIFICATION** | Validation steward |
| Which Habitat schemas are safe for public API/MapLibre/Focus Mode use? | **NEEDS VERIFICATION / release-gated** | Release steward + Policy steward |

---

## Maintainer notes

- Keep this top-level path as a guardrail unless a reviewed migration says otherwise.
- Put Habitat domain schemas under `schemas/contracts/v1/domains/habitat/`.
- Do not let this alias or its child guardrail paths become parallel authority.
- Preserve evidence, uncertainty, cross-domain, policy, release, correction, and rollback boundaries for all Habitat surfaces.
