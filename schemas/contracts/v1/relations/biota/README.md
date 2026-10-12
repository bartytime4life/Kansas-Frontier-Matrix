# `schemas/contracts/v1/relations/biota/` — Biota Relation Schema Guardrail

<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/schemas-contracts-v1-relations-biota-readme
title: schemas/contracts/v1/relations/biota/ — Biota Relation Schema Guardrail
type: readme; relation-schema-index; placement-guardrail; cross-domain-boundary
authority_class: relation-schema-guardrail
version: v0.1
status: draft; empty-relation-lane; exact-biota-schema-not-found; flora-fauna-habitat-nearest-lanes; aquatic-biota-child-relation-present; no-current-relation-schema-files-found; do-not-promote-without-ADR; NEEDS VERIFICATION before promotion
owners:
  - OWNER_TBD — Relation steward
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
policy_label: public; restricted-review-where-sensitive; schemas; contracts-v1; relations; biota; flora; fauna; habitat; evidence-bound; policy-aware; release-gated; rollback-aware; no-parallel-authority
tags: [kfm, schemas, contracts, v1, relations, biota, flora, fauna, habitat, biodiversity, taxon, occurrence, habitat-context, aquatic-biota, cross-domain, relation-lane, no-parallel-authority]
related:
  - ../../README.md
  - ../README.md
  - ../aquatic_biota/README.md
  - ../../domains/README.md
  - ../../domains/flora/README.md
  - ../../domains/fauna/README.md
  - ../../domains/habitat/README.md
  - ../../domains/habitat/land_cover/README.md
  - ../../domains/habitat/ecoregions/README.md
  - ../../../joins/README.md
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
  - "Expanded from an empty file at schemas/contracts/v1/relations/biota/README.md."
  - "Current GitHub search did not surface schema files directly under this relation lane beyond this README."
  - "Current GitHub search did not surface exact biota relation schema evidence in this check."
  - "Flora, Fauna, Habitat, and the aquatic_biota relation README were inspected or reused as nearest verified lanes."
  - "This README is a relation-placement guardrail only; do not create canonical biota relation schemas here without ADR, paired contracts, fixtures, validators, and steward review."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

![status](https://img.shields.io/badge/status-draft-yellow)
![root](https://img.shields.io/badge/root-schemas%2F-blue)
![family](https://img.shields.io/badge/family-relations-purple)
![relation](https://img.shields.io/badge/relation-biota-green)
![posture](https://img.shields.io/badge/posture-guardrail-orange)
![truth](https://img.shields.io/badge/truth-cite--or--abstain-success)

> **Purpose.** `schemas/contracts/v1/relations/biota/` is a README-only guardrail for possible machine-checkable Biota relation shapes.
>
> **One-line boundary.** This path may describe relationship shape only. It must not replace Flora, Fauna, Habitat, Evidence, Policy, Release, or emitted data roots.

---

## Quick jumps

[Status](#status) · [Placement decision](#placement-decision) · [Repo fit](#repo-fit) · [Current inventory](#current-inventory) · [Related surfaced lanes](#related-surfaced-lanes) · [Candidate relation shapes](#candidate-relation-shapes) · [What belongs here](#what-belongs-here) · [What does not belong here](#what-does-not-belong-here) · [Relation guardrails](#relation-guardrails) · [Migration rules](#migration-rules) · [Validation](#validation) · [Rollback](#rollback) · [Open questions](#open-questions)

---

## Status

| Question | Answer | Truth label |
|---|---|---|
| Does this README path exist? | Yes: `schemas/contracts/v1/relations/biota/README.md`. It was empty before this expansion. | **CONFIRMED** |
| Are schema files currently present directly under this relation lane? | Not found in the current GitHub search beyond this README. | **NEEDS VERIFICATION / search-limited** |
| Did current search confirm an exact Biota relation schema surface? | No exact Biota relation schema surface was found in this check. | **NEEDS VERIFICATION** |
| What are the nearest verified domain lanes? | Flora, Fauna, and Habitat schema READMEs were inspected or reused as nearest lanes. | **CONFIRMED path evidence** |
| Is there a related child relation lane? | Yes. `relations/aquatic_biota/README.md` is present as a README-only guardrail. | **CONFIRMED** |
| Is this relation lane canonical? | Not proven. Treat this path as README-only until ADR or steward decision. | **NEEDS VERIFICATION / ADR-sensitive** |
| Can this path store occurrence data, habitat data, receipts, proofs, release records, or public artifacts? | No. This is schema documentation only, not lifecycle data, proof storage, release storage, or publication surface. | **CONFIRMED boundary** |

> [!IMPORTANT]
> Biota relation schemas should connect references across domain-owned objects. They should not copy domain-owned fields, publish observations, or convert a relationship candidate into evidence-backed truth.

---

## Placement decision

Current placement posture:

```text
Requested relation guardrail:
  schemas/contracts/v1/relations/biota/

Related child relation guardrail:
  schemas/contracts/v1/relations/aquatic_biota/

Nearest inspected domain schema lanes:
  schemas/contracts/v1/domains/flora/
  schemas/contracts/v1/domains/fauna/
  schemas/contracts/v1/domains/habitat/
```

Rationale:

- Domain schemas normally belong under `schemas/contracts/v1/domains/<domain>/...` unless an accepted exception says otherwise.
- Flora owns plant taxon, occurrence, vegetation, range, restoration, and sensitivity-aware plant object shapes where accepted.
- Fauna owns animal taxon, occurrence, range, monitoring, and sensitivity-aware animal object shapes where accepted.
- Habitat owns land-cover, ecoregion, habitat patch, suitability, and corridor object shapes where accepted.
- `aquatic_biota/` is a narrower relation guardrail for water-linked biota relation shapes; this `biota/` path is broader and must not silently override it.
- Any future schema here must be paired with contracts, fixtures, validators, registry entries, sensitivity/policy review, release review, and steward review across affected domains.

---

## Repo fit

```text
schemas/
└── contracts/
    └── v1/
        ├── README.md
        ├── relations/
        │   ├── biota/
        │   │   └── README.md                     # this file; relation guardrail only
        │   └── aquatic_biota/
        │       └── README.md                     # narrower relation guardrail
        ├── joins/
        │   └── README.md                         # cross-domain join-family index
        └── domains/
            ├── flora/
            │   └── README.md                     # inspected Flora domain schema lane
            ├── fauna/
            │   └── README.md                     # inspected Fauna domain schema lane
            └── habitat/
                ├── README.md                     # inspected Habitat domain schema lane
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
| `schemas/contracts/v1/relations/biota/README.md` | **CONFIRMED present** | Empty file expanded by this README. |
| `schemas/contracts/v1/relations/biota/*.schema.json` | **Not found in current search** | Do not create here without ADR, paired contracts, and validation plan. |
| `schemas/contracts/v1/relations/aquatic_biota/README.md` | **CONFIRMED inspected** | Narrower aquatic-biota relation guardrail; not a schema and not canonical relation authority. |
| `schemas/contracts/v1/relations/README.md` | **NEEDS VERIFICATION** | Parent relations README was not confirmed in this edit. |
| `schemas/contracts/v1/domains/flora/README.md` | **CONFIRMED inspected** | Flora domain schema lane; sensitivity posture is fail-closed where sensitive. |
| `schemas/contracts/v1/domains/fauna/README.md` | **CONFIRMED reused from recent evidence** | Fauna domain schema lane; sensitivity posture is fail-closed where sensitive. |
| `schemas/contracts/v1/domains/habitat/README.md` | **CONFIRMED reused from recent evidence** | Habitat domain schema lane with land-cover and ecoregions child lanes. |

---

## Related surfaced lanes

| Path | Role signal | Posture |
|---|---|---|
| `schemas/contracts/v1/domains/flora/` | Flora-owned machine shape lane. | **PROPOSED / sensitivity-aware** |
| `schemas/contracts/v1/domains/fauna/` | Fauna-owned machine shape lane. | **PROPOSED / sensitivity-aware** |
| `schemas/contracts/v1/domains/habitat/` | Habitat-owned machine shape lane. | **PROPOSED / child lanes present** |
| `schemas/contracts/v1/relations/aquatic_biota/` | Narrower water-linked biota relation guardrail. | **README-only guardrail** |
| `schemas/contracts/v1/joins/` | Cross-domain join schema family. | **DRAFT / mixed schema and guardrail lanes** |
| `schemas/contracts/v1/relations/biota/` | Possible neutral biota relation schema lane. | **README-only guardrail** |

---

## Candidate relation shapes

Candidate schemas below require steward review, paired contracts, fixtures, validators, registry records, and sensitivity/policy/release review before promotion.

| Candidate schema | Purpose | Default posture |
|---|---|---|
| `biota_relation.schema.json` | Generic relationship envelope between biotic references and context references. | **PROPOSED / not created** |
| `flora_fauna_context.schema.json` | Relation between plant and animal references where evidence supports an association. | **PROPOSED / evidence-bound** |
| `biota_habitat_context.schema.json` | Relation between biotic references and habitat/land-cover/ecoregion context references. | **PROPOSED / sensitivity-aware** |
| `taxon_habitat_association.schema.json` | Relation between taxon references and habitat association references. | **PROPOSED / domain-boundary-sensitive** |
| `biota_release_projection.schema.json` | Public/release projection for already-governed biota relation outputs. | **PROPOSED / release-gated** |

> [!CAUTION]
> Candidate names are proposals only. Do not treat them as repo files, accepted contracts, implementation proof, or public-safe outputs until created, paired, fixture-tested, and reviewed.

---

## What belongs here

- This README.
- Relation schema placement notes for biota relationship objects.
- Future neutral relation schema files if an accepted ADR or migration plan authorizes this lane.
- Links to paired contracts, fixtures, validators, schema registry records, policy references, evidence references, release references, correction references, rollback references, and tests.
- Drift notes preventing duplicate Flora, Fauna, Habitat, aquatic-biota, join, or relation schema authority.

---

## What does not belong here

- Flora-owned canonical schemas.
- Fauna-owned canonical schemas.
- Habitat-owned canonical schemas.
- Semantic contract prose beyond README boundary notes.
- Policy rules, sensitivity decisions, exposure decisions, release decisions, or public map/API behavior.
- Lifecycle data, occurrence records, habitat records, source records, catalog records, triplets, receipt instances, proof outputs, release records, correction notices, rollback cards, public artifacts, dashboards, screenshots, or generated summaries.
- Validator code, packages, pipelines, runtime code, UI/API implementation, or map tiles.
- Claims that a biota relation is valid, complete, current, evidence-backed, policy-safe, release-approved, or public-ready merely because it validates against a schema.

---

## Relation guardrails

| Boundary | Requirement |
|---|---|
| Domain ownership | Flora, Fauna, and Habitat keep their own canonical shapes and semantic contracts. |
| Relation neutrality | A relation schema records relationship shape, not source truth for either side. |
| Reference discipline | Use stable references to domain-owned objects rather than duplicating domain fields. |
| Evidence dependency | Relation outputs need EvidenceBundle or equivalent support where claims depend on evidence. |
| Time discipline | Observational or condition-dependent relations should preserve observation, retrieval, release, and correction time where applicable. |
| Sensitivity posture | Sensitive ecological, exact-location, steward-controlled, or private-land-related surfaces require fail-closed review. |
| Release dependency | Public relation projections must be release-gated and rollback-aware. |
| Child-lane discipline | `aquatic_biota/` is a narrower guardrail; this broader lane must not override it without migration review. |
| No parallel authority | Do not maintain equivalent biota relation schemas under `relations/`, `joins/`, and domain lanes without a mirror/migration rule. |

---

## Migration rules

Do not move or duplicate biota relation schemas into this path unless a reviewed migration plan defines:

- source path;
- target path;
- owning root;
- reason for migration;
- chosen meaning of `biota`;
- relationship between `biota/` and `aquatic_biota/`;
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
find schemas/contracts/v1/relations/biota -maxdepth 2 -type f | sort

# Inspect nearby relation/join/domain schema lanes.
find schemas/contracts/v1/relations schemas/contracts/v1/joins schemas/contracts/v1/domains/flora schemas/contracts/v1/domains/fauna schemas/contracts/v1/domains/habitat -maxdepth 5 -type f 2>/dev/null \
  | grep -Ei 'biota|aquatic|flora|fauna|habitat|taxon|occurrence|README' \
  | sort

# Detect duplicate biota relation authority.
find schemas/contracts/v1 -maxdepth 7 -type f \
  | grep -Ei 'biota|flora.*fauna|fauna.*flora|habitat.*flora|flora.*habitat|habitat.*fauna|fauna.*habitat' \
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

Rollback for this README is ordinary Git rollback: revert the commit that changed `schemas/contracts/v1/relations/biota/README.md`.

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
| Should biota relationship shapes live under `relations/`, `joins/`, Flora, Fauna, Habitat, or another accepted lane? | **NEEDS VERIFICATION / ADR-sensitive** | Relation steward + domain stewards |
| Should `biota/` be a parent relation lane for `aquatic_biota/`, or should both remain independent guardrails? | **NEEDS VERIFICATION / hierarchy-sensitive** | Schema steward + Relation steward |
| Which semantic contract owns neutral biota relation meaning? | **NEEDS VERIFICATION** | Contract steward |
| Which fixtures prove that relations reference domain-owned objects without duplicating fields? | **NEEDS VERIFICATION** | Validation steward |
| Which biota relation projections are safe for public API/MapLibre/Focus Mode use? | **NEEDS VERIFICATION / release-gated** | Release steward + Policy steward |

---

## Maintainer notes

- Keep this path README-only until relation-home placement is resolved.
- Prefer references to domain-owned Flora, Fauna, and Habitat objects over copied fields.
- Do not let this relation lane duplicate `aquatic_biota/`, `joins/`, or domain schema authority.
- Preserve evidence, sensitivity, domain ownership, policy, release, correction, and rollback boundaries for every biota relation surface.
