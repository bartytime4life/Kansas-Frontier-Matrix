<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/contracts-domains-water-planning-project
title: Project Contract — Water Planning
type: semantic-contract
version: v0.2
status: draft; PROPOSED; schema-scaffold; reference-authority checks implemented; NEEDS VERIFICATION before promotion
owners:
  - OWNER_TBD — Water Planning domain steward
  - OWNER_TBD — Contracts steward
  - OWNER_TBD — Source steward
  - OWNER_TBD — Schema steward
  - OWNER_TBD — Policy steward
created: 2026-07-28
updated: 2026-07-30
policy_label: public-with-gates; semantic-contract; water-planning; deferred-epic; PROPOSED
related:
  - ./README.md
  - ../../../schemas/contracts/v1/domains/water_planning/project.schema.json
  - ../../../fixtures/domains/water_planning/project/
  - ../../../fixtures/domains/water_planning/geometry_authority/
  - ../../../tools/validators/domains/water_planning/validate_geometry_authority.py
  - ../../../tests/domains/water_planning/test_geometry_authority.py
  - ../../../docs/sources/catalog/kansas/kwo.md
  - ../../../tests/schemas/test_water_planning_contracts.py
[/KFM_META_BLOCK_V2] -->

# Project Contract — Water Planning

> **Status:** `draft` / PROPOSED semantic contract
> **Schema:** `schemas/contracts/v1/domains/water_planning/project.schema.json`
> **Fixtures:** `fixtures/domains/water_planning/project/`
> **Authority checks:** `tools/validators/domains/water_planning/validate_geometry_authority.py`

## Meaning

A water infrastructure project associated with an Award. Missing recipient identity remains `recipient_resolution_status: unresolved`. Project-region membership and project-location geometry are separate facts with separate resolution states. Neither may be inferred from the other.

`planning_region_resolution_status` states whether `planning_region_ref` has resolved against the exact 14-record RAC identity inventory. `geometry_confidence` states whether `location_ref` has resolved against a declared project-location geometry authority. Null or unavailable facts remain explicit; they are never guessed.

## Authority and resolution rules

- `planning_region_resolution_status: unresolved` requires `planning_region_ref: null`.
- A resolved `planning_region_ref` must be one of `kwo-rac-01` through `kwo-rac-14` and must exist in the exact governed RAC inventory.
- A GMD, county, municipality, recipient, venue, or other regional identifier cannot satisfy `planning_region_ref`.
- `geometry_confidence: unresolved` requires `location_ref: null`.
- `approximate` and `confirmed` each require a non-inline reference to a declared project-location geometry authority record with version, digest, correction posture, and use boundary.
- Region membership does not prove a project location; a location reference does not prove region membership.
- Address, recipient, venue, county, project prose, centroid, containment, or proximity must not be converted into a region or geometry fact.

## Anti-collapse boundaries

- A project is not a completion, payment, construction milestone, or operational benefit.
- Missing recipient identity is unresolved, never guessed.
- Missing project region or geometry is unresolved, never guessed.
- Project-region membership is not project-location geometry.
- Link presence, a recipient table, or source-page text is not geometry proof.
- A passing schema or validator is not source admission, proof, release, or publication.

## Schema posture

| Schema fact | Status |
|---|---|
| Schema file | `schemas/contracts/v1/domains/water_planning/project.schema.json` |
| Schema status | `PROPOSED` |
| Exact RAC reference pattern | `^kwo-rac-(0[1-9]\|1[0-4])$` |
| Region-resolution coherence | Enforced by schema shape and reference-authority validator |
| Location-resolution coherence | Enforced by schema shape and reference-authority validator |
| `additionalProperties` | `false` |

## Related

- [`README.md`](./README.md) — Domain contract index
- [`docs/sources/catalog/kansas/kwo.md`](../../../docs/sources/catalog/kansas/kwo.md) — KWO source catalog entry
- [`schemas/contracts/v1/domains/water_planning/project.schema.json`](../../../schemas/contracts/v1/domains/water_planning/project.schema.json) — Schema
- [`fixtures/domains/water_planning/geometry_authority/`](../../../fixtures/domains/water_planning/geometry_authority/) — Synthetic authority fixtures
- [`tools/validators/domains/water_planning/validate_geometry_authority.py`](../../../tools/validators/domains/water_planning/validate_geometry_authority.py) — Deterministic checker
- [`tests/domains/water_planning/test_geometry_authority.py`](../../../tests/domains/water_planning/test_geometry_authority.py) — No-network tests

