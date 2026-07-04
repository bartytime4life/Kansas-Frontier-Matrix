# `schemas/contracts/v1/hazards/` — Hazards Schema Home Conflict Guardrail

<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/schemas-contracts-v1-hazards-readme
title: schemas/contracts/v1/hazards/ — Hazards Schema Home Conflict Guardrail
type: readme; schema-alias-index; schema-home-conflict-note; hazards-boundary
authority_class: alias-guardrail
version: v0.1
status: draft; empty-alias-index; schema-home-conflict-visible; domain-home-populated; no-current-root-schema-files-found; do-not-promote-without-ADR; NEEDS VERIFICATION before promotion
owners:
  - OWNER_TBD — Hazards domain steward
  - OWNER_TBD — Schema steward
  - OWNER_TBD — Contract steward
  - OWNER_TBD — Receipt steward
  - OWNER_TBD — Freshness steward
  - OWNER_TBD — Policy steward
  - OWNER_TBD — Release steward
  - OWNER_TBD — Validation steward
  - OWNER_TBD — Docs steward
created: NEEDS VERIFICATION — empty README existed before v0.1 expansion
updated: 2026-07-04
policy_label: public; schemas; contracts-v1; hazards; alias-guardrail; schema-home-conflict; domain-home-populated; receipts; freshness; release-gated; rollback-aware; no-parallel-authority
tags: [kfm, schemas, contracts, v1, hazards, alias, guardrail, schema-home-conflict, domain-schema-lane, receipts, freshness, warning-context, release, rollback, evidence, policy, no-parallel-authority]
related:
  - ../README.md
  - ../domains/README.md
  - ../domains/hazards/README.md
  - ../domains/hazards/receipts/README.md
  - ../domains/hazards/source_descriptor.schema.json
  - ../domains/hazards/run_receipt.schema.json
  - ../domains/hazards/release_manifest.schema.json
  - ../domains/hazards/rollback_card.schema.json
  - ../domains/hazards/correction_notice.schema.json
  - ../domains/hazards/promotion_decision.schema.json
  - ../domains/hazards/decision_envelope.schema.json
  - ../domains/hazards/hazards_decision_envelope.schema.json
  - ../../../../docs/domains/hazards/README.md
  - ../../../../docs/domains/hazards/ARCHITECTURE.md
  - ../../../../contracts/domains/hazards/
  - ../../../../policy/domains/hazards/
  - ../../../../fixtures/domains/hazards/
  - ../../../../tests/domains/hazards/
  - ../../../../release/candidates/hazards/
notes:
  - "Expanded from an empty file at schemas/contracts/v1/hazards/README.md."
  - "Current search did not surface schema files directly under schemas/contracts/v1/hazards/ beyond this README in the current check."
  - "Active Hazards schema files were surfaced under schemas/contracts/v1/domains/hazards/."
  - "The Hazards domain schema README records a schema-home conflict: an older/default Hazards schema home was schemas/contracts/v1/hazards/, while the domains/hazards form is also present and populated."
  - "This README is a conflict/alias guardrail only; do not create parallel canonical Hazards schemas in both homes without ADR, migration note, and validator/fixture update plan."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

![status](https://img.shields.io/badge/status-draft-yellow)
![root](https://img.shields.io/badge/root-schemas%2F-blue)
![family](https://img.shields.io/badge/family-hazards-red)
![posture](https://img.shields.io/badge/posture-conflict__guardrail-orange)
![canonical](https://img.shields.io/badge/canonical-NEEDS__ADR-yellow)
![truth](https://img.shields.io/badge/truth-cite--or--abstain-success)

> **Purpose.** `schemas/contracts/v1/hazards/` is an empty top-level guardrail README for the unresolved Hazards schema-home question.
>
> **One-line boundary.** Current schema files were surfaced under `schemas/contracts/v1/domains/hazards/`; this top-level path must not become a parallel canonical Hazards schema home without an accepted ADR or migration plan.

---

## Quick jumps

[Status](#status) · [Placement decision](#placement-decision) · [Repo fit](#repo-fit) · [Current inventory](#current-inventory) · [Active domain-lane inventory](#active-domain-lane-inventory) · [Child receipt lane](#child-receipt-lane) · [What belongs here](#what-belongs-here) · [What does not belong here](#what-does-not-belong-here) · [Migration rules](#migration-rules) · [Validation](#validation) · [Rollback](#rollback) · [Open questions](#open-questions)

---

## Status

| Question | Answer | Truth label |
|---|---|---|
| Does this README path exist? | Yes: `schemas/contracts/v1/hazards/README.md`. It was empty before this expansion. | **CONFIRMED** |
| Are schema files currently present directly under `schemas/contracts/v1/hazards/`? | Not found in current search beyond this README. | **NEEDS VERIFICATION / search-limited** |
| Where are active Hazards schema files currently surfaced? | `schemas/contracts/v1/domains/hazards/` surfaced a README, receipts child README, and multiple schema files. | **CONFIRMED path evidence** |
| Is this top-level path canonical? | Not settled. The domain README records a Hazards schema-home conflict involving this path. | **NEEDS VERIFICATION / ADR-sensitive** |
| Can this README validate Hazards schema completeness? | No. It records placement posture and drift risk only. | **CONFIRMED boundary** |
| Can this path store emitted receipts, proofs, source payloads, release records, or public artifacts? | No. Schema docs are not emitted data, proof, catalog, release, or publication surfaces. | **CONFIRMED boundary** |

> [!IMPORTANT]
> Until the Hazards schema-home conflict is resolved, do not add canonical Hazards schemas here and also under `schemas/contracts/v1/domains/hazards/`. Use one accepted home, or document a temporary mirror/migration rule.

---

## Placement decision

Current placement posture:

```text
Populated Hazards schema lane found by search:
  schemas/contracts/v1/domains/hazards/

Empty top-level path requested here:
  schemas/contracts/v1/hazards/

Hazards receipt child currently surfaced under populated lane:
  schemas/contracts/v1/domains/hazards/receipts/
```

Rationale:

- General ADR-0001-style placement puts domain-specific schemas under `schemas/contracts/v1/domains/<domain>/...`.
- The Hazards domain schema README records a Hazards-specific schema-home conflict and says the older/default Hazards schema home was `schemas/contracts/v1/hazards/`.
- Current repo search surfaced multiple Hazards schema files under `schemas/contracts/v1/domains/hazards/`, not directly under this top-level path.
- This README therefore keeps the conflict visible rather than declaring this path canonical.

---

## Repo fit

```text
schemas/
└── contracts/
    └── v1/
        ├── README.md
        ├── hazards/
        │   └── README.md                         # this file; conflict/alias guardrail only
        └── domains/
            └── hazards/
                ├── README.md                     # populated Hazards domain schema index
                ├── receipts/
                │   └── README.md                 # draft Hazards receipt schema index
                └── *.schema.json                 # current Hazards schema files surfaced by search

contracts/
└── domains/hazards/                               # semantic meaning; not machine shape

policy/
└── domains/hazards/                               # admissibility/policy posture; not schema shape

fixtures/
tests/
release/
data/                                             # lifecycle/receipt/proof/catalog roots, not schema home
```

---

## Current inventory

| Path | Status | Note |
|---|---|---|
| `schemas/contracts/v1/hazards/README.md` | **CONFIRMED present** | Empty file expanded by this README. |
| `schemas/contracts/v1/hazards/*.schema.json` | **Not found in current search** | Do not create here without ADR or migration note. |
| `schemas/contracts/v1/domains/hazards/README.md` | **CONFIRMED present** | Populated Hazards domain schema index; records schema-home conflict. |
| `schemas/contracts/v1/domains/hazards/receipts/README.md` | **CONFIRMED present** | Draft Hazards receipt schema index. |
| `schemas/contracts/v1/domains/hazards/*.schema.json` | **CONFIRMED surfaced by search** | Multiple schema files were found; each file's maturity still requires per-file verification. |

---

## Active domain-lane inventory

Current search surfaced these files under `schemas/contracts/v1/domains/hazards/`. This is a search-derived inventory, not a complete mounted-checkout manifest.

| Surfaced path | Role signal | Posture |
|---|---|---|
| `README.md` | Hazards domain schema index. | **CONFIRMED present** |
| `receipts/README.md` | Hazards receipts schema child index. | **CONFIRMED present / NEEDS VERIFICATION** |
| `source_descriptor.schema.json` | Hazards source descriptor shape. | **NEEDS VERIFICATION** |
| `run_receipt.schema.json` | Run/process receipt shape. | **NEEDS VERIFICATION** |
| `release_manifest.schema.json` | Release manifest shape. | **NEEDS VERIFICATION / release-adjacent** |
| `rollback_card.schema.json` | Rollback card shape. | **NEEDS VERIFICATION / release-adjacent** |
| `correction_notice.schema.json` | Correction notice shape. | **NEEDS VERIFICATION / release-adjacent** |
| `promotion_decision.schema.json` | Promotion decision shape. | **NEEDS VERIFICATION / release-governance boundary** |
| `decision_envelope.schema.json` | Decision envelope shape. | **NEEDS VERIFICATION / policy-runtime boundary** |
| `hazards_decision_envelope.schema.json` | Hazards-specific decision envelope. | **NEEDS VERIFICATION / possible profile or duplicate** |
| Support schemas | `catalog_matrix`, `layer_manifest`, `evidence_bundle`, `source_state_hash`, `domain_observation`, `domain_feature_identity`, `evidence_drawer_payload`, `domain_layer_descriptor`, `domain_validation_report`. | **NEEDS VERIFICATION** |

> [!CAUTION]
> The presence of files in the populated lane does not prove field completeness, accepted schema status, fixture coverage, validator wiring, policy behavior, release readiness, or public-facing readiness.

---

## Child receipt lane

The current populated Hazards receipt schema index is:

```text
schemas/contracts/v1/domains/hazards/receipts/README.md
```

This top-level README must not create a competing receipt sublane under `schemas/contracts/v1/hazards/receipts/` unless a reviewed migration plan says to do so.

---

## What belongs here

- This README.
- Alias, migration, mirror, deprecation, or schema-home conflict notes for `schemas/contracts/v1/hazards/`.
- Pointers to the accepted Hazards schema home once settled.
- Drift notes explaining why schema files should not be added directly here without review.

---

## What does not belong here

- Canonical Hazards JSON Schema files unless an accepted ADR/migration authorizes this path.
- Duplicate Hazards schemas already owned by `schemas/contracts/v1/domains/hazards/`.
- Semantic contract prose.
- Policy rules, sensitivity decisions, exposure decisions, or release decisions.
- Emitted receipt instances, proof outputs, lifecycle data, source registry records, catalog records, triplets, release records, correction notices, withdrawal notices, rollback cards, or public artifacts.
- Validator code, packages, pipelines, runtime code, UI/API implementation, map tiles, dashboards, screenshots, generated summaries, or operational instructions.
- Claims that a Hazards schema is complete or public-ready without fixtures, validators, registry records, policy review, and release support.

---

## Migration rules

Do not move or duplicate Hazards schemas into this top-level path unless a reviewed migration plan defines:

- source path;
- target path;
- owning root;
- reason for migration;
- schema `$id` changes;
- `$ref` and consumer updates;
- fixture and validator updates;
- schema registry updates;
- policy/freshness review;
- release and rollback impact;
- receipt-lane impact;
- deprecation/mirror window;
- tests proving no parallel authority remains.

---

## Validation

Recommended local validation sequence:

```bash
# Confirm this alias path remains README-only unless migration is authorized.
find schemas/contracts/v1/hazards -maxdepth 3 -type f | sort

# Inspect the populated Hazards domain schema lane.
find schemas/contracts/v1/domains/hazards -maxdepth 4 -type f | sort

# Detect duplicate Hazards schema authority across top-level and domain paths.
find schemas/contracts/v1 -maxdepth 6 -type f \
  | grep -Ei '/hazards/|/domains/hazards/' \
  | sort

# Validate JSON syntax for the populated domain lane.
find schemas/contracts/v1/domains/hazards -name '*.schema.json' -print0 \
  | xargs -0 -r -I{} python -m json.tool {} >/dev/null

# Run project validators when available.
python tools/validate_all.py || true
pytest tests/schemas tests/contract tests/domains/hazards tests/policy tests/release || true
```

Replace `|| true` with fail-closed CI behavior once validator and test paths are confirmed.

---

## Rollback

Rollback for this README is ordinary Git rollback: revert the commit that changed `schemas/contracts/v1/hazards/README.md`.

Rollback for any future migration into this path requires checking every downstream reference:

1. Revert or migrate schema files.
2. Restore canonical `$id` and `$ref` targets.
3. Restore paired contract links.
4. Restore fixtures, validators, schema registry records, and CI paths.
5. Restore policy, evidence, release, domain, and receipt references.
6. Restore Hazards API/UI/MapLibre/Evidence Drawer consumers.
7. Preserve correction and rollback records if any public Hazards surface was affected.

---

## Open questions

| Question | Status | Owner |
|---|---|---|
| Should `schemas/contracts/v1/hazards/` become the accepted Hazards schema home, or remain README-only? | **NEEDS VERIFICATION / ADR-sensitive** | Schema steward + Hazards steward |
| Should populated files under `schemas/contracts/v1/domains/hazards/` be migrated, mirrored, or left in place? | **NEEDS VERIFICATION / migration-sensitive** | Schema steward + Hazards steward |
| Should the receipt child lane remain under `domains/hazards/receipts/`? | **NEEDS VERIFICATION / ADR-sensitive** | Receipt steward + Hazards steward |
| Which Hazards schemas are field-complete and fixture-tested? | **NEEDS VERIFICATION** | Validation steward |
| Which Hazards schemas are safe for public API/MapLibre/Focus Mode use? | **NEEDS VERIFICATION / release-gated** | Release steward + Policy steward |

---

## Maintainer notes

- Keep this path README-only until the Hazards schema-home conflict is resolved.
- Do not let `schemas/contracts/v1/hazards/` and `schemas/contracts/v1/domains/hazards/` become parallel canonical homes.
- Preserve evidence, freshness, policy, release, correction, and rollback boundaries for all Hazards schema surfaces.
