<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/intake/resource-lifecycle-object-map-source-map
title: Resource Lifecycle and Governed API Object-Map Source Map
type: exploratory-source-map
version: v0.1.0
status: exploratory; implementation-mapped; non-authoritative
owners: OWNER_TBD — contracts steward; API steward; docs steward
created: 2026-08-10
updated: 2026-08-10
policy_label: internal; exploratory-intake; resource-lifecycle; governed-api
owning_root: docs/
responsibility: Preserve source-to-repository reasoning for the bounded resource-lifecycle and governed-API overlay on the canonical Contract Object Map.
truth_posture: CONFIRMED repository evidence; PROPOSED relationship overlay; NEEDS VERIFICATION completeness and deployed behavior
related:
  - ../../../contracts/OBJECT_MAP.md
  - ../../../control_plane/object_family_register.yaml
  - ../../architecture/governed-ai/ROUTE_MAP.md
  - ../../architecture/governed-api/LIFECYCLE_GATES.md
  - ../../../apps/governed-api/src/governed_api/routes/registry.py
  - ../../../tools/validators/docs/validate_contract_object_map_lifecycle.py
  - ../../../tests/docs/test_contract_object_map_lifecycle.py
  - ../../adr/ADR-0029-adopt-directory-governance-standard-v2.md
notes:
  - "This map preserves exploratory lineage and does not promote an attached or Drive source to repository authority."
[/KFM_META_BLOCK_V2] -->

# Resource Lifecycle and Governed API Object-Map Source Map

## Goal

Implement the smallest collision-safe slice of Pass 20 `EXP-012`: relate selected KFM resource families to lifecycle positions and governed-API relationships while preserving the repository's existing Contract Object Map as the single navigation surface.

## Source and collision review

| Evidence | Observation on authoring base | Disposition |
|---|---|---|
| Attached `KFM_Pass_20_Part_2_Idea_Index_Category_Atlas_and_Expansion_Dossier.md` (`sha256:57e4b74255b52863f2a489595077741d7f45c2968a9740fe4837bac73778f780`) | `EXP-012` proposes a resource ontology and API lifecycle map; `KFM-IDX-MAP-002` calls for explicit resources, lifecycles, relationships, and HTTP discipline. | PROPOSAL LINEAGE; not current implementation proof |
| Google Drive `Kansas Frontier Matrix — Connected-Dots Architecture Brief` (`gdrive://1sdiLNDLFr2cVD3Q8h3ZvHO4D96WLJ6V7vf5neNzEyTM`) | Supplies architecture-doctrine context for the governed API as a trust boundary. | PROPOSAL LINEAGE; repository evidence controls implementation claims |
| `contracts/OBJECT_MAP.md` | Already owns the contract-to-schema/object navigation crosswalk. | EXTEND IN PLACE; do not create a parallel ontology |
| `control_plane/object_family_register.yaml` | Already supplies a partial, machine-readable, navigational object-family projection. | PRESERVE; the overlay does not become a second register |
| `docs/architecture/governed-ai/ROUTE_MAP.md` | Already defines six governed-API relationship families. | REUSE terminology; do not invent endpoint authority |
| `docs/architecture/governed-api/LIFECYCLE_GATES.md` | Already states that request-time API behavior reflects lifecycle state and cannot create release state. | PRESERVE authority boundary |
| `apps/governed-api/src/governed_api/routes/registry.py` | Registers only `/bootstrap`, `/evidence`, and `/layers` on `main@9e76413313b8529091d01be6132d6e987e3f9fae`; each handler returns `ABSTAIN`. | RECORD exact bounded snapshot; do not imply live resolvers |
| Repository and open-PR search | No separate EXP-012 implementation was found; the collision is with existing canonical surfaces, not with a missing concept. | ADD overlay and parity check only |

## Bounded implementation

The candidate updates the canonical object map with a marker-bounded table, selected resource relationships, explicit non-goals, and the exact current route inventory. A no-network validator checks marker integrity, resource-token coverage, repository path existence, route-table parity, and finite `ABSTAIN` behavior. Tests and read-only CI exercise those claims.

This packet does not define URLs, HTTP verbs, authorization, OpenAPI, public DTOs, resource completeness, source admission, lifecycle transitions, policy decisions, evidence closure, release state, deployment, or publication.

## Proof claim

A green result proves that the bounded documentation overlay still names the selected resource families, points to paths that exist in the tested checkout, and matches the executable stub registry. It does not prove semantic completeness, production readiness, current deployment, or public availability.

## Rollback

Revert the isolated documentation-and-validation commit. No source, lifecycle state, runtime store, route, deployment, or public compatibility obligation is changed.
