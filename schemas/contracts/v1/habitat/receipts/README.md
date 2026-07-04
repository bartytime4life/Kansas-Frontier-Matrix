# `schemas/contracts/v1/habitat/receipts/` — Habitat Receipts Schema Guardrail

<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/schemas-contracts-v1-habitat-receipts-readme
title: schemas/contracts/v1/habitat/receipts/ — Habitat Receipts Schema Guardrail
type: readme; receipt-schema-index; alias-guardrail; habitat-domain-boundary
authority_class: schema-sublane-guardrail
version: v0.1
status: draft; empty-receipt-sublane; domain-home-elsewhere; no-current-schema-files-found; receipt-home-sensitive; do-not-promote-without-ADR; NEEDS VERIFICATION before promotion
owners:
  - OWNER_TBD — Habitat domain steward
  - OWNER_TBD — Receipt steward
  - OWNER_TBD — Schema steward
  - OWNER_TBD — Contract steward
  - OWNER_TBD — Policy steward
  - OWNER_TBD — Release steward
  - OWNER_TBD — Validation steward
  - OWNER_TBD — Docs steward
created: NEEDS VERIFICATION — empty README existed before v0.1 expansion
updated: 2026-07-04
policy_label: public; schemas; contracts-v1; habitat; receipts; geoprivacy; transform-receipt; model-run-receipt; run-receipt; release-gated; rollback-aware; no-parallel-authority
tags: [kfm, schemas, contracts, v1, habitat, receipts, geoprivacy-transform-receipt, model-run-receipt, run-receipt, redaction, generalization, release, rollback, evidence, policy, no-parallel-authority]
related:
  - ../../README.md
  - ../README.md
  - ../../domains/habitat/README.md
  - ../../domains/habitat/geoprivacy_transform_receipt.schema.json
  - ../../domains/habitat/model_run_receipt.schema.json
  - ../../domains/habitat/run_receipt.schema.json
  - ../../domains/habitat/release_manifest.schema.json
  - ../../domains/habitat/rollback_card.schema.json
  - ../../domains/habitat/correction_notice.schema.json
  - ../../domains/habitat/promotion_decision.schema.json
  - ../../domains/habitat/decision_envelope.schema.json
  - ../../../../docs/domains/habitat/README.md
  - ../../../../contracts/domains/habitat/
  - ../../../../policy/domains/habitat/
  - ../../../../fixtures/domains/habitat/
  - ../../../../tests/domains/habitat/
  - ../../../../release/candidates/habitat/
notes:
  - "Expanded from an empty file at schemas/contracts/v1/habitat/receipts/README.md."
  - "GitHub search did not surface existing schema files under schemas/contracts/v1/habitat/receipts/ beyond this README in the current check."
  - "Active Habitat schema work is under schemas/contracts/v1/domains/habitat/, including release, rollback, correction, run, model-run, promotion, decision, and geoprivacy transform receipt-like schemas surfaced by search."
  - "Opened geoprivacy_transform_receipt.schema.json is a permissive PROPOSED scaffold with empty properties and additionalProperties true."
  - "This file is a guardrail only; it must not become a parallel Habitat receipt schema home without ADR, migration note, or receipt-home decision."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

![status](https://img.shields.io/badge/status-draft-yellow)
![root](https://img.shields.io/badge/root-schemas%2F-blue)
![domain](https://img.shields.io/badge/domain-habitat-green)
![lane](https://img.shields.io/badge/lane-receipts-purple)
![posture](https://img.shields.io/badge/posture-guardrail-orange)
![canonical](https://img.shields.io/badge/canonical-domain__lane__elsewhere-critical)
![truth](https://img.shields.io/badge/truth-cite--or--abstain-success)

> **Purpose.** `schemas/contracts/v1/habitat/receipts/` is an empty guardrail README for Habitat receipt-schema placement.
>
> **One-line boundary.** Active Habitat schema work is under `schemas/contracts/v1/domains/habitat/`. Do not add canonical Habitat receipt schemas directly under `schemas/contracts/v1/habitat/receipts/` unless an accepted ADR, migration note, or receipt-home decision authorizes this path.

---

## Quick jumps

[Status](#status) · [Placement decision](#placement-decision) · [Repo fit](#repo-fit) · [Current inventory](#current-inventory) · [Surfaced receipt-like schemas](#surfaced-receipt-like-schemas) · [What belongs here](#what-belongs-here) · [What does not belong here](#what-does-not-belong-here) · [Receipt guardrails](#receipt-guardrails) · [Migration rules](#migration-rules) · [Validation](#validation) · [Rollback](#rollback) · [Open questions](#open-questions)

---

## Status

| Question | Answer | Truth label |
|---|---|---|
| Does this README path exist? | Yes: `schemas/contracts/v1/habitat/receipts/README.md`. It was empty before this expansion. | **CONFIRMED** |
| Are schema files currently present under `schemas/contracts/v1/habitat/receipts/`? | Not found in the current GitHub search beyond this README. | **NEEDS VERIFICATION / search-limited** |
| Where is current Habitat schema activity? | `schemas/contracts/v1/domains/habitat/` surfaced a README, child schema indexes, and many schema files. | **CONFIRMED path evidence** |
| Are Habitat receipt-like schemas already elsewhere? | Yes. Search surfaced `run_receipt`, `model_run_receipt`, and `geoprivacy_transform_receipt` under the domain lane. | **CONFIRMED path evidence** |
| Is this top-level receipt sublane canonical? | Not proven. Treat as guardrail only. | **NEEDS VERIFICATION / do-not-promote-without-ADR** |
| Can this path store emitted receipt instances? | No. Schemas may define shape; emitted receipts belong in lifecycle/proof/receipt artifact lanes, not this README path. | **CONFIRMED boundary** |

> [!IMPORTANT]
> A receipt schema is not a receipt instance, proof, policy approval, release approval, correction notice, rollback card, or public-safe artifact. It only defines the machine-checkable shape of a receipt-like object if the path is accepted.

---

## Placement decision

Current placement posture:

```text
Preferred / active Habitat domain schema lane:
  schemas/contracts/v1/domains/habitat/

Do-not-use-as-canonical without ADR or receipt-home decision:
  schemas/contracts/v1/habitat/receipts/
```

Rationale:

- Current Habitat schema index identifies `schemas/contracts/v1/domains/habitat/` as the draft Habitat domain schema lane.
- Current search surfaced many Habitat schemas under the domain lane and none under this top-level receipt sublane.
- The Habitat domain lane already contains receipt-like schema names, including `run_receipt`, `model_run_receipt`, and `geoprivacy_transform_receipt`.
- Maintaining both locations as independent receipt homes would create `$id`, validator, fixture, release, and rollback drift.

---

## Repo fit

```text
schemas/
└── contracts/
    └── v1/
        ├── README.md
        ├── habitat/
        │   └── receipts/
        │       └── README.md                         # this file; guardrail only
        └── domains/
            └── habitat/
                ├── README.md                         # active Habitat domain schema index
                ├── run_receipt.schema.json           # receipt-like schema surfaced by search
                ├── model_run_receipt.schema.json     # receipt-like schema surfaced by search
                ├── geoprivacy_transform_receipt.schema.json
                ├── release_manifest.schema.json
                ├── rollback_card.schema.json
                ├── correction_notice.schema.json
                └── promotion_decision.schema.json

contracts/
└── domains/
    └── habitat/                                      # semantic meaning; not machine shape

policy/
└── domains/habitat/                                  # admissibility/policy posture; not schema shape

fixtures/
└── domains/habitat/                                  # examples; coverage NEEDS VERIFICATION

tests/
└── domains/habitat/                                  # behavioral proof; coverage NEEDS VERIFICATION

release/
└── candidates/habitat/                               # promotion/release/correction/rollback surfaces
```

---

## Current inventory

Current check:

| Path | Status | Note |
|---|---|---|
| `schemas/contracts/v1/habitat/receipts/README.md` | **CONFIRMED present** | Empty file expanded by this README. |
| `schemas/contracts/v1/habitat/receipts/*.schema.json` | **Not found in current search** | Do not create here without ADR, migration note, or receipt-home decision. |
| `schemas/contracts/v1/domains/habitat/README.md` | **CONFIRMED present** | Active Habitat domain schema index. |
| `schemas/contracts/v1/domains/habitat/*.schema.json` | **CONFIRMED surfaced by search** | Many schema files were found; each file's maturity still requires per-file verification. |
| `schemas/contracts/v1/domains/habitat/geoprivacy_transform_receipt.schema.json` | **CONFIRMED opened** | PROPOSED permissive scaffold; empty properties; `additionalProperties: true`. |

---

## Surfaced receipt-like schemas

Current search surfaced these Habitat receipt/release-governance-adjacent schema names under `schemas/contracts/v1/domains/habitat/`. This is a search-derived inventory, not a complete mounted-checkout manifest.

| Surfaced path | Role signal | Posture |
|---|---|---|
| `run_receipt.schema.json` | Run/process receipt shape. | **NEEDS VERIFICATION** |
| `model_run_receipt.schema.json` | Model/suitability run receipt shape. | **NEEDS VERIFICATION** |
| `geoprivacy_transform_receipt.schema.json` | Geoprivacy transform receipt shape; opened file is a permissive PROPOSED scaffold. | **PROPOSED scaffold / receipt-home-sensitive** |
| `release_manifest.schema.json` | Release manifest shape. | **NEEDS VERIFICATION / release authority elsewhere** |
| `rollback_card.schema.json` | Rollback card shape. | **NEEDS VERIFICATION / release authority elsewhere** |
| `correction_notice.schema.json` | Correction notice shape. | **NEEDS VERIFICATION / release authority elsewhere** |
| `promotion_decision.schema.json` | Promotion decision shape. | **NEEDS VERIFICATION / release-governance boundary** |
| `decision_envelope.schema.json` | Decision envelope shape. | **NEEDS VERIFICATION / policy-runtime boundary** |
| `habitat_decision_envelope.schema.json` | Habitat-specific decision envelope shape. | **NEEDS VERIFICATION / possible profile or duplicate** |

> [!CAUTION]
> The presence of receipt-like schema names in the Habitat domain lane does not prove receipt-family placement is settled, fields are complete, fixtures exist, validators are wired, policy gates pass, or public release is approved.

---

## What belongs here

- This README.
- Alias, migration, mirror, deprecation, or receipt-home notes for `schemas/contracts/v1/habitat/receipts/` if needed.
- Pointers to the accepted Habitat receipt schema home.
- Drift notes explaining why receipt schemas should not be added directly here without review.

---

## What does not belong here

- Canonical Habitat receipt schemas unless an accepted ADR/migration authorizes this path.
- Habitat domain schemas that belong under `schemas/contracts/v1/domains/habitat/`.
- Semantic contract prose.
- Policy rules, sensitivity decisions, redaction decisions, exposure decisions, or release decisions.
- Emitted receipt instances, proof outputs, lifecycle data, source registry records, catalog records, triplets, release records, correction notices, withdrawal notices, rollback cards, or public artifacts.
- Validator code, packages, pipelines, runtime code, UI/API implementation, map tiles, dashboards, screenshots, or generated summaries.
- Claims that a habitat transform, model run, generalization, release, correction, or rollback occurred merely because an object validates against a schema.

---

## Receipt guardrails

Habitat receipt schemas must preserve these boundaries:

| Boundary | Rule |
|---|---|
| Schema vs instance | `.schema.json` files define shape; emitted receipt records live elsewhere. |
| Receipt vs proof | A receipt records an action or transform; it is not the full evidence or proof bundle. |
| Receipt vs policy | A receipt can reference policy decisions; it does not decide allow/deny/restrict/abstain by itself. |
| Receipt vs release | A receipt can support release review; it is not a release manifest, correction notice, or rollback card. |
| Geoprivacy transform | Transform receipts must preserve what was transformed, why, by which policy/review basis, and which public geometry or detail level is safe to expose. |
| Model-run receipt | Model/suitability receipts must preserve model version, inputs, assumptions, uncertainty, and limitations without becoming habitat truth. |
| Cross-domain sensitivity | Habitat receipts may touch fauna, flora, rare species, private land, hydrology, hazards, and restoration surfaces; do not expose sensitive joins. |

Default public posture:

```text
receipt schema validity -> not proof of receipt event
receipt event -> not release approval
sensitive habitat join -> deny, restrict, generalize, aggregate, delay, or quarantine
public-safe display -> released projection with evidence, policy, correction, and rollback support
```

---

## Migration rules

Do not move or duplicate Habitat receipt schemas into this path unless a reviewed migration plan defines:

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
# Confirm this guardrail path remains README-only unless migration is authorized.
find schemas/contracts/v1/habitat/receipts -maxdepth 2 -type f | sort

# Inspect active Habitat schema lane and receipt-like schemas.
find schemas/contracts/v1/domains/habitat -maxdepth 3 -type f \
  | grep -Ei 'receipt|release_manifest|rollback|correction|promotion|decision_envelope|README' \
  | sort

# Detect duplicate Habitat receipt schema authority.
find schemas/contracts/v1 -maxdepth 6 -type f \
  | grep -Ei '/habitat/.*/.*receipt|/domains/habitat/.*receipt|release_manifest|rollback_card|correction_notice|promotion_decision' \
  | sort

# Validate JSON syntax for active Habitat receipt-like schemas.
find schemas/contracts/v1/domains/habitat -name '*receipt*.schema.json' -print0 \
  | xargs -0 -r -I{} python -m json.tool {} >/dev/null

# Run project validators when available.
python tools/validate_all.py || true
pytest tests/schemas tests/contract tests/domains/habitat tests/policy tests/release || true
```

Replace `|| true` with fail-closed CI behavior once validator and test paths are confirmed.

---

## Rollback

Rollback for this README is ordinary Git rollback: revert the commit that changed `schemas/contracts/v1/habitat/receipts/README.md`.

Rollback for any future migration into this path requires more care:

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
| Should `schemas/contracts/v1/habitat/receipts/` remain README-only as a guardrail? | **PROPOSED** | Schema steward + Habitat steward + Receipt steward |
| Should Habitat receipt-like schemas remain under `schemas/contracts/v1/domains/habitat/` or move to a receipt sublane? | **NEEDS VERIFICATION / ADR-sensitive** | Habitat steward + schema steward |
| Should geoprivacy receipts be shared/common, domain-specific, or policy/evidence-adjacent? | **NEEDS VERIFICATION / ADR-sensitive** | Policy steward + Evidence steward + Habitat steward |
| Which Habitat receipt schemas are field-complete and fixture-tested? | **NEEDS VERIFICATION** | Validation steward |
| Which Habitat receipts are required for public layers, Focus Mode, Evidence Drawer, or release candidates? | **NEEDS VERIFICATION / release-gated** | Release steward + UI/API steward |

---

## Maintainer notes

- Keep this path as a guardrail unless a reviewed migration says otherwise.
- Keep active Habitat domain schemas under `schemas/contracts/v1/domains/habitat/` until receipt-home placement is settled.
- Do not let this path become a parallel receipt authority.
- Preserve evidence, policy, sensitivity, geoprivacy, release, correction, and rollback boundaries for all Habitat receipt surfaces.
