<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/intake-admin-boundary-change-source-map
title: AdminBoundaryChange Source Map
type: exploratory-source-map
version: v1.0.0
status: proposed; source-grounded; non-authoritative
owners: OWNER_TBD — Intake steward · Geography steward · Evidence steward
created: 2026-08-10
updated: 2026-08-10
policy_label: public; docs; intake; exploratory; AdminBoundaryChange
tags: [kfm, source-map, AdminBoundaryChange, GeographyVersion, GeographyCrosswalk]
related:
  - ../../../contracts/common/admin_boundary_change.md
  - ../../../schemas/contracts/v1/common/admin_boundary_change.schema.json
  - ../../../contracts/common/geography_version.md
  - ../../../contracts/crosswalks/geography_crosswalk.md
notes:
  - "This map records source-to-repository interpretation; it grants no legal, boundary, identity, policy, review, release, or publication authority."
[/KFM_META_BLOCK_V2] -->

# AdminBoundaryChange source map

## Evidence ledger

| Source | Truth label | Relevant idea | Repository interpretation |
|---|---|---|---|
| Google Drive `KFM_Full_Atlas_seed_cards`, “Frontier Demography Economy Settlement Land Time Matrix Lane Pattern” | `CONFIRMED` | The Frontier Matrix lane names `Admin Boundary Change` alongside `GeographyVersion`, crosswalks, observations, uncertainty, threshold models, and releases, while excluding People/DNA, roads, and settlement truth ownership. | Add only a shared administrative geography-lineage event; make no person, parcel, road, settlement, or sovereign-truth claim. |
| `Kansas Frontier Matrix Implementation Reference`, pp. 1 and 10 | `CONFIRMED` | Historical geography broadening follows the staged frontier product; temporal alignment must use `GeographyVersion`, and changed geography requires a crosswalk rather than silent interpolation. | Pin source/target geography versions and require explicit unresolved/referenced crosswalk posture; never transfer observations or infer identity. |
| Existing `GeographyVersion` and `GeographyCrosswalk` contracts on `main` | `CONFIRMED` | Feature identity is version-local and a different-version join needs a separate reviewed crosswalk. | Keep this event declaration additive and inactive; reference those objects without resolving or duplicating them. |
| Google Drive Directory Rules and repository ADR-0029 | `CONFIRMED` | Content belongs under responsibility roots, not new topic roots. | Place semantic meaning in `contracts/common/` and supporting artifacts in existing schema, fixture, validator, test, workflow, intake, and receipt roots. |
| Event cardinality and source-role vocabulary in this PR | `PROPOSED` | One bounded implementation of the named object. | Keep fixture-only pending geography-steward and legal-source review. |

## Included

- ten finite administrative change types;
- explicit source/target version and feature cardinality;
- version-local identity with no equivalence assertion;
- `NOT_APPLICABLE`, `UNRESOLVED`, and `REFERENCED_NOT_RESOLVED` crosswalk postures;
- source publication/retrieval time separation;
- source, evidence, rights, sensitivity, disclosure, and inactive-governance posture;
- deterministic no-network validator, exact fixtures, tests, CI, and current-state receipt.

## Excluded

- coordinates, geometry, boundary comparison, names, and source payloads;
- legal validation or authoritative boundary truth;
- crosswalk rows, weights, execution, reverse inference, or identity equivalence;
- population, area, observation, or classification transfer;
- policy, review, promotion, release, public use, publication, deployment, or registry activation.

## Placement rationale

The event is a common geography-lineage value object consumed across domains. `contracts/common/` is therefore the narrowest accepted semantic home beside `GeographyVersion`. The packet creates no root, data store, active registry record, domain authority, release lane, runtime, or public API.
