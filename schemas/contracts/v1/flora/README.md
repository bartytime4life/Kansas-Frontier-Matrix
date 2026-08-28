# `schemas/contracts/v1/flora/` — Flora Schema Alias Guardrail

<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/schemas-contracts-v1-flora-readme
title: schemas/contracts/v1/flora/ — Flora Schema Alias Guardrail
type: readme; schema-alias-index; drift-guardrail; domain-schema-boundary
authority_class: alias-guardrail
version: v0.1
status: draft; empty-alias-index; domain-home-elsewhere; no-current-schema-files-found; do-not-promote-without-ADR; NEEDS VERIFICATION before promotion
owners:
  - OWNER_TBD — Flora domain steward
  - OWNER_TBD — Schema steward
  - OWNER_TBD — Contract steward
  - OWNER_TBD — Sensitivity steward
  - OWNER_TBD — Policy steward
  - OWNER_TBD — Release steward
  - OWNER_TBD — Validation steward
  - OWNER_TBD — Docs steward
created: NEEDS VERIFICATION — empty README existed before v0.1 expansion
updated: 2026-07-04
policy_label: public; schemas; contracts-v1; flora; alias-guardrail; domain-home-elsewhere; rare-plants; geoprivacy-aware; sensitivity-aware; release-gated; rollback-aware; no-parallel-authority
tags: [kfm, schemas, contracts, v1, flora, alias, guardrail, domain-schema-lane, rare-plants, geoprivacy, sensitive-plants, occurrence, range, phenology, vegetation, restoration, redaction, no-parallel-authority]
related:
  - ../README.md
  - ../domains/README.md
  - ../domains/flora/README.md
  - ../../../../docs/domains/flora/README.md
  - ../../../../docs/domains/flora/CANONICAL_PATHS.md
  - ../../../../docs/domains/flora/SCHEMAS.md
  - ../../../../docs/domains/flora/RIGHTS_AND_SENSITIVITY.md
  - ../../../../contracts/domains/flora/
  - ../../../../policy/domains/flora/
  - ../../../../fixtures/domains/flora/
  - ../../../../tests/domains/flora/
  - ../../../../release/candidates/flora/
notes:
  - "Expanded from an empty file at schemas/contracts/v1/flora/README.md."
  - "GitHub search did not surface existing schema files under schemas/contracts/v1/flora/ beyond this README in the current check."
  - "Current flora schema activity is under schemas/contracts/v1/domains/flora/, including README and many schema files surfaced by search."
  - "This file is an alias/guardrail index only; it must not become a parallel canonical flora schema home without ADR or migration note."
  - "Flora schemas are sensitivity- and geoprivacy-significant; exact rare plant locations, culturally sensitive plant knowledge, steward-controlled records, and reversible redaction details require fail-closed handling."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

![status](https://img.shields.io/badge/status-draft-yellow)
![root](https://img.shields.io/badge/root-schemas%2F-blue)
![family](https://img.shields.io/badge/family-flora-green)
![posture](https://img.shields.io/badge/posture-alias__guardrail-orange)
![canonical](https://img.shields.io/badge/canonical-domain__lane__elsewhere-critical)
![sensitivity](https://img.shields.io/badge/sensitivity-fail--closed-red)
![truth](https://img.shields.io/badge/truth-cite--or--abstain-success)

> **Purpose.** `schemas/contracts/v1/flora/` is an empty alias/guardrail README for Flora schema placement.
>
> **One-line boundary.** The verified Flora schema lane is `schemas/contracts/v1/domains/flora/`. Do not add canonical Flora schema files directly under `schemas/contracts/v1/flora/` unless an accepted ADR, migration note, or compatibility plan authorizes this path.

---

## Quick jumps

[Status](#status) · [Placement decision](#placement-decision) · [Repo fit](#repo-fit) · [Current inventory](#current-inventory) · [Canonical lane inventory](#canonical-lane-inventory) · [What belongs here](#what-belongs-here) · [What does not belong here](#what-does-not-belong-here) · [Flora sensitivity guardrails](#flora-sensitivity-guardrails) · [Migration rules](#migration-rules) · [Validation](#validation) · [Rollback](#rollback) · [Open questions](#open-questions)

---

## Status

| Question | Answer | Truth label |
|---|---|---|
| Does this README path exist? | Yes: `schemas/contracts/v1/flora/README.md`. It was empty before this expansion. | **CONFIRMED** |
| Are schema files currently present under `schemas/contracts/v1/flora/`? | Not found in the current GitHub search beyond this README. | **NEEDS VERIFICATION / search-limited** |
| Where is current Flora schema activity? | `schemas/contracts/v1/domains/flora/` surfaced a README and many schema files. | **CONFIRMED path evidence** |
| Is this top-level `flora/` path canonical? | Not proven. Treat as alias/guardrail only. | **NEEDS VERIFICATION / do-not-promote-without-ADR** |
| Can this README validate Flora schema completeness? | No. It only prevents parallel authority and points to the domain lane. | **CONFIRMED boundary** |
| Can this path store public Flora records or sensitive occurrence data? | No. Schema docs must not store lifecycle data, occurrences, source records, receipts, proofs, or sensitive details. | **CONFIRMED boundary** |

> [!IMPORTANT]
> Flora is a domain lane, not a top-level schema family, unless an accepted ADR says otherwise. Keep authoritative Flora schema work under `schemas/contracts/v1/domains/flora/` and use this file only to prevent accidental duplicate schema authority.

---

## Placement decision

Current placement posture:

```text
Preferred / active domain schema lane:
  schemas/contracts/v1/domains/flora/

Do-not-use-as-canonical without ADR:
  schemas/contracts/v1/flora/
```

Rationale:

- ADR-0001-style schema placement uses `schemas/contracts/v1/domains/<domain>/...` for domain-specific schemas.
- The existing Flora domain schema README already identifies `schemas/contracts/v1/domains/flora/` as the Flora domain schema lane.
- Current search surfaced many Flora schemas under the domain lane and none under this top-level path.
- Maintaining both paths as independent schema homes would create validator drift, `$id` conflicts, stale fixtures, and publication-risk confusion.

---

## Repo fit

```text
schemas/
└── contracts/
    └── v1/
        ├── README.md
        ├── flora/
        │   └── README.md                       # this file; alias/guardrail only
        └── domains/
            └── flora/
                ├── README.md                   # active Flora domain schema index
                └── *.schema.json               # current Flora schema files

contracts/
└── domains/
    └── flora/                                  # semantic meaning; not machine shape

policy/
└── domains/flora/                              # sensitivity/policy posture; not schema shape

fixtures/
└── domains/flora/                              # valid/invalid examples; coverage NEEDS VERIFICATION

tests/
└── domains/flora/                              # behavioral proof; coverage NEEDS VERIFICATION

release/
└── candidates/flora/                           # promotion/release/correction/rollback surfaces
```

---

## Current inventory

Current check:

| Path | Status | Note |
|---|---|---|
| `schemas/contracts/v1/flora/README.md` | **CONFIRMED present** | Empty file expanded by this README. |
| `schemas/contracts/v1/flora/*.schema.json` | **Not found in current search** | Do not create here without ADR or migration note. |
| `schemas/contracts/v1/domains/flora/README.md` | **CONFIRMED present** | Active Flora domain schema index. |
| `schemas/contracts/v1/domains/flora/*.schema.json` | **CONFIRMED surfaced by search** | Many schema files were found; each file's maturity still requires per-file verification. |

---

## Canonical lane inventory

Current search surfaced the following files under `schemas/contracts/v1/domains/flora/`. This is a search-derived inventory, not a complete mounted-checkout manifest.

| Surfaced path | Role signal | Posture |
|---|---|---|
| `README.md` | Flora domain schema index. | **CONFIRMED present** |
| `plant_taxon.schema.json` | Plant taxonomic identity shape. | **NEEDS VERIFICATION** |
| `flora_taxon_crosswalk.schema.json` | Authority taxonomy mapping. | **NEEDS VERIFICATION** |
| `specimen_record.schema.json` | Specimen/evidence record shape. | **NEEDS VERIFICATION** |
| `flora_occurrence.schema.json` | Flora occurrence shape. | **NEEDS VERIFICATION** |
| `occurrence_restricted.schema.json` | Restricted occurrence shape. | **NEEDS VERIFICATION / sensitive** |
| `occurrence_public.schema.json` | Public-safe occurrence shape. | **NEEDS VERIFICATION / release-gated** |
| `rare_plant_record.schema.json` | Rare/protected plant shape. | **NEEDS VERIFICATION / fail-closed** |
| `range_polygon.schema.json` | Range/distribution geometry shape. | **NEEDS VERIFICATION** |
| `range_polygon.flora.schema.json` | Flora-specific range/distribution geometry variant. | **NEEDS VERIFICATION / possible duplicate or profile** |
| `distribution_surface.flora.schema.json` | Flora distribution surface shape. | **NEEDS VERIFICATION** |
| `phenology_observation.schema.json` | Phenology observation shape. | **NEEDS VERIFICATION** |
| `vegetation_community.schema.json` | Vegetation community shape. | **NEEDS VERIFICATION** |
| `habitat_association.schema.json` | Flora/habitat association shape. | **NEEDS VERIFICATION / cross-domain boundary** |
| `habitat_association.flora.schema.json` | Flora-specific habitat-association variant. | **NEEDS VERIFICATION / possible duplicate or profile** |
| `botanical_survey.schema.json` | Botanical survey/event shape. | **NEEDS VERIFICATION** |
| `restoration_planting.schema.json` | Restoration planting shape. | **NEEDS VERIFICATION** |
| `invasive_plant_record.schema.json` | Invasive plant record shape. | **NEEDS VERIFICATION** |
| `redaction_receipt.schema.json` | Redaction receipt shape. | **PROPOSED / scaffold** |
| `redaction_receipt.flora.schema.json` | Flora-specific redaction receipt variant. | **NEEDS VERIFICATION / possible duplicate or profile** |
| Governance support schemas | `run_receipt`, `release_manifest`, `correction_notice`, `promotion_decision`, `source_state_hash`, `catalog_matrix`, `layer_manifest`, `decision_envelope`, `flora_decision_envelope`, `evidence_bundle`, `evidence_drawer_payload`, `domain_observation`, `domain_feature_identity`, `domain_validation_report`, `domain_layer_descriptor`. | **NEEDS VERIFICATION** |

> [!CAUTION]
> The presence of files in the domain lane does not prove field completeness, accepted schema status, fixture coverage, validator wiring, policy behavior, release readiness, or public-safety approval.

---

## What belongs here

- This README.
- Alias, migration, mirror, or deprecation notes for `schemas/contracts/v1/flora/` if needed.
- Pointers to the accepted Flora schema home.
- Drift notes explaining why schema files should not be added directly here.

---

## What does not belong here

- Canonical Flora JSON Schema files unless an accepted ADR/migration authorizes this path.
- Domain-specific Flora schema files that belong under `schemas/contracts/v1/domains/flora/`.
- Semantic contract prose.
- Policy rules, sensitivity decisions, redaction decisions, or exposure decisions.
- Validator code, packages, pipelines, runtime code, or public UI/API implementation.
- Lifecycle data, occurrence records, source registry records, SourceDescriptor instances, receipt instances, proof outputs, catalog records, triplets, release records, correction notices, rollback cards, map tiles, dashboards, screenshots, or generated summaries.
- Precise rare/protected plant locations, culturally sensitive plant knowledge, private-land joins, steward-controlled records, or reversible redaction details.

---

## Flora sensitivity guardrails

Flora schema work must preserve fail-closed treatment for:

- exact occurrence geometry for rare, protected, culturally sensitive, or steward-controlled plants;
- seed-source, collection, harvest, medicinal/traditional-use, or sensitive ecological knowledge where publication could cause harm;
- sensitive restoration, monitoring, or survey locations;
- private-land joins and landowner-adjacent records;
- invasive plant records where exposure could create harm or misuse;
- any public layer or API response that could reveal protected locations through joins, residual geometry, small counts, timestamps, source identifiers, or reversible redaction.

Default public posture:

```text
precise sensitive data -> deny, restrict, generalize, aggregate, delay, or quarantine
public-safe display    -> released projection with evidence, policy, redaction, correction, and rollback support
schema validity        -> never enough for publication
```

---

## Migration rules

Do not move or duplicate Flora schemas into this top-level path unless a reviewed migration plan defines:

- source path;
- target path;
- owning root;
- reason for migration;
- schema `$id` changes;
- `$ref` and consumer updates;
- fixture and validator updates;
- schema registry updates;
- policy/sensitivity review;
- release and rollback impact;
- deprecation/mirror window;
- tests proving no parallel authority remains.

---

## Validation

Recommended local validation sequence:

```bash
# Confirm this alias path remains README-only unless migration is authorized.
find schemas/contracts/v1/flora -maxdepth 2 -type f | sort

# Inspect the active Flora domain schema lane.
find schemas/contracts/v1/domains/flora -maxdepth 3 -type f | sort

# Detect duplicate flora schema authority across top-level and domain paths.
find schemas/contracts/v1 -maxdepth 5 -type f \
  | grep -Ei '/flora/|/domains/flora/' \
  | sort

# Validate JSON syntax for the active domain lane.
find schemas/contracts/v1/domains/flora -name '*.schema.json' -print0 \
  | xargs -0 -r -I{} python -m json.tool {} >/dev/null

# Run project validators when available.
python tools/validate_all.py || true
pytest tests/schemas tests/contract tests/domains/flora tests/policy || true
```

Replace `|| true` with fail-closed CI behavior once validator and test paths are confirmed.

---

## Rollback

Rollback for this README is ordinary Git rollback: revert the commit that changed `schemas/contracts/v1/flora/README.md`.

Rollback for any future migration into this path requires more care:

1. Revert or migrate schema files.
2. Restore canonical `$id` and `$ref` targets.
3. Restore paired contract links.
4. Restore fixtures, validators, schema registry records, and CI paths.
5. Restore policy/sensitivity references.
6. Restore domain API/UI/MapLibre/Evidence Drawer consumers.
7. Preserve correction and rollback records if any public Flora surface was affected.

---

## Open questions

| Question | Status | Owner |
|---|---|---|
| Should `schemas/contracts/v1/flora/` remain README-only as an alias guardrail? | **PROPOSED** | Schema steward + Flora steward |
| Is there any accepted ADR authorizing top-level domain schema folders outside `domains/<domain>/`? | **NEEDS VERIFICATION** | Schema steward |
| Should duplicate/profile variants such as `range_polygon.schema.json` vs `range_polygon.flora.schema.json`, `habitat_association.schema.json` vs `habitat_association.flora.schema.json`, and `redaction_receipt.schema.json` vs `redaction_receipt.flora.schema.json` be consolidated or profiled? | **NEEDS VERIFICATION / ADR-sensitive** | Flora steward + schema steward |
| Which Flora schema files are field-complete and fixture-tested? | **NEEDS VERIFICATION** | Validation steward |
| Which Flora schemas are safe for public API/MapLibre/Focus Mode use? | **NEEDS VERIFICATION / release-gated** | Release steward + policy steward |

---

## Maintainer notes

- Keep this path as a guardrail unless a reviewed migration says otherwise.
- Put Flora domain schemas under `schemas/contracts/v1/domains/flora/`.
- Do not let this alias become a parallel authority.
- Preserve geoprivacy, sensitivity, evidence, policy, release, correction, and rollback boundaries for all Flora surfaces.
