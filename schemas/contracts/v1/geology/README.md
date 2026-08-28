# `schemas/contracts/v1/geology/` — Geology Schema Alias Guardrail

<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/schemas-contracts-v1-geology-readme
title: schemas/contracts/v1/geology/ — Geology Schema Alias Guardrail
type: readme; schema-alias-index; drift-guardrail; domain-schema-boundary
authority_class: alias-guardrail
version: v0.1
status: draft; empty-alias-index; domain-home-elsewhere; no-current-schema-files-found; do-not-promote-without-ADR; NEEDS VERIFICATION before promotion
owners:
  - OWNER_TBD — Geology domain steward
  - OWNER_TBD — Schema steward
  - OWNER_TBD — Contract steward
  - OWNER_TBD — Policy steward
  - OWNER_TBD — Release steward
  - OWNER_TBD — Validation steward
  - OWNER_TBD — Docs steward
created: NEEDS VERIFICATION — empty README existed before v0.1 expansion
updated: 2026-07-04
policy_label: public; schemas; contracts-v1; geology; alias-guardrail; domain-home-elsewhere; sublane-aware; surficial; bedrock; stratigraphy; lithology; natural-resources; evidence-bound; release-gated; rollback-aware; no-parallel-authority
tags: [kfm, schemas, contracts, v1, geology, alias, guardrail, domain-schema-lane, geologic-unit, geologic-age, lithology, stratigraphy, surficial, bedrock, structure, mineral-occurrence, resource-deposit, well-log, borehole, geochemistry, geophysics, reclamation, no-parallel-authority]
related:
  - ../README.md
  - ../domains/README.md
  - ../domains/geology/README.md
  - ../domains/geology/sublanes/README.md
  - ../domains/geology/sublanes/surficial/README.md
  - ../../../../docs/domains/geology/README.md
  - ../../../../docs/domains/geology/POLICY.md
  - ../../../../contracts/domains/geology/
  - ../../../../policy/domains/geology/
  - ../../../../fixtures/domains/geology/
  - ../../../../tests/domains/geology/
  - ../../../../release/candidates/geology/
notes:
  - "Expanded from an empty file at schemas/contracts/v1/geology/README.md."
  - "GitHub search did not surface existing schema files under schemas/contracts/v1/geology/ beyond this README in the current check."
  - "Current geology schema activity is under schemas/contracts/v1/domains/geology/, including README, sublane indexes, and many schema files surfaced by search."
  - "This file is an alias/guardrail index only; it must not become a parallel canonical geology schema home without ADR or migration note."
  - "Geology schemas may intersect resources, extraction sites, wells, boreholes, hazards, hydrology, archaeology, land/title, infrastructure, and sensitive-location policy. Preserve adjacent-domain and publication boundaries."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

![status](https://img.shields.io/badge/status-draft-yellow)
![root](https://img.shields.io/badge/root-schemas%2F-blue)
![family](https://img.shields.io/badge/family-geology-brown)
![posture](https://img.shields.io/badge/posture-alias__guardrail-orange)
![canonical](https://img.shields.io/badge/canonical-domain__lane__elsewhere-critical)
![release](https://img.shields.io/badge/release-gated-critical)
![truth](https://img.shields.io/badge/truth-cite--or--abstain-success)

> **Purpose.** `schemas/contracts/v1/geology/` is an empty alias/guardrail README for Geology schema placement.
>
> **One-line boundary.** The verified Geology schema lane is `schemas/contracts/v1/domains/geology/`. Do not add canonical Geology schema files directly under `schemas/contracts/v1/geology/` unless an accepted ADR, migration note, or compatibility plan authorizes this path.

---

## Quick jumps

[Status](#status) · [Placement decision](#placement-decision) · [Repo fit](#repo-fit) · [Current inventory](#current-inventory) · [Canonical lane inventory](#canonical-lane-inventory) · [What belongs here](#what-belongs-here) · [What does not belong here](#what-does-not-belong-here) · [Geology boundary guardrails](#geology-boundary-guardrails) · [Migration rules](#migration-rules) · [Validation](#validation) · [Rollback](#rollback) · [Open questions](#open-questions)

---

## Status

| Question | Answer | Truth label |
|---|---|---|
| Does this README path exist? | Yes: `schemas/contracts/v1/geology/README.md`. It was empty before this expansion. | **CONFIRMED** |
| Are schema files currently present under `schemas/contracts/v1/geology/`? | Not found in the current GitHub search beyond this README. | **NEEDS VERIFICATION / search-limited** |
| Where is current Geology schema activity? | `schemas/contracts/v1/domains/geology/` surfaced a README, sublane indexes, and many schema files. | **CONFIRMED path evidence** |
| Is this top-level `geology/` path canonical? | Not proven. Treat as alias/guardrail only. | **NEEDS VERIFICATION / do-not-promote-without-ADR** |
| Can this README validate Geology schema completeness? | No. It only prevents parallel authority and points to the domain lane. | **CONFIRMED boundary** |
| Can this path store source records, extraction records, well logs, receipts, or published map artifacts? | No. Schema docs must not store lifecycle data, source records, registry records, receipts, proofs, release records, or public artifacts. | **CONFIRMED boundary** |

> [!IMPORTANT]
> Geology is a domain lane, not a top-level schema family, unless an accepted ADR says otherwise. Keep authoritative Geology schema work under `schemas/contracts/v1/domains/geology/` and use this file only to prevent accidental duplicate schema authority.

---

## Placement decision

Current placement posture:

```text
Preferred / active domain schema lane:
  schemas/contracts/v1/domains/geology/

Do-not-use-as-canonical without ADR:
  schemas/contracts/v1/geology/
```

Rationale:

- ADR-0001-style schema placement uses `schemas/contracts/v1/domains/<domain>/...` for domain-specific schemas.
- The existing Geology domain schema README identifies `schemas/contracts/v1/domains/geology/` as the draft Geology domain schema lane.
- Current search surfaced many Geology schemas and child indexes under the domain lane and none under this top-level path.
- Maintaining both paths as independent schema homes would create validator drift, `$id` conflicts, stale fixtures, and publication-risk confusion.

---

## Repo fit

```text
schemas/
└── contracts/
    └── v1/
        ├── README.md
        ├── geology/
        │   └── README.md                       # this file; alias/guardrail only
        └── domains/
            └── geology/
                ├── README.md                   # active Geology domain schema index
                ├── *.schema.json               # current Geology schema files surfaced by search
                └── sublanes/
                    ├── README.md               # draft sublane index
                    └── surficial/
                        └── README.md           # draft Surficial schema sublane index

contracts/
└── domains/
    └── geology/                                # semantic meaning; not machine shape

docs/
└── domains/
    └── geology/                                # human-facing doctrine; not schema shape

policy/
└── domains/geology/                            # admissibility/policy posture; not schema shape

fixtures/
└── domains/geology/                            # valid/invalid examples; coverage NEEDS VERIFICATION

tests/
└── domains/geology/                            # behavioral proof; coverage NEEDS VERIFICATION

release/
└── candidates/geology/                         # promotion/release/correction/rollback surfaces
```

---

## Current inventory

Current check:

| Path | Status | Note |
|---|---|---|
| `schemas/contracts/v1/geology/README.md` | **CONFIRMED present** | Empty file expanded by this README. |
| `schemas/contracts/v1/geology/*.schema.json` | **Not found in current search** | Do not create here without ADR or migration note. |
| `schemas/contracts/v1/domains/geology/README.md` | **CONFIRMED present** | Active Geology domain schema index. |
| `schemas/contracts/v1/domains/geology/sublanes/README.md` | **CONFIRMED present** | Draft sublane index; convention still needs review. |
| `schemas/contracts/v1/domains/geology/sublanes/surficial/README.md` | **CONFIRMED present** | Draft Surficial child index. |
| `schemas/contracts/v1/domains/geology/*.schema.json` | **CONFIRMED surfaced by search** | Many schema files were found; each file's maturity still requires per-file verification. |

---

## Canonical lane inventory

Current search surfaced the following files under `schemas/contracts/v1/domains/geology/`. This is a search-derived inventory, not a complete mounted-checkout manifest.

| Surfaced path | Role signal | Posture |
|---|---|---|
| `README.md` | Geology domain schema index. | **CONFIRMED present** |
| `sublanes/README.md` | Draft Geology schema sublane index. | **NEEDS VERIFICATION / convention-sensitive** |
| `sublanes/surficial/README.md` | Draft Surficial child schema index. | **NEEDS VERIFICATION / convention-sensitive** |
| `geologic_unit.schema.json` | Geologic unit shape. | **NEEDS VERIFICATION** |
| `geologic_age.schema.json` | Geologic age shape. | **NEEDS VERIFICATION** |
| `lithology.schema.json` | Lithology/vocabulary shape. | **NEEDS VERIFICATION** |
| `stratigraphic_interval.schema.json` | Stratigraphic interval shape. | **NEEDS VERIFICATION** |
| `structure_feature.schema.json` | Structural feature shape. | **NEEDS VERIFICATION** |
| `cross_section.schema.json` | Cross-section/interpretation shape. | **NEEDS VERIFICATION** |
| `core_sample.schema.json` | Core sample shape. | **NEEDS VERIFICATION** |
| `geochemistry_sample.schema.json` | Geochemistry sample shape. | **NEEDS VERIFICATION** |
| `geophysical_observation.schema.json` | Geophysical observation shape. | **NEEDS VERIFICATION** |
| `borehole_reference.schema.json` | Borehole reference shape. | **NEEDS VERIFICATION** |
| `well_log_reference.schema.json` | Well-log reference shape. | **NEEDS VERIFICATION** |
| `hydrostratigraphic_unit.schema.json` | Hydrostratigraphic unit shape; hydrology-adjacent. | **NEEDS VERIFICATION / cross-domain boundary** |
| `mineral_occurrence.schema.json` | Mineral occurrence shape. | **NEEDS VERIFICATION / resource-sensitive** |
| `resource_deposit.schema.json` | Resource deposit shape. | **NEEDS VERIFICATION / resource-sensitive** |
| `resource_estimate.schema.json` | Resource estimate shape. | **NEEDS VERIFICATION / uncertainty-sensitive** |
| `extraction_site.schema.json` | Extraction site shape. | **NEEDS VERIFICATION / sensitivity-policy review** |
| `reclamation_record.schema.json` | Reclamation record shape. | **NEEDS VERIFICATION** |
| `geoprivacy_transform_receipt.schema.json` | Geoprivacy transform receipt shape. | **NEEDS VERIFICATION / receipt-home-sensitive** |
| Governance support schemas | `run_receipt`, `release_manifest`, `rollback_card`, `correction_notice`, `promotion_decision`, `source_state_hash`, `catalog_matrix`, `layer_manifest`, `geology_layer_manifest`, `decision_envelope`, `geology_decision_envelope`, `evidence_bundle`, `evidence_drawer_payload`, `domain_observation`, `domain_feature_identity`, `domain_validation_report`, `domain_layer_descriptor`. | **NEEDS VERIFICATION** |

> [!CAUTION]
> The presence of files in the domain lane does not prove field completeness, accepted schema status, fixture coverage, validator wiring, policy behavior, release readiness, or public-safety approval.

---

## What belongs here

- This README.
- Alias, migration, mirror, or deprecation notes for `schemas/contracts/v1/geology/` if needed.
- Pointers to the accepted Geology schema home.
- Drift notes explaining why schema files should not be added directly here.

---

## What does not belong here

- Canonical Geology JSON Schema files unless an accepted ADR/migration authorizes this path.
- Domain-specific Geology schema files that belong under `schemas/contracts/v1/domains/geology/`.
- Semantic contract prose.
- Policy rules, sensitivity decisions, redaction decisions, exposure decisions, or release decisions.
- Validator code, packages, pipelines, runtime code, or public UI/API implementation.
- Lifecycle data, source registry records, SourceDescriptor instances, well logs, borehole files, sample records, extraction records, receipt instances, proof outputs, catalog records, triplets, release records, correction notices, rollback cards, map tiles, dashboards, screenshots, or generated summaries.
- Claims of legal mineral rights, property title, operational authority, live extraction status, safety status, resource certainty, or public-safe exposure merely because an object validates against a schema.

---

## Geology boundary guardrails

Geology schema work must preserve boundaries around:

- geologic interpretation versus measured observation;
- map unit geometry versus released public layer;
- resource occurrence versus resource estimate versus extraction operation;
- well-log or borehole reference versus raw proprietary/log data;
- hydrostratigraphic unit versus hydrology authority;
- extraction/reclamation records versus regulatory/legal authority;
- archaeology-adjacent formations, caves, fossil sites, culturally sensitive sites, or precise sensitive locations;
- private-land, parcel, ownership, mineral rights, and living-person joins;
- public map display versus canonical evidence truth.

Default public posture:

```text
uncertain geology claim -> cite, qualify, or abstain
sensitive/resource location -> deny, restrict, generalize, aggregate, delay, or quarantine
public-safe display -> released projection with evidence, policy, correction, and rollback support
schema validity -> never enough for publication
```

---

## Migration rules

Do not move or duplicate Geology schemas into this top-level path unless a reviewed migration plan defines:

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
- sublane impact;
- deprecation/mirror window;
- tests proving no parallel authority remains.

---

## Validation

Recommended local validation sequence:

```bash
# Confirm this alias path remains README-only unless migration is authorized.
find schemas/contracts/v1/geology -maxdepth 2 -type f | sort

# Inspect the active Geology domain schema lane.
find schemas/contracts/v1/domains/geology -maxdepth 4 -type f | sort

# Detect duplicate geology schema authority across top-level and domain paths.
find schemas/contracts/v1 -maxdepth 6 -type f \
  | grep -Ei '/geology/|/domains/geology/' \
  | sort

# Validate JSON syntax for the active domain lane.
find schemas/contracts/v1/domains/geology -name '*.schema.json' -print0 \
  | xargs -0 -r -I{} python -m json.tool {} >/dev/null

# Run project validators when available.
python tools/validate_all.py || true
pytest tests/schemas tests/contract tests/domains/geology tests/policy || true
```

Replace `|| true` with fail-closed CI behavior once validator and test paths are confirmed.

---

## Rollback

Rollback for this README is ordinary Git rollback: revert the commit that changed `schemas/contracts/v1/geology/README.md`.

Rollback for any future migration into this path requires more care:

1. Revert or migrate schema files.
2. Restore canonical `$id` and `$ref` targets.
3. Restore paired contract links.
4. Restore fixtures, validators, schema registry records, and CI paths.
5. Restore policy/sensitivity references.
6. Restore sublane/domain API/UI/MapLibre/Evidence Drawer consumers.
7. Preserve correction and rollback records if any public Geology surface was affected.

---

## Open questions

| Question | Status | Owner |
|---|---|---|
| Should `schemas/contracts/v1/geology/` remain README-only as an alias guardrail? | **PROPOSED** | Schema steward + Geology steward |
| Is there any accepted ADR authorizing top-level domain schema folders outside `domains/<domain>/`? | **NEEDS VERIFICATION** | Schema steward |
| Should the `sublanes/` convention under `domains/geology/` be formally accepted, revised, or removed? | **NEEDS VERIFICATION / ADR-sensitive** | Geology steward + schema steward |
| Which Geology schema files are field-complete and fixture-tested? | **NEEDS VERIFICATION** | Validation steward |
| Which Geology schemas are safe for public API/MapLibre/Focus Mode use? | **NEEDS VERIFICATION / release-gated** | Release steward + policy steward |
| Which resource/extraction/well-log fields require redaction, aggregation, or access restriction? | **NEEDS VERIFICATION / policy-sensitive** | Policy steward + Geology steward |

---

## Maintainer notes

- Keep this path as a guardrail unless a reviewed migration says otherwise.
- Put Geology domain schemas under `schemas/contracts/v1/domains/geology/`.
- Do not let this alias become a parallel authority.
- Preserve evidence, uncertainty, adjacent-domain, policy, release, correction, and rollback boundaries for all Geology surfaces.
