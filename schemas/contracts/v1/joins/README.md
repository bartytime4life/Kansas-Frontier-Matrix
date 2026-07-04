# `schemas/contracts/v1/joins/` — Cross-Domain Join Schema Family Index

<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/schemas-contracts-v1-joins-readme
title: schemas/contracts/v1/joins/ — Cross-Domain Join Schema Family Index
type: readme; schema-family-index; join-schema-boundary; cross-domain-guardrail
authority_class: schema-family-index
version: v0.1
status: draft; join-family-present; mixed-schema-and-guardrail-lanes; PROPOSED; no-parallel-authority; NEEDS VERIFICATION before promotion
owners:
  - OWNER_TBD — Join steward
  - OWNER_TBD — Schema steward
  - OWNER_TBD — Contract steward
  - OWNER_TBD — Domain stewards for affected domains
  - OWNER_TBD — Policy steward
  - OWNER_TBD — Release steward
  - OWNER_TBD — Validation steward
  - OWNER_TBD — Docs steward
created: NEEDS VERIFICATION — empty README existed before v0.1 expansion
updated: 2026-07-04
policy_label: public; schemas; contracts-v1; joins; cross-domain; relationship-shape; evidence-bound; policy-aware; release-gated; rollback-aware; no-parallel-authority
tags: [kfm, schemas, contracts, v1, joins, cross-domain, relationship-shape, habitat-fauna, agriculture-hydrology, hydrology-hazards, hydrology-settlements, hydrology-soil, migration-routes, alias-guardrails, no-parallel-authority]
related:
  - ../README.md
  - ../domains/README.md
  - ./habitat-fauna-join.schema.json
  - ./agriculture-hydrology/README.md
  - ./hydrology_agriculture/README.md
  - ./hydrology_hazards/README.md
  - ./hydrology_settlements/README.md
  - ./hydrology_soil/README.md
  - ./migration-routes/README.md
  - ../domains/agriculture/README.md
  - ../domains/habitat/README.md
  - ../domains/fauna/README.md
  - ../domains/hydrology/README.md
  - ../domains/hazards/README.md
  - ../domains/soil/README.md
  - ../domains/settlement/README.md
  - ../domains/settlements-infrastructure/README.md
  - ../domains/roads-rail-trade/README.md
  - ../domains/transport/README.md
  - ../domains/roads/README.md
  - ../../../../contracts/domains/
  - ../../../../docs/architecture/cross-domain/README.md
  - ../../../../policy/
  - ../../../../fixtures/
  - ../../../../tests/
  - ../../../../release/
notes:
  - "Expanded from an empty file at schemas/contracts/v1/joins/README.md."
  - "Current search surfaced habitat-fauna-join.schema.json, agriculture-hydrology/README.md, and hydrology_agriculture/README.md under this folder; additional recently updated join README guardrails were verified by direct fetch in the current work sequence."
  - "habitat-fauna-join.schema.json is an actual PROPOSED scaffold schema with empty properties and additionalProperties true."
  - "Most child directories are guardrail-only README lanes and do not yet contain accepted join schemas."
  - "This folder defines relationship shape only; it must not replace domain schema lanes, emitted joined data, proof outputs, policy decisions, release records, or public artifacts."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

![status](https://img.shields.io/badge/status-draft-yellow)
![root](https://img.shields.io/badge/root-schemas%2F-blue)
![family](https://img.shields.io/badge/family-joins-purple)
![authority](https://img.shields.io/badge/authority-relationship--shape-informational)
![maturity](https://img.shields.io/badge/maturity-PROPOSED-orange)
![release](https://img.shields.io/badge/release-gated-critical)
![truth](https://img.shields.io/badge/truth-cite--or--abstain-success)

> **Purpose.** `schemas/contracts/v1/joins/` is the schema family for cross-domain relationship shapes: objects that connect references owned by two or more domain schema lanes without copying, replacing, or collapsing those domains' canonical records.
>
> **One-line boundary.** Join schemas define relationship shape only. They do not own domain truth, source truth, policy decisions, emitted joined datasets, proof outputs, release records, route authority, public map artifacts, or AI answer authority.

---

## Quick jumps

[Status](#status) · [Authority and placement](#authority-and-placement) · [Repo fit](#repo-fit) · [Current inventory](#current-inventory) · [Child lane posture](#child-lane-posture) · [What belongs here](#what-belongs-here) · [What does not belong here](#what-does-not-belong-here) · [Join-family rules](#join-family-rules) · [Promotion checklist](#promotion-checklist) · [Validation](#validation) · [Rollback](#rollback) · [Open questions](#open-questions)

---

## Status

| Question | Answer | Truth label |
|---|---|---|
| Does this README path exist? | Yes: `schemas/contracts/v1/joins/README.md`. It was empty before this expansion. | **CONFIRMED** |
| Does this folder contain at least one schema file? | Yes. `habitat-fauna-join.schema.json` was opened and is a PROPOSED scaffold. | **CONFIRMED** |
| Does this folder contain join child README guardrails? | Yes. Search and direct fetch surfaced multiple child README guardrails. | **CONFIRMED / search-limited** |
| Are all join lanes accepted canonical homes? | No. Most child lanes are explicitly README-only or do-not-promote-without-ADR guardrails. | **CONFIRMED posture** |
| Can a join schema replace domain schemas? | No. Join schemas should reference domain-owned objects and keep domain authority separate. | **CONFIRMED boundary** |
| Can this folder store joined datasets, receipts, proofs, release records, or map artifacts? | No. This folder is for schema files and schema-family documentation only. | **CONFIRMED boundary** |

> [!IMPORTANT]
> A join schema is not a data product. It does not prove that a join has been computed, reviewed, released, corrected, or made public-safe. It only constrains the shape of a proposed relationship object.

---

## Authority and placement

This folder belongs under the schema responsibility root:

```text
schemas/contracts/v1/joins/
```

It may define cross-domain JSON Schema shapes when the following are clear:

- which domains own the joined objects;
- which stable references are used;
- which contract describes the relationship meaning;
- which fixtures prove valid and invalid relationships;
- which validators enforce the schema;
- which policy, evidence, release, correction, and rollback references are required;
- whether a child lane is an accepted home, a temporary guardrail, or a compatibility alias.

Adjacent authority remains separate:

- `schemas/contracts/v1/domains/<domain>/` owns domain-specific machine shapes.
- `contracts/` owns semantic meaning.
- `policy/` owns allow/deny/restrict/abstain posture.
- `fixtures/` and `tests/` prove examples and validator behavior.
- `data/` owns lifecycle records, registry records, receipts, proofs, catalog/triplet records, and published data products where applicable.
- `release/` owns promotion, release, correction, withdrawal, and rollback records.

---

## Repo fit

```text
schemas/
└── contracts/
    └── v1/
        ├── README.md
        ├── joins/
        │   ├── README.md                         # this file
        │   ├── habitat-fauna-join.schema.json    # PROPOSED scaffold schema
        │   ├── agriculture-hydrology/
        │   │   └── README.md                     # join guardrail
        │   ├── hydrology_agriculture/
        │   │   └── README.md                     # duplicate-slug alias guardrail
        │   ├── hydrology_hazards/
        │   │   └── README.md                     # join guardrail
        │   ├── hydrology_settlements/
        │   │   └── README.md                     # join guardrail
        │   ├── hydrology_soil/
        │   │   └── README.md                     # join guardrail
        │   └── migration-routes/
        │       └── README.md                     # ambiguous-term guardrail
        └── domains/
            ├── agriculture/
            ├── fauna/
            ├── habitat/
            ├── hazards/
            ├── hydrology/
            ├── roads-rail-trade/
            ├── settlement/
            ├── settlements-infrastructure/
            └── soil/

contracts/
policy/
fixtures/
tests/
data/
release/
```

---

## Current inventory

This inventory is based on current search plus direct fetches from the current work sequence. GitHub search may lag recently committed files, so each child lane still carries a verification posture.

| Path | Kind | Current posture | Note |
|---|---|---|---|
| `README.md` | README | **CONFIRMED present** | Parent join schema family index. |
| `habitat-fauna-join.schema.json` | JSON Schema | **PROPOSED scaffold** | Draft 2020-12 object; `$id` uses `https://schemas.kfm.local/...`; empty `properties`; `additionalProperties: true`; `contract_doc: null`. |
| `agriculture-hydrology/README.md` | Child README | **Guardrail** | Neutral Agriculture–Hydrology join placement; not a canonical schema file lane without ADR. |
| `hydrology_agriculture/README.md` | Child README | **Duplicate-slug alias guardrail** | Underscore/reversed-order alias for Agriculture–Hydrology; should not become parallel authority. |
| `hydrology_hazards/README.md` | Child README | **Guardrail** | Hydrology–Hazards relationship-shape lane; no direct schema files found during that edit. |
| `hydrology_settlements/README.md` | Child README | **Guardrail** | Hydrology–Settlements relationship-shape lane; settlement slug conflict remains visible. |
| `hydrology_soil/README.md` | Child README | **Guardrail** | Hydrology–Soil relationship-shape lane; no direct schema files found during that edit. |
| `migration-routes/README.md` | Child README | **Ambiguity guardrail** | Keeps Fauna migration routes separate from transport/trade/human-route meaning until stewards decide. |

---

## Child lane posture

| Lane | Relationship | Required discipline |
|---|---|---|
| `habitat-fauna-join.schema.json` | Habitat ↔ Fauna | Needs paired contract, fields, fixtures, validator coverage, and policy/sensitivity review before promotion. |
| `agriculture-hydrology/` | Agriculture ↔ Hydrology | Must not replace Agriculture, Hydrology, or Agriculture `hydrology-ext/` authority. |
| `hydrology_agriculture/` | Hydrology ↔ Agriculture alias | Keep README-only unless an ADR chooses this slug and migrates the hyphenated path. |
| `hydrology_hazards/` | Hydrology ↔ Hazards | Must preserve Hydrology and Hazards ownership plus time/freshness and release posture. |
| `hydrology_settlements/` | Hydrology ↔ Settlements/Infrastructure | Must preserve settlement slug conflict and the broader `settlements-infrastructure` working lane. |
| `hydrology_soil/` | Hydrology ↔ Soil | Must preserve domain-owned hydrology and soil objects; use references rather than copied fields. |
| `migration-routes/` | Ambiguous route/migration relationships | Must first resolve whether the meaning is ecological, historical/human, transport/trade, or a governed cross-domain join. |

---

## What belongs here

- This README.
- Cross-domain JSON Schema files after placement, contract, fixture, validator, and steward review.
- Child README guardrails for unsettled or candidate join lanes.
- Alias, migration, mirror, deprecation, and slug-drift notes for join paths.
- Links to paired semantic contracts, domain schema lanes, policy references, evidence references, fixtures, tests, release references, correction references, and rollback references.

---

## What does not belong here

- Domain-owned canonical schemas.
- Semantic contract prose beyond README boundary notes.
- Policy rules, sensitivity decisions, exposure decisions, or release decisions.
- Joined datasets, lifecycle data, source records, catalog records, triplets, receipt instances, proof outputs, release records, correction notices, rollback cards, public map artifacts, dashboards, screenshots, or generated summaries.
- Validator code, packages, pipelines, runtime code, or UI/API implementation.
- Claims that a join is valid, complete, true, current, policy-safe, release-approved, or public-ready merely because it validates against a schema.

---

## Join-family rules

| Rule | Requirement |
|---|---|
| Reference, do not copy | Join schemas should use stable references to domain-owned objects rather than duplicating domain fields. |
| Domain ownership remains intact | A join object never becomes the canonical record for either side of the relationship. |
| Meaning must be paired | Each accepted join schema needs a semantic contract or an approved contract profile. |
| Evidence must be explicit | Claims derived from joins require EvidenceBundle or equivalent support. |
| Policy must travel with public use | Joins that affect access, exposure, or public display need policy posture and release support. |
| Time must be explicit | Joins involving observations, models, hazards, or changing infrastructure need observation/retrieval/release/correction time where applicable. |
| Sensitivity must fail closed | Joins involving fauna, flora, living-person data, private land, archaeology, precise sensitive locations, or controlled records require explicit sensitivity review. |
| Guardrails are not accepted schemas | A child README does not authorize a schema home unless the child lane says it has been accepted by ADR/steward review. |
| No parallel authority | Do not maintain equivalent schemas under `joins/` and a domain lane without a mirror/migration rule. |

---

## Promotion checklist

A join schema or child lane should not advance beyond `PROPOSED` unless:

- [ ] Owning domains are identified.
- [ ] Join-home placement is settled.
- [ ] Slug convention is settled.
- [ ] Paired semantic contract exists.
- [ ] `$id` is stable and uses the accepted schema namespace convention.
- [ ] Domain references are stable and do not copy domain-owned fields unnecessarily.
- [ ] Required fields are defined.
- [ ] Valid fixtures exist.
- [ ] Invalid fixtures exist.
- [ ] Validator support exists.
- [ ] CI/schema-test coverage exists.
- [ ] Policy and sensitivity dependencies are explicit.
- [ ] Evidence dependencies are explicit.
- [ ] Public/release use is gated by release/correction/rollback support.
- [ ] Migration notes exist for aliases, mirrors, slug variants, or duplicate paths.

---

## Validation

Recommended local validation sequence:

```bash
# Inspect the join schema family.
find schemas/contracts/v1/joins -maxdepth 4 -type f | sort

# Find actual schema files in the join family.
find schemas/contracts/v1/joins -name '*.schema.json' -type f | sort

# Find child README guardrails.
find schemas/contracts/v1/joins -name 'README.md' -type f | sort

# Detect likely duplicate join/extension authority.
find schemas/contracts/v1 -maxdepth 7 -type f \
  | grep -Ei 'join|hydrology.*agriculture|agriculture.*hydrology|hydrology.*hazards|hydrology.*settlements|hydrology.*soil|migration.*route|habitat.*fauna|fauna.*habitat' \
  | sort

# Validate JSON syntax for actual join schemas.
find schemas/contracts/v1/joins -name '*.schema.json' -print0 \
  | xargs -0 -r -I{} python -m json.tool {} >/dev/null

# Run project validators when available.
python tools/validate_all.py || true
pytest tests/schemas tests/contract tests/policy || true
```

Replace `|| true` with fail-closed CI behavior once validator and test paths are confirmed.

---

## Rollback

Rollback for this README is ordinary Git rollback: revert the commit that changed `schemas/contracts/v1/joins/README.md`.

Rollback for future join schema changes requires checking every downstream reference:

1. Revert or migrate schema files.
2. Restore canonical `$id` and `$ref` targets.
3. Restore paired contract links.
4. Restore fixtures, validators, schema registry records, and CI paths.
5. Restore domain, policy, evidence, release, correction, and receipt references.
6. Restore API/UI/MapLibre/Evidence Drawer consumers.
7. Preserve correction and rollback records if any public join surface was affected.

---

## Open questions

| Question | Status | Owner |
|---|---|---|
| Should all neutral cross-domain join schemas live under `schemas/contracts/v1/joins/`, or should some remain domain-owned extension profiles? | **NEEDS VERIFICATION / ADR-sensitive** | Schema steward + domain stewards |
| Should join child lane slugs use hyphens, underscores, domain order, or a registry-backed canonical slug convention? | **NEEDS VERIFICATION / slug-sensitive** | Schema steward + Join steward |
| Should `habitat-fauna-join.schema.json` remain as a flat schema file or move into a child lane? | **NEEDS VERIFICATION / migration-sensitive** | Habitat steward + Fauna steward + Schema steward |
| Which join schemas have paired semantic contracts? | **NEEDS VERIFICATION** | Contract steward |
| Which join schemas have valid/invalid/public-safe/sensitivity fixtures? | **NEEDS VERIFICATION** | Validation steward |
| Which join outputs are safe for public API/MapLibre/Focus Mode use? | **NEEDS VERIFICATION / release-gated** | Release steward + Policy steward |

---

## Maintainer notes

- Keep this folder focused on relationship shape, not joined data products.
- Prefer references to domain-owned objects over copied fields.
- Treat README-only child lanes as guardrails until an ADR or steward review accepts them.
- Preserve evidence, sensitivity, domain ownership, policy, release, correction, and rollback boundaries for every join surface.
