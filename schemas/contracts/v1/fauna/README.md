# `schemas/contracts/v1/fauna/` — Fauna Schema Alias Guardrail

<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/schemas-contracts-v1-fauna-readme
title: schemas/contracts/v1/fauna/ — Fauna Schema Alias Guardrail
type: readme; schema-alias-index; drift-guardrail; domain-schema-boundary
authority_class: alias-guardrail
version: v0.1
status: draft; empty-alias-index; domain-home-elsewhere; no-current-schema-files-found; do-not-promote-without-ADR; NEEDS VERIFICATION before promotion
owners:
  - OWNER_TBD — Fauna domain steward
  - OWNER_TBD — Schema steward
  - OWNER_TBD — Contract steward
  - OWNER_TBD — Sensitivity steward
  - OWNER_TBD — Policy steward
  - OWNER_TBD — Release steward
  - OWNER_TBD — Validation steward
  - OWNER_TBD — Docs steward
created: NEEDS VERIFICATION — empty README existed before v0.1 expansion
updated: 2026-07-04
policy_label: public; schemas; contracts-v1; fauna; alias-guardrail; domain-home-elsewhere; sensitivity-aware; geoprivacy-aware; release-gated; rollback-aware; no-parallel-authority
tags: [kfm, schemas, contracts, v1, fauna, alias, guardrail, domain-schema-lane, geoprivacy, sensitive-taxa, occurrence, range, monitoring, redaction, receipts, no-parallel-authority]
related:
  - ../README.md
  - ../domains/README.md
  - ../domains/fauna/README.md
  - ../domains/fauna/receipts/README.md
  - ../../../../docs/domains/fauna/README.md
  - ../../../../docs/domains/fauna/SCHEMAS.md
  - ../../../../contracts/domains/fauna/
  - ../../../../policy/domains/fauna/
  - ../../../../fixtures/domains/fauna/
  - ../../../../tests/domains/fauna/
  - ../../../../release/candidates/fauna/
notes:
  - "Expanded from an empty file at schemas/contracts/v1/fauna/README.md."
  - "GitHub search did not surface existing schema files under schemas/contracts/v1/fauna/ beyond this README in the current check."
  - "Current fauna schema activity is under schemas/contracts/v1/domains/fauna/, including README and many schema files surfaced by search."
  - "This file is an alias/guardrail index only; it must not become a parallel canonical fauna schema home without ADR or migration note."
  - "Fauna schemas are sensitivity- and geoprivacy-significant; exact occurrence geometry, sensitive sites, telemetry, rare taxa, and private-land joins require fail-closed handling."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

![status](https://img.shields.io/badge/status-draft-yellow)
![root](https://img.shields.io/badge/root-schemas%2F-blue)
![family](https://img.shields.io/badge/family-fauna-green)
![posture](https://img.shields.io/badge/posture-alias__guardrail-orange)
![canonical](https://img.shields.io/badge/canonical-domain__lane__elsewhere-critical)
![sensitivity](https://img.shields.io/badge/sensitivity-fail--closed-red)
![truth](https://img.shields.io/badge/truth-cite--or--abstain-success)

> **Purpose.** `schemas/contracts/v1/fauna/` is an empty alias/guardrail README for Fauna schema placement.
>
> **One-line boundary.** The verified Fauna schema lane is `schemas/contracts/v1/domains/fauna/`. Do not add canonical Fauna schema files directly under `schemas/contracts/v1/fauna/` unless an accepted ADR, migration note, or compatibility plan authorizes this path.

---

## Quick jumps

[Status](#status) · [Placement decision](#placement-decision) · [Repo fit](#repo-fit) · [Current inventory](#current-inventory) · [Canonical lane inventory](#canonical-lane-inventory) · [What belongs here](#what-belongs-here) · [What does not belong here](#what-does-not-belong-here) · [Fauna sensitivity guardrails](#fauna-sensitivity-guardrails) · [Migration rules](#migration-rules) · [Validation](#validation) · [Rollback](#rollback) · [Open questions](#open-questions)

---

## Status

| Question | Answer | Truth label |
|---|---|---|
| Does this README path exist? | Yes: `schemas/contracts/v1/fauna/README.md`. It was empty before this expansion. | **CONFIRMED** |
| Are schema files currently present under `schemas/contracts/v1/fauna/`? | Not found in the current GitHub search beyond this README. | **NEEDS VERIFICATION / search-limited** |
| Where is current Fauna schema activity? | `schemas/contracts/v1/domains/fauna/` surfaced a README and many schema files. | **CONFIRMED path evidence** |
| Is this top-level `fauna/` path canonical? | Not proven. Treat as alias/guardrail only. | **NEEDS VERIFICATION / do-not-promote-without-ADR** |
| Can this README validate Fauna schema completeness? | No. It only prevents parallel authority and points to the domain lane. | **CONFIRMED boundary** |
| Can this path store public Fauna records or sensitive occurrence data? | No. Schema docs must not store lifecycle data, occurrences, source records, receipts, proofs, or sensitive details. | **CONFIRMED boundary** |

> [!IMPORTANT]
> Fauna is a domain lane, not a top-level schema family, unless an accepted ADR says otherwise. Keep authoritative Fauna schema work under `schemas/contracts/v1/domains/fauna/` and use this file only to prevent accidental duplicate schema authority.

---

## Placement decision

Current placement posture:

```text
Preferred / active domain schema lane:
  schemas/contracts/v1/domains/fauna/

Do-not-use-as-canonical without ADR:
  schemas/contracts/v1/fauna/
```

Rationale:

- ADR-0001-style schema placement uses `schemas/contracts/v1/domains/<domain>/...` for domain-specific schemas.
- The existing Fauna domain schema README already identifies `schemas/contracts/v1/domains/fauna/` as the Fauna domain schema lane.
- Current search surfaced many Fauna schemas under the domain lane and none under this top-level path.
- Maintaining both paths as independent schema homes would create validator drift, `$id` conflicts, stale fixtures, and publication-risk confusion.

---

## Repo fit

```text
schemas/
└── contracts/
    └── v1/
        ├── README.md
        ├── fauna/
        │   └── README.md                       # this file; alias/guardrail only
        └── domains/
            └── fauna/
                ├── README.md                   # active Fauna domain schema index
                ├── *.schema.json               # current Fauna schema files
                └── receipts/
                    └── README.md               # Fauna receipt schema child lane

contracts/
└── domains/
    └── fauna/                                  # semantic meaning; not machine shape

policy/
└── domains/fauna/                              # sensitivity/policy posture; not schema shape

fixtures/
└── domains/fauna/                              # valid/invalid examples; coverage NEEDS VERIFICATION

tests/
└── domains/fauna/                              # behavioral proof; coverage NEEDS VERIFICATION

release/
└── candidates/fauna/                           # promotion/release/correction/rollback surfaces
```

---

## Current inventory

Current check:

| Path | Status | Note |
|---|---|---|
| `schemas/contracts/v1/fauna/README.md` | **CONFIRMED present** | Empty file expanded by this README. |
| `schemas/contracts/v1/fauna/*.schema.json` | **Not found in current search** | Do not create here without ADR or migration note. |
| `schemas/contracts/v1/domains/fauna/README.md` | **CONFIRMED present** | Active Fauna domain schema index. |
| `schemas/contracts/v1/domains/fauna/*.schema.json` | **CONFIRMED surfaced by search** | Many schema files were found; each file's maturity still requires per-file verification. |

---

## Canonical lane inventory

Current search surfaced the following files under `schemas/contracts/v1/domains/fauna/`. This is a search-derived inventory, not a complete mounted-checkout manifest.

| Surfaced path | Role signal | Posture |
|---|---|---|
| `README.md` | Fauna domain schema index. | **CONFIRMED present** |
| `taxon.schema.json` | Taxonomic identity shape. | **NEEDS VERIFICATION** |
| `taxon_crosswalk.schema.json` | Authority taxonomy mapping. | **NEEDS VERIFICATION** |
| `feature_dto.schema.json` | Feature/API DTO shape. | **NEEDS VERIFICATION** |
| `domain_feature_identity.schema.json` | Domain feature identity shape. | **NEEDS VERIFICATION** |
| `occurrence_evidence.schema.json` | Evidence-bearing occurrence shape. | **NEEDS VERIFICATION** |
| `occurrence_restricted.schema.json` | Restricted occurrence shape. | **NEEDS VERIFICATION / sensitive** |
| `occurrence_public.schema.json` | Public-safe occurrence shape. | **NEEDS VERIFICATION / release-gated** |
| `range_polygon.schema.json` | Range geometry shape. | **NEEDS VERIFICATION** |
| `seasonal_range.schema.json` | Seasonal range shape. | **NEEDS VERIFICATION** |
| `migration_route.schema.json` | Migration route shape. | **NEEDS VERIFICATION / sensitivity review** |
| `monitoring_event.schema.json` | Monitoring event shape. | **NEEDS VERIFICATION** |
| `sensitive_site.schema.json` | Sensitive site shape. | **NEEDS VERIFICATION / fail-closed** |
| `conservation_status.schema.json` | Conservation/legal status shape. | **NEEDS VERIFICATION** |
| `abundance_indicator.schema.json` | Abundance indicator shape. | **NEEDS VERIFICATION** |
| `richness_indicator.schema.json` | Richness indicator shape. | **NEEDS VERIFICATION** |
| `mortality_observation.schema.json` | Mortality observation shape. | **NEEDS VERIFICATION** |
| `disease_observation.schema.json` | Disease observation shape. | **NEEDS VERIFICATION** |
| `invasive_species_record.schema.json` | Invasive species record shape. | **NEEDS VERIFICATION** |
| `redaction_receipt.schema.json` | Redaction receipt shape. | **PROPOSED / placement-sensitive** |
| `receipts/redaction_receipt.schema.json` | Fauna receipt child-lane redaction receipt. | **NEEDS VERIFICATION / possible duplicate authority** |
| Governance support schemas | `run_receipt`, `release_manifest`, `rollback_card`, `correction_notice`, `promotion_decision`, `source_state_hash`, `catalog_matrix`, `layer_manifest`, `decision_envelope`, `evidence_bundle`, `evidence_drawer_payload`, `domain_observation`, `domain_validation_report`, `domain_layer_descriptor`. | **NEEDS VERIFICATION** |

> [!CAUTION]
> The presence of files in the domain lane does not prove field completeness, accepted schema status, fixture coverage, validator wiring, policy behavior, release readiness, or public-safety approval.

---

## What belongs here

- This README.
- Alias, migration, mirror, or deprecation notes for `schemas/contracts/v1/fauna/` if needed.
- Pointers to the accepted Fauna schema home.
- Drift notes explaining why schema files should not be added directly here.

---

## What does not belong here

- Canonical Fauna JSON Schema files unless an accepted ADR/migration authorizes this path.
- Domain-specific Fauna schema files that belong under `schemas/contracts/v1/domains/fauna/`.
- Semantic contract prose.
- Policy rules, sensitivity decisions, redaction decisions, or exposure decisions.
- Validator code, packages, pipelines, runtime code, or public UI/API implementation.
- Lifecycle data, occurrence records, source registry records, SourceDescriptor instances, receipt instances, proof outputs, catalog records, triplets, release records, correction notices, rollback cards, map tiles, dashboards, screenshots, or generated summaries.
- Precise sensitive locations, rare-species sites, telemetry, private-land joins, or steward-controlled data.

---

## Fauna sensitivity guardrails

Fauna schema work must preserve fail-closed treatment for:

- exact occurrence geometry for sensitive taxa;
- nesting, denning, roosting, breeding, migration, telemetry, and seasonal concentration locations;
- sensitive sites and steward-controlled records;
- rare-species locations and private-land joins;
- disease, mortality, invasive species, or conservation-status records where exposure could cause harm;
- any public layer or API response that could reveal protected locations through joins, residual geometry, small counts, timestamps, or reversible redaction.

Default public posture:

```text
precise sensitive data -> deny, restrict, generalize, aggregate, delay, or quarantine
public-safe display    -> released projection with evidence, policy, redaction, correction, and rollback support
schema validity        -> never enough for publication
```

---

## Migration rules

Do not move or duplicate Fauna schemas into this top-level path unless a reviewed migration plan defines:

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
find schemas/contracts/v1/fauna -maxdepth 2 -type f | sort

# Inspect the active Fauna domain schema lane.
find schemas/contracts/v1/domains/fauna -maxdepth 3 -type f | sort

# Detect duplicate fauna schema authority across top-level and domain paths.
find schemas/contracts/v1 -maxdepth 5 -type f \
  | grep -Ei '/fauna/|/domains/fauna/' \
  | sort

# Validate JSON syntax for the active domain lane.
find schemas/contracts/v1/domains/fauna -name '*.schema.json' -print0 \
  | xargs -0 -r -I{} python -m json.tool {} >/dev/null

# Run project validators when available.
python tools/validate_all.py || true
pytest tests/schemas tests/contract tests/domains/fauna tests/policy || true
```

Replace `|| true` with fail-closed CI behavior once validator and test paths are confirmed.

---

## Rollback

Rollback for this README is ordinary Git rollback: revert the commit that changed `schemas/contracts/v1/fauna/README.md`.

Rollback for any future migration into this path requires more care:

1. Revert or migrate schema files.
2. Restore canonical `$id` and `$ref` targets.
3. Restore paired contract links.
4. Restore fixtures, validators, schema registry records, and CI paths.
5. Restore policy/sensitivity references.
6. Restore domain API/UI/MapLibre/Evidence Drawer consumers.
7. Preserve correction and rollback records if any public fauna surface was affected.

---

## Open questions

| Question | Status | Owner |
|---|---|---|
| Should `schemas/contracts/v1/fauna/` remain README-only as an alias guardrail? | **PROPOSED** | Schema steward + Fauna steward |
| Is there any accepted ADR authorizing top-level domain schema folders outside `domains/<domain>/`? | **NEEDS VERIFICATION** | Schema steward |
| Should duplicate redaction receipt schema placements inside `domains/fauna/` and `domains/fauna/receipts/` be consolidated? | **NEEDS VERIFICATION / ADR-sensitive** | Fauna steward + schema steward + receipt steward |
| Which Fauna schema files are field-complete and fixture-tested? | **NEEDS VERIFICATION** | Validation steward |
| Which Fauna schemas are safe for public API/MapLibre/Focus Mode use? | **NEEDS VERIFICATION / release-gated** | Release steward + policy steward |

---

## Maintainer notes

- Keep this path as a guardrail unless a reviewed migration says otherwise.
- Put Fauna domain schemas under `schemas/contracts/v1/domains/fauna/`.
- Do not let this alias become a parallel authority.
- Preserve geoprivacy, sensitivity, evidence, policy, release, correction, and rollback boundaries for all Fauna surfaces.
