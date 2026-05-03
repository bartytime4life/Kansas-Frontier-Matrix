# Geology & Natural Resources Cross-Lane Relations

Rules for relating geology assertions to adjacent lanes without collapsing source-of-truth boundaries.

## Relation principles

1. Relations add context; they do not transfer authority.
2. The upstream claim keeps its own source role, review state, and policy burden.
3. Cross-lane joins must be explicit, typed, and auditable.

## Common relation patterns

| Geology object | Adjacent lane | Allowed relation type | Guardrail |
| --- | --- | --- | --- |
| Geologic unit | Soil | `influences_parent_material` | Soil interpretation remains a soil-lane claim. |
| Aquifer-bearing formation | Hydrology | `hydrostratigraphic_context_for` | Does not override observed water levels/quality. |
| Fault or landform feature | Hazards | `context_for_hazard_assessment` | Hazard likelihood/severity remains hazard-lane governed. |
| Resource occurrence area | Settlements/Infrastructure | `near_or_overlaps_infrastructure_context` | Proximity is not causality or legal encumbrance truth. |
| Permit/lease record | People/Land ownership | `administrative_relation_to_parcel_or_operator` | Administrative linkage does not prove geologic deposit. |

## Required relation metadata

- `relation_type`
- `subject_ref`
- `object_ref`
- `assertion_basis`
- `confidence_or_certainty`
- `source_ref`
- `review_state`

## Deny rules

- Deny relations that imply legal ownership from physical geology alone.
- Deny relations that expose restricted exact coordinates through secondary joins.
- Deny relations that erase modeled vs observed boundaries.
