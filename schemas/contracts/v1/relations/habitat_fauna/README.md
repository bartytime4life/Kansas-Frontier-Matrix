# `schemas/contracts/v1/relations/habitat_fauna/` — Habitat Fauna Relation Schema Guardrail

<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/schemas-contracts-v1-relations-habitat-fauna-readme
title: schemas/contracts/v1/relations/habitat_fauna/ — Habitat Fauna Relation Schema Guardrail
type: readme; relation-schema-index; placement-guardrail; cross-domain-boundary
authority_class: relation-schema-guardrail
version: v0.1
status: draft; empty-relation-lane; join-schema-scaffold-present; proof-pipeline-present; habitat-fauna-domain-lanes-present; no-current-relation-schema-files-found; do-not-promote-without-ADR; NEEDS VERIFICATION before promotion
owners:
  - OWNER_TBD — Relation steward
  - OWNER_TBD — Habitat domain steward
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
policy_label: public; restricted-review-where-sensitive; schemas; contracts-v1; relations; habitat-fauna; habitat; fauna; evidence-bound; policy-aware; release-gated; rollback-aware; no-parallel-authority
tags: [kfm, schemas, contracts, v1, relations, habitat-fauna, habitat, fauna, occurrence, habitat-context, suitability, corridor, cross-domain, join-overlap, proof-pipeline-overlap, relation-lane, no-parallel-authority]
related:
  - ../../README.md
  - ../README.md
  - ../biota/README.md
  - ../aquatic_biota/README.md
  - ../../joins/README.md
  - ../../joins/habitat-fauna-join.schema.json
  - ../../domains/README.md
  - ../../domains/habitat/README.md
  - ../../domains/habitat/land_cover/README.md
  - ../../domains/habitat/ecoregions/README.md
  - ../../domains/fauna/README.md
  - ../../../../pipelines/proofs/habitat_fauna_thin_slice/README.md
  - ../../../../contracts/domains/habitat/
  - ../../../../contracts/domains/fauna/
  - ../../../../docs/domains/habitat/
  - ../../../../docs/domains/fauna/
  - ../../../../policy/domains/habitat/
  - ../../../../policy/domains/fauna/
  - ../../../../fixtures/domains/habitat/
  - ../../../../fixtures/domains/fauna/
  - ../../../../tests/domains/habitat/
  - ../../../../tests/domains/fauna/
notes:
  - "Expanded from an empty file at schemas/contracts/v1/relations/habitat_fauna/README.md."
  - "Current GitHub search did not surface schema files directly under this relation lane beyond this README."
  - "A proposed flat join scaffold exists at schemas/contracts/v1/joins/habitat-fauna-join.schema.json with empty properties, additionalProperties true, and contract_doc null."
  - "A Habitat × Fauna proof pipeline README exists under pipelines/proofs/habitat_fauna_thin_slice/ and is proof-harness authority, not schema authority."
  - "Habitat and Fauna domain schema READMEs were inspected as nearest verified domain lanes."
  - "This README is a relation-placement guardrail only; do not create canonical habitat-fauna relation schemas here without ADR, paired contracts, fixtures, validators, sensitivity/policy/release review, and steward review."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

![status](https://img.shields.io/badge/status-draft-yellow)
![root](https://img.shields.io/badge/root-schemas%2F-blue)
![family](https://img.shields.io/badge/family-relations-purple)
![relation](https://img.shields.io/badge/relation-habitat__fauna-green)
![posture](https://img.shields.io/badge/posture-guardrail-orange)
![truth](https://img.shields.io/badge/truth-cite--or--abstain-success)

> **Purpose.** `schemas/contracts/v1/relations/habitat_fauna/` is a README-only guardrail for possible machine-checkable relation shapes between Habitat references and Fauna references.
>
> **One-line boundary.** This path may describe relationship shape only. It must not replace Habitat, Fauna, Evidence, Policy, Release, emitted data roots, the existing join scaffold, or the Habitat × Fauna proof pipeline.

---

## Quick jumps

[Status](#status) · [Placement decision](#placement-decision) · [Repo fit](#repo-fit) · [Current inventory](#current-inventory) · [Related surfaced lanes](#related-surfaced-lanes) · [Candidate relation shapes](#candidate-relation-shapes) · [What belongs here](#what-belongs-here) · [What does not belong here](#what-does-not-belong-here) · [Relation guardrails](#relation-guardrails) · [Migration rules](#migration-rules) · [Validation](#validation) · [Rollback](#rollback) · [Open questions](#open-questions)

---

## Status

| Question | Answer | Truth label |
|---|---|---|
| Does this README path exist? | Yes: `schemas/contracts/v1/relations/habitat_fauna/README.md`. It was empty before this expansion. | **CONFIRMED** |
| Are schema files currently present directly under this relation lane? | Not found in the current GitHub search beyond this README. | **NEEDS VERIFICATION / search-limited** |
| Is a related join schema already present? | Yes. `schemas/contracts/v1/joins/habitat-fauna-join.schema.json` exists as a PROPOSED scaffold with empty `properties`, `additionalProperties: true`, and `contract_doc: null`. | **CONFIRMED scaffold / NEEDS VERIFICATION** |
| Is a related proof pipeline present? | Yes. `pipelines/proofs/habitat_fauna_thin_slice/README.md` exists as a proof-harness lane, not schema authority. | **CONFIRMED** |
| What are the nearest verified domain lanes? | Habitat and Fauna schema READMEs were inspected. | **CONFIRMED path evidence** |
| Is this relation lane canonical? | Not proven. Treat this path as README-only until ADR or steward decision. | **NEEDS VERIFICATION / ADR-sensitive** |
| Can this path store habitat data, fauna occurrence data, proof outputs, receipts, release records, public artifacts, or pipeline code? | No. This is schema documentation only, not lifecycle data, proof storage, release storage, publication surface, or executable pipeline root. | **CONFIRMED boundary** |

> [!IMPORTANT]
> Habitat-fauna relation schemas should connect references across domain-owned objects. They should not copy domain-owned fields, publish observations, turn Habitat context into Fauna truth, or turn Fauna occurrence into Habitat truth.

---

## Placement decision

Current placement posture:

```text
Requested relation guardrail:
  schemas/contracts/v1/relations/habitat_fauna/

Existing related join scaffold:
  schemas/contracts/v1/joins/habitat-fauna-join.schema.json

Related proof harness:
  pipelines/proofs/habitat_fauna_thin_slice/

Nearest inspected domain schema lanes:
  schemas/contracts/v1/domains/habitat/
  schemas/contracts/v1/domains/fauna/
```

Rationale:

- Domain schemas normally belong under `schemas/contracts/v1/domains/<domain>/...` unless an accepted exception says otherwise.
- Habitat owns habitat context, land-cover, ecoregion, suitability, habitat patch, and corridor object shapes where accepted.
- Fauna owns taxon, occurrence, range, monitoring, sensitive-site, and sensitivity-aware animal object shapes where accepted.
- A join scaffold already exists under `schemas/contracts/v1/joins/`; this relation lane must not duplicate or override that join surface without a migration/profile rule.
- The proof pipeline belongs under `pipelines/` because it is executable proof orchestration, not schema shape.
- Any future schema here must be paired with contracts, fixtures, validators, registry entries, sensitivity/policy review, release review, and steward review across affected domains.

---

## Repo fit

```text
schemas/
└── contracts/
    └── v1/
        ├── README.md
        ├── relations/
        │   ├── habitat_fauna/
        │   │   └── README.md                     # this file; relation guardrail only
        │   ├── biota/
        │   └── aquatic_biota/
        ├── joins/
        │   ├── README.md
        │   └── habitat-fauna-join.schema.json    # existing PROPOSED join scaffold
        └── domains/
            ├── habitat/
            │   ├── README.md                     # inspected Habitat domain schema lane
            │   ├── land_cover/
            │   └── ecoregions/
            └── fauna/
                └── README.md                     # inspected Fauna domain schema lane

pipelines/
└── proofs/
    └── habitat_fauna_thin_slice/                  # proof harness; not schema shape

contracts/
├── domains/habitat/                               # semantic meaning; not machine shape
└── domains/fauna/                                 # semantic meaning; not machine shape

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
| `schemas/contracts/v1/relations/habitat_fauna/README.md` | **CONFIRMED present** | Empty file expanded by this README. |
| `schemas/contracts/v1/relations/habitat_fauna/*.schema.json` | **Not found in current search** | Do not create here without ADR, paired contracts, and validation plan. |
| `schemas/contracts/v1/joins/habitat-fauna-join.schema.json` | **CONFIRMED scaffold** | PROPOSED join scaffold; empty `properties`, `additionalProperties: true`, `contract_doc: null`. |
| `pipelines/proofs/habitat_fauna_thin_slice/README.md` | **CONFIRMED inspected** | Proof-harness lane; not schema authority and not direct publication. |
| `schemas/contracts/v1/domains/habitat/README.md` | **CONFIRMED inspected** | Habitat domain schema lane with land-cover and ecoregions child lanes. |
| `schemas/contracts/v1/domains/fauna/README.md` | **CONFIRMED inspected** | Fauna domain schema lane; sensitivity posture is fail-closed where sensitive. |

---

## Related surfaced lanes

| Path | Role signal | Posture |
|---|---|---|
| `schemas/contracts/v1/relations/habitat_fauna/` | Possible neutral relation schema lane. | **README-only guardrail** |
| `schemas/contracts/v1/joins/habitat-fauna-join.schema.json` | Existing habitat-fauna join schema scaffold. | **PROPOSED / field-incomplete** |
| `pipelines/proofs/habitat_fauna_thin_slice/` | Executable proof-harness lane. | **DRAFT / not schema authority** |
| `schemas/contracts/v1/domains/habitat/` | Habitat-owned machine shape lane. | **PROPOSED / child lanes present** |
| `schemas/contracts/v1/domains/fauna/` | Fauna-owned machine shape lane. | **PROPOSED / sensitivity-aware** |
| `schemas/contracts/v1/relations/biota/` | Broader biota relation guardrail. | **README-only guardrail** |
| `schemas/contracts/v1/joins/` | Cross-domain join schema family. | **DRAFT / mixed schema and guardrail lanes** |

---

## Candidate relation shapes

Candidate schemas below require steward review, paired contracts, fixtures, validators, registry records, and sensitivity/policy/release review before promotion.

| Candidate schema | Purpose | Default posture |
|---|---|---|
| `habitat_fauna_relation.schema.json` | Generic relation envelope between Habitat references and Fauna references. | **PROPOSED / not created** |
| `fauna_habitat_context.schema.json` | Relation between fauna occurrence/range/taxon refs and habitat context refs. | **PROPOSED / evidence-bound** |
| `habitat_suitability_fauna_context.schema.json` | Relation between suitability/corridor context refs and fauna refs. | **PROPOSED / model-vs-observation-sensitive** |
| `fauna_habitat_release_projection.schema.json` | Public/release projection for already-governed Habitat × Fauna relation outputs. | **PROPOSED / release-gated** |

> [!CAUTION]
> Candidate names are proposals only. Do not treat them as repo files, accepted contracts, implementation proof, proof-pipeline output, or public-safe outputs until created, paired, fixture-tested, and reviewed.

---

## What belongs here

- This README.
- Relation schema placement notes for Habitat × Fauna relationship objects.
- Future neutral relation schema files if an accepted ADR or migration plan authorizes this lane.
- Links to paired contracts, fixtures, validators, schema registry records, policy references, evidence references, release references, correction references, rollback references, and tests.
- Drift notes preventing duplicate Habitat, Fauna, join, proof-pipeline, or relation schema authority.

---

## What does not belong here

- Habitat-owned canonical schemas.
- Fauna-owned canonical schemas.
- Join schemas already owned by `schemas/contracts/v1/joins/` unless migrated by review.
- Proof-pipeline code or proof-output artifacts.
- Semantic contract prose beyond README boundary notes.
- Policy rules, sensitivity decisions, exposure decisions, release decisions, or public map/API behavior.
- Lifecycle data, habitat records, fauna occurrence records, source records, catalog records, triplets, receipt instances, proof outputs, release records, correction notices, rollback cards, public artifacts, dashboards, screenshots, or generated summaries.
- Validator code, packages, pipelines, runtime code, UI/API implementation, or map tiles.
- Claims that a habitat-fauna relation is valid, complete, current, evidence-backed, policy-safe, release-approved, or public-ready merely because it validates against a schema.

---

## Relation guardrails

| Boundary | Requirement |
|---|---|
| Domain ownership | Habitat and Fauna keep their own canonical shapes and semantic contracts. |
| Relation neutrality | A relation schema records relationship shape, not source truth for either side. |
| Join overlap | The existing join scaffold must be profiled, migrated, or retained explicitly before this relation lane becomes schema-bearing. |
| Proof overlap | The proof pipeline demonstrates scoped behavior; it does not own schema shape or release authority. |
| Reference discipline | Use stable references to domain-owned objects rather than duplicating domain fields. |
| Evidence dependency | Relation outputs need EvidenceBundle or equivalent support where claims depend on evidence. |
| Model/observation discipline | Suitability, corridor, model, candidate, range, and occurrence labels must remain distinguishable. |
| Sensitivity posture | Sensitive ecological, exact-location, steward-controlled, or private-land-related surfaces require fail-closed review. |
| Release dependency | Public relation projections must be release-gated and rollback-aware. |
| No parallel authority | Do not maintain equivalent Habitat × Fauna relation schemas under `relations/`, `joins/`, proof pipelines, and domain lanes without a mirror/migration rule. |

---

## Migration rules

Do not move or duplicate Habitat × Fauna relation schemas into this path unless a reviewed migration plan defines:

- source path;
- target path;
- owning root;
- reason for migration;
- chosen meaning of `habitat_fauna`;
- relationship between `relations/habitat_fauna/`, `joins/habitat-fauna-join.schema.json`, and `pipelines/proofs/habitat_fauna_thin_slice/`;
- schema `$id` changes;
- `$ref` and consumer updates;
- fixture and validator updates;
- schema registry updates;
- Habitat, Fauna, policy, sensitivity, and release steward review;
- deprecation/mirror window;
- tests proving no parallel authority remains.

---

## Validation

Recommended local validation sequence:

```bash
# Confirm this relation lane remains README-only unless authorized.
find schemas/contracts/v1/relations/habitat_fauna -maxdepth 2 -type f | sort

# Inspect nearby relation/join/domain/proof surfaces.
find schemas/contracts/v1/relations schemas/contracts/v1/joins schemas/contracts/v1/domains/habitat schemas/contracts/v1/domains/fauna pipelines/proofs/habitat_fauna_thin_slice -maxdepth 5 -type f 2>/dev/null \
  | grep -Ei 'habitat|fauna|join|proof|occurrence|suitability|corridor|README' \
  | sort

# Detect duplicate Habitat-Fauna relation authority.
find schemas/contracts/v1 pipelines/proofs -maxdepth 7 -type f 2>/dev/null \
  | grep -Ei 'habitat[-_].*fauna|fauna[-_].*habitat|habitat-fauna|habitat_fauna' \
  | sort

# Validate JSON syntax for nearby schema files when present.
find schemas/contracts/v1/joins schemas/contracts/v1/domains/habitat schemas/contracts/v1/domains/fauna -name '*.schema.json' -print0 \
  | xargs -0 -r -I{} python -m json.tool {} >/dev/null

# Run project validators when available.
python tools/validate_all.py || true
pytest tests/schemas tests/contract tests/domains/habitat tests/domains/fauna tests/policy tests/release || true
```

Replace `|| true` with fail-closed CI behavior once validator and test paths are confirmed.

---

## Rollback

Rollback for this README is ordinary Git rollback: revert the commit that changed `schemas/contracts/v1/relations/habitat_fauna/README.md`.

Rollback for future relation schema changes requires checking every downstream reference:

1. Revert or migrate schema files.
2. Restore canonical `$id` and `$ref` targets.
3. Restore paired contract links.
4. Restore fixtures, validators, schema registry records, and CI paths.
5. Restore Habitat, Fauna, policy, sensitivity, evidence, release, correction, and receipt references.
6. Restore proof-pipeline, API/UI, MapLibre, and Evidence Drawer consumers.
7. Preserve correction and rollback records if any public relation surface was affected.

---

## Open questions

| Question | Status | Owner |
|---|---|---|
| Should Habitat × Fauna relationship shapes live under `relations/`, `joins/`, Habitat, Fauna, or another accepted lane? | **NEEDS VERIFICATION / ADR-sensitive** | Relation steward + domain stewards |
| Should `joins/habitat-fauna-join.schema.json` be profiled, migrated, replaced, or retained separately from this relation lane? | **NEEDS VERIFICATION / migration-sensitive** | Schema steward + Relation steward |
| Which semantic contract owns neutral Habitat × Fauna relation meaning? | **NEEDS VERIFICATION** | Contract steward |
| Which fixtures prove that relations reference domain-owned objects without duplicating fields? | **NEEDS VERIFICATION** | Validation steward |
| Which Habitat × Fauna relation projections are safe for public API/MapLibre/Focus Mode use? | **NEEDS VERIFICATION / release-gated** | Release steward + Policy steward |

---

## Maintainer notes

- Keep this path README-only until relation-home placement is resolved.
- Prefer references to domain-owned Habitat and Fauna objects over copied fields.
- Do not let this relation lane duplicate the existing join scaffold, proof pipeline, or domain schema authority.
- Preserve evidence, sensitivity, domain ownership, policy, release, correction, and rollback boundaries for every Habitat × Fauna relation surface.
