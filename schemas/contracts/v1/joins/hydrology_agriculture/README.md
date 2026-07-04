# `schemas/contracts/v1/joins/hydrology_agriculture/` — Agriculture–Hydrology Join Alias Guardrail

<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/schemas-contracts-v1-joins-hydrology-agriculture-readme
title: schemas/contracts/v1/joins/hydrology_agriculture/ — Agriculture–Hydrology Join Alias Guardrail
type: readme; alias-guardrail; duplicate-slug-warning; join-schema-boundary
authority_class: alias-guardrail
version: v0.1
status: draft; empty-alias-index; duplicate-slug; canonical-join-home-unsettled; points-to-agriculture-hydrology; no-current-schema-files-found; do-not-promote-without-ADR; NEEDS VERIFICATION before promotion
owners:
  - OWNER_TBD — Agriculture domain steward
  - OWNER_TBD — Hydrology domain steward
  - OWNER_TBD — Join steward
  - OWNER_TBD — Schema steward
  - OWNER_TBD — Contract steward
  - OWNER_TBD — Validation steward
  - OWNER_TBD — Docs steward
created: NEEDS VERIFICATION — empty README existed before v0.1 expansion
updated: 2026-07-04
policy_label: public; schemas; contracts-v1; joins; hydrology_agriculture; duplicate-slug; agriculture-hydrology; alias-guardrail; no-parallel-authority
tags: [kfm, schemas, contracts, v1, joins, hydrology_agriculture, agriculture-hydrology, alias, duplicate-slug, guardrail, no-parallel-authority]
related:
  - ../../README.md
  - ../README.md
  - ../agriculture-hydrology/README.md
  - ../../domains/agriculture/README.md
  - ../../domains/agriculture/hydrology-ext/README.md
  - ../../domains/hydrology/README.md
  - ../../../../contracts/domains/agriculture/
  - ../../../../contracts/domains/hydrology/
  - ../../../../docs/domains/agriculture/
  - ../../../../docs/domains/hydrology/
notes:
  - "Expanded from an empty file at schemas/contracts/v1/joins/hydrology_agriculture/README.md."
  - "Current search did not surface schema files directly under this underscore join path beyond this README."
  - "The hyphenated join guardrail already exists at schemas/contracts/v1/joins/agriculture-hydrology/README.md."
  - "This underscore path is a duplicate-slug alias guardrail only; do not add canonical schemas here unless an accepted ADR chooses this slug and migrates the hyphenated path."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

![status](https://img.shields.io/badge/status-draft-yellow)
![root](https://img.shields.io/badge/root-schemas%2F-blue)
![family](https://img.shields.io/badge/family-joins-purple)
![posture](https://img.shields.io/badge/posture-alias__guardrail-orange)
![slug](https://img.shields.io/badge/slug-duplicate-orange)
![truth](https://img.shields.io/badge/truth-cite--or--abstain-success)

> **Purpose.** `schemas/contracts/v1/joins/hydrology_agriculture/` is an alias/duplicate-slug guardrail for Agriculture–Hydrology join schema placement.
>
> **One-line boundary.** Do not add canonical schemas here while `schemas/contracts/v1/joins/agriculture-hydrology/` already exists as the inspected Agriculture–Hydrology join guardrail.

---

## Quick jumps

[Status](#status) · [Placement decision](#placement-decision) · [Repo fit](#repo-fit) · [What belongs here](#what-belongs-here) · [What does not belong here](#what-does-not-belong-here) · [Slug migration rules](#slug-migration-rules) · [Validation](#validation) · [Rollback](#rollback) · [Open questions](#open-questions)

---

## Status

| Question | Answer | Truth label |
|---|---|---|
| Does this README path exist? | Yes: `schemas/contracts/v1/joins/hydrology_agriculture/README.md`. It was empty before this expansion. | **CONFIRMED** |
| Are schema files present under this underscore path? | Not found in the current search beyond this README. | **NEEDS VERIFICATION / search-limited** |
| Is there an overlapping hyphenated join path? | Yes: `schemas/contracts/v1/joins/agriculture-hydrology/README.md`. | **CONFIRMED** |
| Is either join path accepted as canonical? | Not proven. The hyphenated path is already the fuller guardrail; this underscore path is alias-only. | **NEEDS VERIFICATION / ADR-sensitive** |
| Can this alias path store joined data or released outputs? | No. Schema docs are not lifecycle data, emitted records, proofs, release records, or public artifacts. | **CONFIRMED boundary** |

> [!IMPORTANT]
> Keep this underscore path README-only unless a reviewed migration chooses it as the accepted slug. Do not create parallel `hydrology_agriculture` and `agriculture-hydrology` schema definitions.

---

## Placement decision

Current placement posture:

```text
Fuller inspected join guardrail:
  schemas/contracts/v1/joins/agriculture-hydrology/

Duplicate underscore alias guardrail:
  schemas/contracts/v1/joins/hydrology_agriculture/

Agriculture-owned extension lane:
  schemas/contracts/v1/domains/agriculture/hydrology-ext/

Domain schema lanes:
  schemas/contracts/v1/domains/agriculture/
  schemas/contracts/v1/domains/hydrology/
```

Rationale:

- The hyphenated `agriculture-hydrology` path already records the current Agriculture–Hydrology join-placement guardrail.
- This underscore path reverses the name order and changes separator style, which can create duplicate slug authority.
- Agriculture and Hydrology domain schema lanes remain the source homes for domain-owned shapes.
- The Agriculture `hydrology-ext/` lane remains the inspected Agriculture-owned extension lane.

---

## Repo fit

```text
schemas/
└── contracts/
    └── v1/
        ├── README.md
        ├── joins/
        │   ├── agriculture-hydrology/
        │   │   └── README.md                     # fuller inspected join guardrail
        │   └── hydrology_agriculture/
        │       └── README.md                     # this file; duplicate-slug alias only
        └── domains/
            ├── agriculture/
            │   ├── README.md
            │   └── hydrology-ext/
            │       └── README.md
            └── hydrology/
                └── README.md
```

---

## What belongs here

- This README.
- A short alias/deprecation/migration note for the underscore slug.
- Pointers to the accepted join schema home once a slug is chosen.
- Drift notes explaining why schema files should not be added here without review.

---

## What does not belong here

- Canonical Agriculture–Hydrology JSON Schema files unless an accepted ADR/migration authorizes this exact slug.
- Duplicate schemas already proposed or documented under `joins/agriculture-hydrology/`.
- Agriculture-owned canonical schemas.
- Hydrology-owned canonical schemas.
- Agriculture extension schemas that belong under `domains/agriculture/hydrology-ext/`.
- Semantic contract prose, policy rules, lifecycle data, joined datasets, source records, receipts, proofs, release records, public artifacts, validator code, packages, pipelines, runtime code, UI/API implementation, map tiles, dashboards, screenshots, or generated summaries.
- Claims that a join is valid, complete, true, or public-ready merely because it validates against a schema.

---

## Slug migration rules

If stewards choose `hydrology_agriculture` as the canonical slug, create a reviewed migration note that defines:

- why the underscore/reversed-order slug is preferred;
- source path and target path;
- schema `$id` changes;
- `$ref` and consumer updates;
- paired contract updates;
- fixture and validator updates;
- schema registry updates;
- Agriculture and Hydrology steward review;
- release and rollback impact;
- deprecation/mirror window for the non-canonical slug;
- tests proving no parallel authority remains.

Until then, treat this path as README-only.

---

## Validation

Recommended local validation sequence:

```bash
# Confirm this alias remains README-only.
find schemas/contracts/v1/joins/hydrology_agriculture -maxdepth 2 -type f | sort

# Compare all Agriculture-Hydrology join/extension paths.
find schemas/contracts/v1 -maxdepth 6 -type f \
  | grep -Ei 'agriculture-hydrology|hydrology_agriculture|hydrology-ext|agriculture.*hydrology|hydrology.*agriculture' \
  | sort

# Inspect related domain lanes.
find schemas/contracts/v1/domains/agriculture schemas/contracts/v1/domains/hydrology -maxdepth 4 -type f | sort

# Run project validators when available.
python tools/validate_all.py || true
pytest tests/schemas tests/contract tests/domains/agriculture tests/domains/hydrology tests/policy || true
```

Replace `|| true` with fail-closed CI behavior once validator and test paths are confirmed.

---

## Rollback

Rollback for this README is ordinary Git rollback: revert the commit that changed `schemas/contracts/v1/joins/hydrology_agriculture/README.md`.

Rollback for any future slug migration requires restoring the accepted schema home, `$id` targets, references, fixtures, validators, registry records, paired contracts, and any public/release consumers affected by the slug change.

---

## Open questions

| Question | Status | Owner |
|---|---|---|
| Should the accepted join slug be `agriculture-hydrology`, `hydrology_agriculture`, or another convention? | **NEEDS VERIFICATION / ADR-sensitive** | Schema steward + Join steward |
| Should this underscore path be deleted, deprecated, or retained as a README-only alias? | **PROPOSED** | Schema steward |
| Should neutral join schemas live under `joins/` or remain Agriculture-owned under `domains/agriculture/hydrology-ext/`? | **NEEDS VERIFICATION** | Agriculture steward + Hydrology steward |

---

## Maintainer notes

- Keep this path README-only unless the slug decision changes.
- Prefer one canonical join home, not parallel slugs.
- Preserve Agriculture ownership, Hydrology ownership, evidence, policy, release, correction, and rollback boundaries for all join surfaces.
