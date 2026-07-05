# `schemas/contracts/v1/relations/` — Relation Schema Family Index

<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/schemas-contracts-v1-relations-readme
title: schemas/contracts/v1/relations/ — Relation Schema Family Index
type: readme; schema-family-index; relation-schema-boundary; placement-guardrail
authority_class: schema-family-guardrail
version: v0.1
status: draft; relation-family-present; child-lanes-readme-only; no-current-parent-schema-files-found; joins-overlap-present; domain-lanes-retain-authority; do-not-promote-without-ADR; NEEDS VERIFICATION before promotion
owners:
  - OWNER_TBD — Relation steward
  - OWNER_TBD — Schema steward
  - OWNER_TBD — Contract steward
  - OWNER_TBD — Domain stewards for affected relation lanes
  - OWNER_TBD — Policy steward
  - OWNER_TBD — Release steward
  - OWNER_TBD — Validation steward
  - OWNER_TBD — Docs steward
created: NEEDS VERIFICATION — empty README existed before v0.1 expansion
updated: 2026-07-04
policy_label: public; restricted-review-where-sensitive; schemas; contracts-v1; relations; cross-domain; evidence-bound; release-gated; no-parallel-authority
tags: [kfm, schemas, contracts, v1, relations, cross-domain, biota, aquatic-biota, biota-hazards, habitat-fauna, pollinator, joins-overlap, relation-guardrail, no-parallel-authority]
related:
  - ../README.md
  - ./aquatic_biota/README.md
  - ./biota/README.md
  - ./biota_hazards/README.md
  - ./habitat_fauna/README.md
  - ./pollinator/README.md
  - ../joins/README.md
  - ../joins/habitat-fauna-join.schema.json
  - ../domains/README.md
  - ../domains/flora/README.md
  - ../domains/fauna/README.md
  - ../domains/habitat/README.md
  - ../domains/hazards/README.md
  - ../domains/hydrology/README.md
notes:
  - "Expanded from an empty file at schemas/contracts/v1/relations/README.md."
  - "Current GitHub search surfaced relation child README files, but no concrete .schema.json files directly under schemas/contracts/v1/relations/ in this check."
  - "Direct inspection confirmed README-only child relation guardrails for aquatic_biota, biota, biota_hazards, habitat_fauna, and pollinator."
  - "The existing joins family contains at least one related scaffold, schemas/contracts/v1/joins/habitat-fauna-join.schema.json, so relation-vs-join placement must stay visible."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

![status](https://img.shields.io/badge/status-draft-yellow)
![root](https://img.shields.io/badge/root-schemas%2F-blue)
![family](https://img.shields.io/badge/family-relations-purple)
![posture](https://img.shields.io/badge/posture-family__guardrail-orange)
![truth](https://img.shields.io/badge/truth-cite--or--abstain-success)

> **Purpose.** `schemas/contracts/v1/relations/` is the parent schema-family index for possible machine-checkable cross-domain relation shapes.
>
> **One-line boundary.** Relation schemas define relationship object shape only. They do not replace domain-owned schemas, evidence, policy, release decisions, emitted data roots, proof pipelines, joins, receipts, or public artifacts.

---

## Quick jumps

[Status](#status) · [Authority and placement](#authority-and-placement) · [Repo fit](#repo-fit) · [Current relation inventory](#current-relation-inventory) · [Relation vs join posture](#relation-vs-join-posture) · [What belongs here](#what-belongs-here) · [What does not belong here](#what-does-not-belong-here) · [Relation-family rules](#relation-family-rules) · [Promotion checklist](#promotion-checklist) · [Validation](#validation) · [Rollback](#rollback) · [Open questions](#open-questions)

---

## Status

| Question | Answer | Truth label |
|---|---|---|
| Does this README path exist? | Yes: `schemas/contracts/v1/relations/README.md`. It was empty before this expansion. | **CONFIRMED** |
| Are concrete schema files currently present directly under `schemas/contracts/v1/relations/`? | Not confirmed in the current search. Current inspected relation surfaces are README-only child guardrails. | **NEEDS VERIFICATION / search-limited** |
| Are child relation lanes present? | Yes. Direct inspection confirmed README-only child lanes for `aquatic_biota/`, `biota/`, `biota_hazards/`, `habitat_fauna/`, and `pollinator/`. | **CONFIRMED** |
| Are child relation lanes canonical schema homes? | Not proven. They all use guardrail posture and require ADR/steward review before schema promotion. | **CONFIRMED boundary** |
| Is there overlap with `joins/`? | Yes. `habitat_fauna/` points to an existing `joins/habitat-fauna-join.schema.json` scaffold. | **CONFIRMED overlap** |
| Can relation schemas prove a relationship claim? | No. Relation schemas constrain shape; evidence, policy, review, release, and domain-owned records still control claim support. | **CONFIRMED boundary** |

---

## Authority and placement

This folder is under the schema responsibility root:

```text
schemas/contracts/v1/relations/
```

It may host relation schema shapes only after the relation-vs-join-vs-domain placement question is settled for each object family. Adjacent authority remains separate:

- `schemas/contracts/v1/domains/<domain>/` owns domain-specific machine shape.
- `contracts/` owns semantic meaning.
- `schemas/contracts/v1/joins/` owns accepted join object shapes where confirmed.
- `data/` owns lifecycle data and emitted records according to each data root.
- `policy/` owns policy posture where implemented.
- `release/` owns release, correction, withdrawal, and rollback records.
- `pipelines/` owns executable orchestration and proof harnesses.
- `fixtures/` and `tests/` prove valid/invalid examples and validator behavior.

This README does not amend ADR-0001, Directory Rules, domain ownership, join ownership, policy docs, validators, or release gates.

---

## Repo fit

```text
schemas/
└── contracts/
    └── v1/
        ├── README.md
        ├── relations/
        │   ├── README.md                         # this file; family index / guardrail
        │   ├── aquatic_biota/
        │   │   └── README.md                     # README-only guardrail
        │   ├── biota/
        │   │   └── README.md                     # README-only guardrail
        │   ├── biota_hazards/
        │   │   └── README.md                     # README-only guardrail
        │   ├── habitat_fauna/
        │   │   └── README.md                     # README-only guardrail; join/proof overlap
        │   └── pollinator/
        │       └── README.md                     # README-only guardrail
        ├── joins/
        │   ├── README.md
        │   └── habitat-fauna-join.schema.json    # related PROPOSED scaffold
        └── domains/
            ├── flora/
            ├── fauna/
            ├── habitat/
            ├── hazards/
            └── hydrology/

contracts/
policy/
fixtures/
tests/
data/
release/
pipelines/
```

---

## Current relation inventory

| Child lane | Current status | Nearest lanes | Notes |
|---|---|---|---|
| `aquatic_biota/` | **README-only guardrail** | Hydrology, Fauna, Habitat | No exact aquatic-biota schema evidence confirmed in its edit. |
| `biota/` | **README-only guardrail** | Flora, Fauna, Habitat | Broader biota relation guardrail. |
| `biota_hazards/` | **README-only guardrail** | Biota, Hazards, Flora, Fauna, Habitat | Hazard-context relation guardrail; no direct schema files confirmed. |
| `habitat_fauna/` | **README-only guardrail** | Habitat, Fauna, Joins, proof pipeline | Related `joins/habitat-fauna-join.schema.json` scaffold and proof harness exist. |
| `pollinator/` | **README-only guardrail** | Biota, Flora, Fauna, Habitat | No exact pollinator relation schema evidence confirmed in its edit. |

---

## Relation vs join posture

Relation and join language overlap in the current repository. This README uses the following conservative posture:

| Surface | Role | Current posture |
|---|---|---|
| `schemas/contracts/v1/relations/` | Candidate relationship schema family. | **DRAFT / README-only parent guardrail** |
| `schemas/contracts/v1/relations/*/README.md` | Child-lane placement notes. | **README-only guardrails** |
| `schemas/contracts/v1/joins/README.md` | Join schema family index. | **Existing adjacent family** |
| `schemas/contracts/v1/joins/habitat-fauna-join.schema.json` | Existing join scaffold. | **PROPOSED / field-incomplete** |
| Domain schema lanes | Canonical domain object shape where accepted. | **Domain-owned / not replaced by relations** |

A relation schema file should not be added until maintainers decide whether the object is a relation, a join, a domain-owned context shape, a release projection, or a proof-harness output.

---

## What belongs here

- This README.
- README-only child-lane guardrails for relation schema placement.
- Future relation `.schema.json` files only after accepted placement, contract pairing, fixtures, validators, and steward review.
- Migration notes for relation-vs-join-vs-domain placement decisions.
- Links to paired contracts, fixtures, validators, schema registry records, domain references, policy references, evidence references, release references, correction references, rollback references, and tests.

---

## What does not belong here

- Domain-owned canonical schemas.
- Join schemas already owned by `schemas/contracts/v1/joins/` unless migrated by review.
- Semantic contract prose beyond README boundary notes.
- Lifecycle data, source records, catalog records, triplets, receipt instances, proof outputs, release records, correction notices, rollback cards, public artifacts, dashboards, screenshots, or generated summaries.
- Policy rules, release decisions, public map/API behavior, runtime behavior, validator code, packages, pipelines, proof-harness code, UI/API implementation, or map tiles.
- Claims that a relation is valid, complete, current, evidence-backed, policy-safe, release-approved, or public-ready merely because it validates against a schema.

---

## Relation-family rules

| Rule | Requirement |
|---|---|
| Shape is not truth | Schema validation constrains shape; it does not prove the relationship claim. |
| Reference over copy | Relation shapes should reference domain-owned objects rather than copying domain fields. |
| Domain ownership remains | Domains keep canonical object shapes and semantic contracts. |
| Join overlap visible | Relation-vs-join placement must be explicit before schema-bearing promotion. |
| Evidence required | Relationship claims need EvidenceBundle or equivalent support where claims depend on evidence. |
| Release remains separate | Public relation projections must be release-gated and rollback-aware. |
| No parallel authority | Equivalent relation shapes must not drift across relations, joins, domains, pipelines, and release lanes without migration notes. |

---

## Promotion checklist

A relation schema should not advance beyond `PROPOSED` unless:

- [ ] Placement is resolved: `relations/`, `joins/`, domain lane, release projection, or proof pipeline output.
- [ ] Paired semantic contract exists.
- [ ] `$id` namespace convention is settled.
- [ ] Domain-owned referenced object families are identified.
- [ ] Required fields are defined.
- [ ] Evidence support is defined where claims depend on evidence.
- [ ] Policy review is complete where relation output requires it.
- [ ] Public-safe projection, if any, is release-gated.
- [ ] Valid fixtures exist.
- [ ] Invalid fixtures exist.
- [ ] Validators exist and paths are correct.
- [ ] CI/schema-test coverage exists.
- [ ] Migration notes exist for duplicate relation/join/domain surfaces.
- [ ] Correction and rollback references are defined where public use depends on the relation.

---

## Validation

Recommended local validation sequence:

```bash
# Inspect the relation schema family.
find schemas/contracts/v1/relations -maxdepth 4 -type f | sort

# Confirm relation child lanes are README-only unless authorized.
find schemas/contracts/v1/relations -maxdepth 4 -type f \
  | grep -Ev '/README\.md$' \
  | sort

# Inspect relation, join, and nearby domain schema surfaces.
find schemas/contracts/v1/relations schemas/contracts/v1/joins schemas/contracts/v1/domains -maxdepth 6 -type f 2>/dev/null \
  | grep -Ei 'relation|join|biota|pollinator|habitat|fauna|flora|hazard|hydro|README|schema\.json' \
  | sort

# Validate JSON syntax for relation/join/domain schemas when present.
find schemas/contracts/v1/relations schemas/contracts/v1/joins schemas/contracts/v1/domains -name '*.schema.json' -print0 2>/dev/null \
  | xargs -0 -r -I{} python -m json.tool {} >/dev/null

# Run project validators when available.
python tools/validate_all.py || true
pytest tests/schemas tests/contract tests/policy tests/release || true
```

Replace `|| true` with fail-closed CI behavior once validator and test paths are confirmed.

---

## Rollback

Rollback for this README is ordinary Git rollback: revert the commit that changed `schemas/contracts/v1/relations/README.md`.

Rollback for future relation schema changes requires checking every downstream reference:

1. Revert or migrate schema files.
2. Restore canonical `$id` and `$ref` targets.
3. Restore paired contract links.
4. Restore fixtures, validators, schema registry records, and CI paths.
5. Restore domain, policy, evidence, release, correction, receipt, proof, and join references.
6. Restore API/UI/MapLibre/Evidence Drawer consumers where applicable.
7. Preserve correction and rollback records if any public relation surface was affected.

---

## Open questions

| Question | Status | Owner |
|---|---|---|
| Should `relations/` become a schema-bearing family or remain README-only while `joins/` carries cross-domain schemas? | **NEEDS VERIFICATION / ADR-sensitive** | Relation steward + Schema steward |
| What is the formal difference between a relation schema, a join schema, a domain context shape, and a release projection? | **NEEDS VERIFICATION** | Contract steward + Schema steward |
| Which relation slugs are accepted and which are only experimental guardrails? | **NEEDS VERIFICATION / slug-sensitive** | Relation steward |
| Which fixtures prove relation schemas reference domain-owned objects without duplicating fields? | **NEEDS VERIFICATION** | Validation steward |
| Which relation projections are safe for public API/MapLibre/Focus Mode use? | **NEEDS VERIFICATION / release-gated** | Release steward + Policy steward |

---

## Maintainer notes

- Keep this parent README focused on relation schema-family boundaries.
- Prefer references to domain-owned objects over copied fields.
- Do not let `relations/` duplicate `joins/`, domain schema lanes, proof pipelines, or release projections.
- Preserve evidence, domain ownership, policy, release, correction, and rollback boundaries for every relation surface.
