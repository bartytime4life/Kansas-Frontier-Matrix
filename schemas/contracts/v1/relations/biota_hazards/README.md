# `schemas/contracts/v1/relations/biota_hazards/` — Biota Hazards Relation Schema Guardrail

<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/schemas-contracts-v1-relations-biota-hazards-readme
title: schemas/contracts/v1/relations/biota_hazards/ — Biota Hazards Relation Schema Guardrail
type: readme; relation-schema-index; placement-guardrail; cross-domain-boundary
authority_class: relation-schema-guardrail
version: v0.1
status: draft; empty-relation-lane; exact-biota-hazards-schema-not-found; biota-relation-guardrail-present; hazards-domain-lane-present; no-current-relation-schema-files-found; do-not-promote-without-ADR; NEEDS VERIFICATION before promotion
owners:
  - OWNER_TBD — Relation steward
  - OWNER_TBD — Biota relation steward
  - OWNER_TBD — Hazards domain steward
  - OWNER_TBD — Flora domain steward
  - OWNER_TBD — Fauna domain steward
  - OWNER_TBD — Habitat domain steward
  - OWNER_TBD — Schema steward
  - OWNER_TBD — Contract steward
  - OWNER_TBD — Freshness steward
  - OWNER_TBD — Sensitivity steward
  - OWNER_TBD — Policy steward
  - OWNER_TBD — Release steward
  - OWNER_TBD — Validation steward
  - OWNER_TBD — Docs steward
created: NEEDS VERIFICATION — empty README existed before v0.1 expansion
updated: 2026-07-04
policy_label: public; restricted-review-where-sensitive; schemas; contracts-v1; relations; biota-hazards; flora; fauna; habitat; hazards; freshness-aware; evidence-bound; policy-aware; release-gated; rollback-aware; no-life-safety-authority; no-parallel-authority
tags: [kfm, schemas, contracts, v1, relations, biota-hazards, biota, hazards, flora, fauna, habitat, exposure, vulnerability, hazard-context, cross-domain, relation-lane, freshness, no-life-safety-authority, no-parallel-authority]
related:
  - ../../README.md
  - ../README.md
  - ../biota/README.md
  - ../aquatic_biota/README.md
  - ../../domains/README.md
  - ../../domains/hazards/README.md
  - ../../domains/flora/README.md
  - ../../domains/fauna/README.md
  - ../../domains/habitat/README.md
  - ../../joins/README.md
  - ../../../../contracts/domains/hazards/
  - ../../../../contracts/domains/flora/
  - ../../../../contracts/domains/fauna/
  - ../../../../contracts/domains/habitat/
  - ../../../../docs/domains/hazards/
  - ../../../../docs/domains/flora/
  - ../../../../docs/domains/fauna/
  - ../../../../docs/domains/habitat/
  - ../../../../policy/domains/hazards/
  - ../../../../policy/domains/flora/
  - ../../../../policy/domains/fauna/
  - ../../../../policy/domains/habitat/
  - ../../../../fixtures/domains/hazards/
  - ../../../../fixtures/domains/flora/
  - ../../../../fixtures/domains/fauna/
  - ../../../../fixtures/domains/habitat/
  - ../../../../tests/domains/hazards/
  - ../../../../tests/domains/flora/
  - ../../../../tests/domains/fauna/
  - ../../../../tests/domains/habitat/
notes:
  - "Expanded from an empty file at schemas/contracts/v1/relations/biota_hazards/README.md."
  - "Current GitHub search did not surface schema files directly under this relation lane beyond this README."
  - "Current GitHub search did not surface exact biota_hazards relation schema evidence in this check."
  - "The Biota relation README and Hazards domain schema README were inspected or reused as nearest verified lanes."
  - "Hazards schema evidence states KFM Hazards is not an emergency alert system or life-safety authority. This relation lane inherits that boundary."
  - "This README is a relation-placement guardrail only; do not create canonical biota-hazards relation schemas here without ADR, paired contracts, fixtures, validators, freshness/policy/release review, and steward review."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

![status](https://img.shields.io/badge/status-draft-yellow)
![root](https://img.shields.io/badge/root-schemas%2F-blue)
![family](https://img.shields.io/badge/family-relations-purple)
![relation](https://img.shields.io/badge/relation-biota__hazards-red)
![posture](https://img.shields.io/badge/posture-guardrail-orange)
![boundary](https://img.shields.io/badge/boundary-not__life--safety__authority-critical)
![truth](https://img.shields.io/badge/truth-cite--or--abstain-success)

> **Purpose.** `schemas/contracts/v1/relations/biota_hazards/` is a README-only guardrail for possible machine-checkable relation shapes between biotic references and hazard-context references.
>
> **One-line boundary.** This path may describe relationship shape only. It must not replace Biota, Flora, Fauna, Habitat, Hazards, Evidence, Policy, Release, or emitted data roots, and it is not an emergency-alert or life-safety authority.

---

## Quick jumps

[Status](#status) · [Placement decision](#placement-decision) · [Repo fit](#repo-fit) · [Current inventory](#current-inventory) · [Related surfaced lanes](#related-surfaced-lanes) · [Candidate relation shapes](#candidate-relation-shapes) · [What belongs here](#what-belongs-here) · [What does not belong here](#what-does-not-belong-here) · [Relation guardrails](#relation-guardrails) · [Migration rules](#migration-rules) · [Validation](#validation) · [Rollback](#rollback) · [Open questions](#open-questions)

---

## Status

| Question | Answer | Truth label |
|---|---|---|
| Does this README path exist? | Yes: `schemas/contracts/v1/relations/biota_hazards/README.md`. It was empty before this expansion. | **CONFIRMED** |
| Are schema files currently present directly under this relation lane? | Not found in the current GitHub search beyond this README. | **NEEDS VERIFICATION / search-limited** |
| Did current search confirm an exact Biota Hazards relation schema surface? | No exact `biota_hazards` relation schema surface was found in this check. | **NEEDS VERIFICATION** |
| What are the nearest verified lanes? | `relations/biota/README.md` and `schemas/contracts/v1/domains/hazards/README.md` were inspected or reused as nearest lanes. | **CONFIRMED path evidence** |
| Is this relation lane canonical? | Not proven. Treat this path as README-only until ADR or steward decision. | **NEEDS VERIFICATION / ADR-sensitive** |
| Can this path store occurrence data, hazard event data, warning outputs, receipts, proofs, release records, public artifacts, or operational instructions? | No. This is schema documentation only, not lifecycle data, alerting, proof storage, release storage, or publication surface. | **CONFIRMED boundary** |

> [!IMPORTANT]
> Biota-hazards relation schemas should connect references across domain-owned objects. They should not copy domain-owned fields, publish observations, confirm hazards, issue warnings, or convert a relationship candidate into evidence-backed truth.

---

## Placement decision

Current placement posture:

```text
Requested relation guardrail:
  schemas/contracts/v1/relations/biota_hazards/

Related broader relation guardrail:
  schemas/contracts/v1/relations/biota/

Nearest inspected domain schema lanes:
  schemas/contracts/v1/domains/hazards/
  schemas/contracts/v1/domains/flora/
  schemas/contracts/v1/domains/fauna/
  schemas/contracts/v1/domains/habitat/
```

Rationale:

- Domain schemas normally belong under `schemas/contracts/v1/domains/<domain>/...` unless an accepted exception says otherwise.
- Hazards owns hazard context, warning context, event/context, freshness, and release-support object shapes where accepted, while remaining explicitly outside emergency-alert or life-safety authority.
- Flora, Fauna, and Habitat keep domain-owned biotic and habitat object shapes.
- `relations/biota/` is a broader README-only relation guardrail; this `biota_hazards/` lane is narrower and hazard-context specific.
- Any future schema here must be paired with contracts, fixtures, validators, registry entries, freshness semantics, sensitivity/policy review, release review, and steward review across affected domains.

---

## Repo fit

```text
schemas/
└── contracts/
    └── v1/
        ├── README.md
        ├── relations/
        │   ├── biota/
        │   │   └── README.md                     # broader relation guardrail
        │   ├── aquatic_biota/
        │   │   └── README.md                     # narrower water-linked relation guardrail
        │   └── biota_hazards/
        │       └── README.md                     # this file; relation guardrail only
        ├── joins/
        │   └── README.md                         # cross-domain join-family index
        └── domains/
            ├── hazards/
            │   └── README.md                     # inspected Hazards domain schema lane
            ├── flora/
            │   └── README.md                     # biota-adjacent domain schema lane
            ├── fauna/
            │   └── README.md                     # biota-adjacent domain schema lane
            └── habitat/
                └── README.md                     # biota-adjacent context lane

contracts/
├── domains/hazards/                               # semantic meaning; not machine shape
├── domains/flora/
├── domains/fauna/
└── domains/habitat/

policy/
fixtures/
tests/
data/
release/
```

---

## Current inventory

| Path | Status | Note |
|---|---|---|
| `schemas/contracts/v1/relations/biota_hazards/README.md` | **CONFIRMED present** | Empty file expanded by this README. |
| `schemas/contracts/v1/relations/biota_hazards/*.schema.json` | **Not found in current search** | Do not create here without ADR, paired contracts, and validation plan. |
| `schemas/contracts/v1/relations/biota/README.md` | **CONFIRMED inspected** | Broader Biota relation guardrail; not a schema and not canonical relation authority. |
| `schemas/contracts/v1/relations/aquatic_biota/README.md` | **CONFIRMED surfaced** | Narrower aquatic-biota relation guardrail. |
| `schemas/contracts/v1/domains/hazards/README.md` | **CONFIRMED inspected** | Hazards domain schema lane; canonical path remains conflict-visible and not life-safety authority. |
| `schemas/contracts/v1/domains/flora/README.md` | **CONFIRMED reused from recent evidence** | Flora domain schema lane; sensitivity posture is fail-closed where sensitive. |
| `schemas/contracts/v1/domains/fauna/README.md` | **CONFIRMED reused from recent evidence** | Fauna domain schema lane; sensitivity posture is fail-closed where sensitive. |
| `schemas/contracts/v1/domains/habitat/README.md` | **CONFIRMED reused from recent evidence** | Habitat domain schema lane with land-cover and ecoregions child lanes. |

---

## Related surfaced lanes

| Path | Role signal | Posture |
|---|---|---|
| `schemas/contracts/v1/relations/biota/` | Broader biota relation guardrail. | **README-only guardrail** |
| `schemas/contracts/v1/relations/aquatic_biota/` | Water-linked biota relation guardrail. | **README-only guardrail** |
| `schemas/contracts/v1/domains/hazards/` | Hazards-owned machine shape lane. | **PROPOSED / CONFLICTED / not life-safety authority** |
| `schemas/contracts/v1/domains/flora/` | Flora-owned machine shape lane. | **PROPOSED / sensitivity-aware** |
| `schemas/contracts/v1/domains/fauna/` | Fauna-owned machine shape lane. | **PROPOSED / sensitivity-aware** |
| `schemas/contracts/v1/domains/habitat/` | Habitat-owned machine shape lane. | **PROPOSED / child lanes present** |
| `schemas/contracts/v1/joins/` | Cross-domain join schema family. | **DRAFT / mixed schema and guardrail lanes** |
| `schemas/contracts/v1/relations/biota_hazards/` | Possible neutral biota-hazards relation schema lane. | **README-only guardrail** |

---

## Candidate relation shapes

Candidate schemas below require steward review, paired contracts, fixtures, validators, registry records, freshness semantics, and sensitivity/policy/release review before promotion.

| Candidate schema | Purpose | Default posture |
|---|---|---|
| `biota_hazard_relation.schema.json` | Generic relationship envelope between biotic references and hazard-context references. | **PROPOSED / not created** |
| `biota_exposure_context.schema.json` | Relation between biotic references and hazard exposure/context references. | **PROPOSED / evidence-bound** |
| `hazard_biota_impact_context.schema.json` | Relation describing an asserted hazard/biotic impact context using references only. | **PROPOSED / review-sensitive** |
| `biota_hazard_freshness_context.schema.json` | Relation with explicit freshness, observation, retrieval, release, and correction time support. | **PROPOSED / freshness-sensitive** |
| `biota_hazard_release_projection.schema.json` | Public/release projection for already-governed biota-hazards relation outputs. | **PROPOSED / release-gated** |

> [!CAUTION]
> Candidate names are proposals only. Do not treat them as repo files, accepted contracts, implementation proof, live warnings, or public-safe outputs until created, paired, fixture-tested, and reviewed.

---

## What belongs here

- This README.
- Relation schema placement notes for biota-hazards relationship objects.
- Future neutral relation schema files if an accepted ADR or migration plan authorizes this lane.
- Links to paired contracts, fixtures, validators, schema registry records, policy references, evidence references, release references, correction references, rollback references, and tests.
- Drift notes preventing duplicate Biota, Hazards, Flora, Fauna, Habitat, join, or relation schema authority.

---

## What does not belong here

- Hazards-owned canonical schemas.
- Flora-owned canonical schemas.
- Fauna-owned canonical schemas.
- Habitat-owned canonical schemas.
- Semantic contract prose beyond README boundary notes.
- Policy rules, sensitivity decisions, exposure decisions, release decisions, emergency instructions, live warning behavior, or public map/API behavior.
- Lifecycle data, occurrence records, hazard event records, warning records, source records, catalog records, triplets, receipt instances, proof outputs, release records, correction notices, rollback cards, public artifacts, dashboards, screenshots, or generated summaries.
- Validator code, packages, pipelines, runtime code, UI/API implementation, or map tiles.
- Claims that a biota-hazards relation is valid, complete, current, evidence-backed, policy-safe, release-approved, public-ready, or operationally actionable merely because it validates against a schema.

---

## Relation guardrails

| Boundary | Requirement |
|---|---|
| Domain ownership | Hazards, Flora, Fauna, and Habitat keep their own canonical shapes and semantic contracts. |
| Relation neutrality | A relation schema records relationship shape, not source truth for either side. |
| No life-safety authority | This lane must not issue emergency directions, warnings, or operational safety instructions. |
| Reference discipline | Use stable references to domain-owned objects rather than duplicating domain fields. |
| Evidence dependency | Relation outputs need EvidenceBundle or equivalent support where claims depend on evidence. |
| Freshness dependency | Hazard-related relation outputs need source time, observation time, retrieval time, release time, expiry/correction posture, or equivalent time support where applicable. |
| Sensitivity posture | Sensitive ecological, exact-location, steward-controlled, or private-land-related surfaces require fail-closed review. |
| Release dependency | Public relation projections must be release-gated and rollback-aware. |
| Broader-lane discipline | `biota/` is the broader guardrail; this lane must not override it without migration review. |
| No parallel authority | Do not maintain equivalent biota-hazards relation schemas under `relations/`, `joins/`, and domain lanes without a mirror/migration rule. |

---

## Migration rules

Do not move or duplicate biota-hazards relation schemas into this path unless a reviewed migration plan defines:

- source path;
- target path;
- owning root;
- reason for migration;
- chosen meaning of `biota_hazards`;
- relationship between `biota/`, `aquatic_biota/`, and `biota_hazards/`;
- schema `$id` changes;
- `$ref` and consumer updates;
- fixture and validator updates;
- schema registry updates;
- Hazards, Flora, Fauna, Habitat, freshness, policy, sensitivity, and release steward review;
- deprecation/mirror window;
- tests proving no parallel authority remains.

---

## Validation

Recommended local validation sequence:

```bash
# Confirm this relation lane remains README-only unless authorized.
find schemas/contracts/v1/relations/biota_hazards -maxdepth 2 -type f | sort

# Inspect nearby relation/join/domain schema lanes.
find schemas/contracts/v1/relations schemas/contracts/v1/joins schemas/contracts/v1/domains/hazards schemas/contracts/v1/domains/flora schemas/contracts/v1/domains/fauna schemas/contracts/v1/domains/habitat -maxdepth 5 -type f 2>/dev/null \
  | grep -Ei 'biota|hazard|flora|fauna|habitat|taxon|occurrence|exposure|freshness|README' \
  | sort

# Detect duplicate biota-hazards relation authority.
find schemas/contracts/v1 -maxdepth 7 -type f \
  | grep -Ei 'biota.*hazard|hazard.*biota|flora.*hazard|hazard.*flora|fauna.*hazard|hazard.*fauna|habitat.*hazard|hazard.*habitat' \
  | sort

# Validate JSON syntax for nearby domain schemas when present.
find schemas/contracts/v1/domains/hazards schemas/contracts/v1/domains/flora schemas/contracts/v1/domains/fauna schemas/contracts/v1/domains/habitat -name '*.schema.json' -print0 \
  | xargs -0 -r -I{} python -m json.tool {} >/dev/null

# Run project validators when available.
python tools/validate_all.py || true
pytest tests/schemas tests/contract tests/domains/hazards tests/domains/flora tests/domains/fauna tests/domains/habitat tests/policy tests/release || true
```

Replace `|| true` with fail-closed CI behavior once validator and test paths are confirmed.

---

## Rollback

Rollback for this README is ordinary Git rollback: revert the commit that changed `schemas/contracts/v1/relations/biota_hazards/README.md`.

Rollback for future relation schema changes requires checking every downstream reference:

1. Revert or migrate schema files.
2. Restore canonical `$id` and `$ref` targets.
3. Restore paired contract links.
4. Restore fixtures, validators, schema registry records, and CI paths.
5. Restore Hazards, Flora, Fauna, Habitat, freshness, policy, sensitivity, evidence, release, correction, and receipt references.
6. Restore API/UI/MapLibre/Evidence Drawer consumers.
7. Preserve correction and rollback records if any public relation surface was affected.

---

## Open questions

| Question | Status | Owner |
|---|---|---|
| Should biota-hazards relationship shapes live under `relations/`, `joins/`, Hazards, Flora/Fauna/Habitat, or another accepted lane? | **NEEDS VERIFICATION / ADR-sensitive** | Relation steward + domain stewards |
| Should `biota_hazards/` be a child/sibling of `biota/`, or should it remain an independent guardrail? | **NEEDS VERIFICATION / hierarchy-sensitive** | Schema steward + Relation steward |
| Which semantic contract owns neutral biota-hazards relation meaning? | **NEEDS VERIFICATION** | Contract steward |
| Which fixtures prove that relations reference domain-owned objects without duplicating fields? | **NEEDS VERIFICATION** | Validation steward |
| Which biota-hazards relation projections are safe for public API/MapLibre/Focus Mode use? | **NEEDS VERIFICATION / release-gated** | Release steward + Policy steward |

---

## Maintainer notes

- Keep this path README-only until relation-home placement is resolved.
- Prefer references to domain-owned Hazards, Flora, Fauna, and Habitat objects over copied fields.
- Do not let this relation lane duplicate `biota/`, `aquatic_biota/`, `joins/`, or domain schema authority.
- Preserve evidence, freshness, sensitivity, domain ownership, policy, release, correction, and rollback boundaries for every biota-hazards relation surface.
- Do not present this lane as emergency-alert, warning, operational, or life-safety authority.
