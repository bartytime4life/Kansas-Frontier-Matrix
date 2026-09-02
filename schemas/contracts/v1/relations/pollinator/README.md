# `schemas/contracts/v1/relations/pollinator/` — Pollinator Relation Schema Guardrail

<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/schemas-contracts-v1-relations-pollinator-readme
title: schemas/contracts/v1/relations/pollinator/ — Pollinator Relation Schema Guardrail
type: readme; relation-schema-index; placement-guardrail; cross-domain-boundary
authority_class: relation-schema-guardrail
version: v0.1
status: draft; empty-relation-lane; exact-pollinator-schema-not-found; flora-fauna-habitat-nearest-lanes; biota-relation-guardrail-present; no-current-relation-schema-files-found; do-not-promote-without-ADR; NEEDS VERIFICATION before promotion
owners:
  - OWNER_TBD — Relation steward
  - OWNER_TBD — Pollinator relation steward
  - OWNER_TBD — Flora domain steward
  - OWNER_TBD — Fauna domain steward
  - OWNER_TBD — Habitat domain steward
  - OWNER_TBD — Schema steward
  - OWNER_TBD — Contract steward
  - OWNER_TBD — Sensitivity steward
  - OWNER_TBD — Policy steward
  - OWNER_TBD — Release steward
  - OWNER_TBD — Validation steward
  - OWNER_TBD — Docs steward
created: NEEDS VERIFICATION — empty README existed before v0.1 expansion
updated: 2026-07-04
policy_label: public; restricted-review-where-sensitive; schemas; contracts-v1; relations; pollinator; flora; fauna; habitat; biota; evidence-bound; policy-aware; release-gated; rollback-aware; no-parallel-authority
tags: [kfm, schemas, contracts, v1, relations, pollinator, pollination, flora, fauna, habitat, biota, plant-pollinator, taxon, occurrence, habitat-context, cross-domain, relation-lane, no-parallel-authority]
related:
  - ../../README.md
  - ../README.md
  - ../biota/README.md
  - ../habitat_fauna/README.md
  - ../aquatic_biota/README.md
  - ../../joins/README.md
  - ../../domains/README.md
  - ../../domains/flora/README.md
  - ../../domains/fauna/README.md
  - ../../domains/habitat/README.md
  - ../../domains/habitat/land_cover/README.md
  - ../../domains/habitat/ecoregions/README.md
  - ../../../../contracts/domains/flora/
  - ../../../../contracts/domains/fauna/
  - ../../../../contracts/domains/habitat/
  - ../../../../docs/domains/flora/
  - ../../../../docs/domains/fauna/
  - ../../../../docs/domains/habitat/
  - ../../../../policy/domains/flora/
  - ../../../../policy/domains/fauna/
  - ../../../../policy/domains/habitat/
  - ../../../../fixtures/domains/flora/
  - ../../../../fixtures/domains/fauna/
  - ../../../../fixtures/domains/habitat/
  - ../../../../tests/domains/flora/
  - ../../../../tests/domains/fauna/
  - ../../../../tests/domains/habitat/
notes:
  - "Expanded from an empty file at schemas/contracts/v1/relations/pollinator/README.md."
  - "Current GitHub search did not surface schema files directly under this relation lane beyond this README."
  - "Current GitHub search did not surface exact pollinator relation schema evidence in this check."
  - "The Biota relation README was inspected as the nearest relation guardrail, and Flora, Fauna, and Habitat are the nearest domain schema lanes."
  - "This README is a relation-placement guardrail only; do not create canonical pollinator relation schemas here without ADR, paired contracts, fixtures, validators, sensitivity/policy/release review, and steward review."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

![status](https://img.shields.io/badge/status-draft-yellow)
![root](https://img.shields.io/badge/root-schemas%2F-blue)
![family](https://img.shields.io/badge/family-relations-purple)
![relation](https://img.shields.io/badge/relation-pollinator-goldenrod)
![posture](https://img.shields.io/badge/posture-guardrail-orange)
![truth](https://img.shields.io/badge/truth-cite--or--abstain-success)

> **Purpose.** `schemas/contracts/v1/relations/pollinator/` is a README-only guardrail for possible machine-checkable pollinator relation shapes.
>
> **One-line boundary.** This path may describe relationship shape only. It must not replace Flora, Fauna, Habitat, Evidence, Policy, Release, emitted data roots, or broader Biota relation governance.

---

## Quick jumps

[Status](#status) · [Placement decision](#placement-decision) · [Repo fit](#repo-fit) · [Current inventory](#current-inventory) · [Related surfaced lanes](#related-surfaced-lanes) · [Candidate relation shapes](#candidate-relation-shapes) · [What belongs here](#what-belongs-here) · [What does not belong here](#what-does-not-belong-here) · [Relation guardrails](#relation-guardrails) · [Migration rules](#migration-rules) · [Validation](#validation) · [Rollback](#rollback) · [Open questions](#open-questions)

---

## Status

| Question | Answer | Truth label |
|---|---|---|
| Does this README path exist? | Yes: `schemas/contracts/v1/relations/pollinator/README.md`. It was empty before this expansion. | **CONFIRMED** |
| Are schema files currently present directly under this relation lane? | Not found in the current GitHub search beyond this README. | **NEEDS VERIFICATION / search-limited** |
| Did current search confirm an exact Pollinator relation schema surface? | No exact pollinator relation schema surface was found in this check. | **NEEDS VERIFICATION** |
| What is the nearest verified relation lane? | `schemas/contracts/v1/relations/biota/README.md` was inspected as the broader relation guardrail. | **CONFIRMED path evidence** |
| What are the nearest domain lanes? | Flora, Fauna, and Habitat are the nearest domain schema lanes for plant, animal, and habitat context. | **CONFIRMED path evidence** |
| Is this relation lane canonical? | Not proven. Treat this path as README-only until ADR or steward decision. | **NEEDS VERIFICATION / ADR-sensitive** |
| Can this path store plant occurrence data, animal occurrence data, habitat data, pollinator observations, receipts, proofs, release records, or public artifacts? | No. This is schema documentation only, not lifecycle data, proof storage, release storage, or publication surface. | **CONFIRMED boundary** |

> [!IMPORTANT]
> Pollinator relation schemas should connect references across domain-owned objects. They should not copy domain-owned fields, publish observations, turn plant context into animal truth, or turn animal occurrence into plant truth.

---

## Placement decision

Current placement posture:

```text
Requested relation guardrail:
  schemas/contracts/v1/relations/pollinator/

Broader relation guardrail:
  schemas/contracts/v1/relations/biota/

Related relation guardrails:
  schemas/contracts/v1/relations/habitat_fauna/
  schemas/contracts/v1/relations/aquatic_biota/

Nearest inspected domain schema lanes:
  schemas/contracts/v1/domains/flora/
  schemas/contracts/v1/domains/fauna/
  schemas/contracts/v1/domains/habitat/
```

Rationale:

- Domain schemas normally belong under `schemas/contracts/v1/domains/<domain>/...` unless an accepted exception says otherwise.
- Flora owns plant taxon, plant occurrence, vegetation, rare/protected plant, invasive plant, restoration, and sensitivity-aware plant object shapes where accepted.
- Fauna owns animal taxon, occurrence, range, monitoring, sensitive-site, and sensitivity-aware animal object shapes where accepted.
- Habitat owns habitat context, land-cover, ecoregion, habitat patch, suitability, and corridor object shapes where accepted.
- `relations/biota/` is the broader README-only relation guardrail; this `pollinator/` lane is narrower and should not silently override it.
- Any future schema here must be paired with contracts, fixtures, validators, registry entries, sensitivity/policy review, release review, and steward review across affected domains.

---

## Repo fit

```text
schemas/
└── contracts/
    └── v1/
        ├── README.md
        ├── relations/
        │   ├── pollinator/
        │   │   └── README.md                     # this file; relation guardrail only
        │   ├── biota/
        │   │   └── README.md                     # broader relation guardrail
        │   ├── habitat_fauna/
        │   └── aquatic_biota/
        ├── joins/
        │   └── README.md                         # cross-domain join-family index
        └── domains/
            ├── flora/
            │   └── README.md                     # plant-related domain schema lane
            ├── fauna/
            │   └── README.md                     # animal-related domain schema lane
            └── habitat/
                ├── README.md                     # habitat context schema lane
                ├── land_cover/
                └── ecoregions/

contracts/
├── domains/flora/                                 # semantic meaning; not machine shape
├── domains/fauna/                                 # semantic meaning; not machine shape
└── domains/habitat/                               # semantic meaning; not machine shape

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
| `schemas/contracts/v1/relations/pollinator/README.md` | **CONFIRMED present** | Empty file expanded by this README. |
| `schemas/contracts/v1/relations/pollinator/*.schema.json` | **Not found in current search** | Do not create here without ADR, paired contracts, and validation plan. |
| `schemas/contracts/v1/relations/biota/README.md` | **CONFIRMED inspected** | Broader Biota relation guardrail; not a schema and not canonical relation authority. |
| `schemas/contracts/v1/relations/habitat_fauna/README.md` | **CONFIRMED surfaced** | Related Habitat × Fauna relation guardrail. |
| `schemas/contracts/v1/relations/aquatic_biota/README.md` | **CONFIRMED surfaced** | Related aquatic-biota relation guardrail. |
| `schemas/contracts/v1/domains/flora/README.md` | **CONFIRMED reused from recent evidence** | Flora domain schema lane; sensitivity posture is fail-closed where sensitive. |
| `schemas/contracts/v1/domains/fauna/README.md` | **CONFIRMED reused from recent evidence** | Fauna domain schema lane; sensitivity posture is fail-closed where sensitive. |
| `schemas/contracts/v1/domains/habitat/README.md` | **CONFIRMED reused from recent evidence** | Habitat domain schema lane with land-cover and ecoregions child lanes. |

---

## Related surfaced lanes

| Path | Role signal | Posture |
|---|---|---|
| `schemas/contracts/v1/relations/pollinator/` | Possible neutral pollinator relation schema lane. | **README-only guardrail** |
| `schemas/contracts/v1/relations/biota/` | Broader biota relation guardrail. | **README-only guardrail** |
| `schemas/contracts/v1/relations/habitat_fauna/` | Habitat × Fauna relation guardrail. | **README-only guardrail** |
| `schemas/contracts/v1/domains/flora/` | Flora-owned machine shape lane. | **PROPOSED / sensitivity-aware** |
| `schemas/contracts/v1/domains/fauna/` | Fauna-owned machine shape lane. | **PROPOSED / sensitivity-aware** |
| `schemas/contracts/v1/domains/habitat/` | Habitat-owned machine shape lane. | **PROPOSED / child lanes present** |
| `schemas/contracts/v1/joins/` | Cross-domain join schema family. | **DRAFT / mixed schema and guardrail lanes** |

---

## Candidate relation shapes

Candidate schemas below require steward review, paired contracts, fixtures, validators, registry records, and sensitivity/policy/release review before promotion.

| Candidate schema | Purpose | Default posture |
|---|---|---|
| `pollinator_relation.schema.json` | Generic relation envelope between plant, pollinator, and context references. | **PROPOSED / not created** |
| `plant_pollinator_context.schema.json` | Relation between plant taxon/occurrence refs and pollinator taxon/occurrence refs. | **PROPOSED / evidence-bound** |
| `pollinator_habitat_context.schema.json` | Relation between pollinator refs and habitat/land-cover/ecoregion context refs. | **PROPOSED / sensitivity-aware** |
| `phenology_pollinator_context.schema.json` | Relation between plant/pollinator timing context refs where supported by evidence. | **PROPOSED / time-sensitive** |
| `pollinator_release_projection.schema.json` | Public/release projection for already-governed pollinator relation outputs. | **PROPOSED / release-gated** |

> [!CAUTION]
> Candidate names are proposals only. Do not treat them as repo files, accepted contracts, implementation proof, or public-safe outputs until created, paired, fixture-tested, and reviewed.

---

## What belongs here

- This README.
- Relation schema placement notes for pollinator relationship objects.
- Future neutral relation schema files if an accepted ADR or migration plan authorizes this lane.
- Links to paired contracts, fixtures, validators, schema registry records, policy references, evidence references, release references, correction references, rollback references, and tests.
- Drift notes preventing duplicate Flora, Fauna, Habitat, Biota, join, or relation schema authority.

---

## What does not belong here

- Flora-owned canonical schemas.
- Fauna-owned canonical schemas.
- Habitat-owned canonical schemas.
- Semantic contract prose beyond README boundary notes.
- Policy rules, sensitivity decisions, exposure decisions, release decisions, or public map/API behavior.
- Lifecycle data, plant occurrence records, animal occurrence records, pollinator observation records, habitat records, source records, catalog records, triplets, receipt instances, proof outputs, release records, correction notices, rollback cards, public artifacts, dashboards, screenshots, or generated summaries.
- Validator code, packages, pipelines, runtime code, UI/API implementation, or map tiles.
- Claims that a pollinator relation is valid, complete, current, evidence-backed, policy-safe, release-approved, or public-ready merely because it validates against a schema.

---

## Relation guardrails

| Boundary | Requirement |
|---|---|
| Domain ownership | Flora, Fauna, and Habitat keep their own canonical shapes and semantic contracts. |
| Relation neutrality | A relation schema records relationship shape, not source truth for either side. |
| Broader-lane discipline | `biota/` is the broader guardrail; this lane must not override it without migration review. |
| Reference discipline | Use stable references to domain-owned objects rather than duplicating domain fields. |
| Evidence dependency | Relation outputs need EvidenceBundle or equivalent support where claims depend on evidence. |
| Time discipline | Phenology, observation, retrieval, release, and correction time should remain distinguishable where applicable. |
| Sensitivity posture | Sensitive ecological, exact-location, steward-controlled, rare-species, or private-land-related surfaces require fail-closed review. |
| Release dependency | Public relation projections must be release-gated and rollback-aware. |
| No parallel authority | Do not maintain equivalent pollinator relation schemas under `relations/`, `joins/`, and domain lanes without a mirror/migration rule. |

---

## Migration rules

Do not move or duplicate pollinator relation schemas into this path unless a reviewed migration plan defines:

- source path;
- target path;
- owning root;
- reason for migration;
- chosen meaning of `pollinator`;
- relationship between `pollinator/`, `biota/`, `habitat_fauna/`, and domain lanes;
- schema `$id` changes;
- `$ref` and consumer updates;
- fixture and validator updates;
- schema registry updates;
- Flora, Fauna, Habitat, policy, sensitivity, and release steward review;
- deprecation/mirror window;
- tests proving no parallel authority remains.

---

## Validation

Recommended local validation sequence:

```bash
# Confirm this relation lane remains README-only unless authorized.
find schemas/contracts/v1/relations/pollinator -maxdepth 2 -type f | sort

# Inspect nearby relation/join/domain schema lanes.
find schemas/contracts/v1/relations schemas/contracts/v1/joins schemas/contracts/v1/domains/flora schemas/contracts/v1/domains/fauna schemas/contracts/v1/domains/habitat -maxdepth 5 -type f 2>/dev/null \
  | grep -Ei 'pollinator|pollination|biota|flora|fauna|habitat|taxon|occurrence|phenology|README' \
  | sort

# Detect duplicate pollinator relation authority.
find schemas/contracts/v1 -maxdepth 7 -type f \
  | grep -Ei 'pollinator|pollination|plant.*pollinator|pollinator.*plant|flora.*fauna|fauna.*flora' \
  | sort

# Validate JSON syntax for nearby domain schemas when present.
find schemas/contracts/v1/domains/flora schemas/contracts/v1/domains/fauna schemas/contracts/v1/domains/habitat -name '*.schema.json' -print0 \
  | xargs -0 -r -I{} python -m json.tool {} >/dev/null

# Run project validators when available.
python tools/validate_all.py || true
pytest tests/schemas tests/contract tests/domains/flora tests/domains/fauna tests/domains/habitat tests/policy tests/release || true
```

Replace `|| true` with fail-closed CI behavior once validator and test paths are confirmed.

---

## Rollback

Rollback for this README is ordinary Git rollback: revert the commit that changed `schemas/contracts/v1/relations/pollinator/README.md`.

Rollback for future relation schema changes requires checking every downstream reference:

1. Revert or migrate schema files.
2. Restore canonical `$id` and `$ref` targets.
3. Restore paired contract links.
4. Restore fixtures, validators, schema registry records, and CI paths.
5. Restore Flora, Fauna, Habitat, policy, sensitivity, evidence, release, correction, and receipt references.
6. Restore API/UI/MapLibre/Evidence Drawer consumers.
7. Preserve correction and rollback records if any public relation surface was affected.

---

## Open questions

| Question | Status | Owner |
|---|---|---|
| Should pollinator relationship shapes live under `relations/`, `joins/`, Flora, Fauna, Habitat, or another accepted lane? | **NEEDS VERIFICATION / ADR-sensitive** | Relation steward + domain stewards |
| Should `pollinator/` be a child/sibling of `biota/`, or should it remain an independent guardrail? | **NEEDS VERIFICATION / hierarchy-sensitive** | Schema steward + Relation steward |
| Which semantic contract owns neutral pollinator relation meaning? | **NEEDS VERIFICATION** | Contract steward |
| Which fixtures prove that relations reference domain-owned objects without duplicating fields? | **NEEDS VERIFICATION** | Validation steward |
| Which pollinator relation projections are safe for public API/MapLibre/Focus Mode use? | **NEEDS VERIFICATION / release-gated** | Release steward + Policy steward |

---

## Maintainer notes

- Keep this path README-only until relation-home placement is resolved.
- Prefer references to domain-owned Flora, Fauna, and Habitat objects over copied fields.
- Do not let this relation lane duplicate `biota/`, `habitat_fauna/`, `joins/`, or domain schema authority.
- Preserve evidence, sensitivity, domain ownership, policy, release, correction, and rollback boundaries for every pollinator relation surface.
