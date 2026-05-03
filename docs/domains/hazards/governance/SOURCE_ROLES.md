# Hazards Source Roles

This file defines source-role boundaries used by validation, UI labeling, and policy checks.

## Role taxonomy

| Role | Meaning | Must not be interpreted as |
| --- | --- | --- |
| `historical_event_record` | Published record of a past event. | Active warning or response instruction. |
| `operational_warning` | Warning context with issue/expiry/freshness. | KFM emergency guidance. |
| `operational_advisory` | Advisory context about conditions. | Verified event occurrence. |
| `operational_watch` | Watch context for potential hazards. | Confirmed impacts. |
| `administrative_declaration` | Governmental declaration context. | Direct physical evidence. |
| `regulatory_context` | Regulatory hazard-zone context. | Observed on-the-ground condition. |
| `scientific_observation` | Instrument/report-based observation. | Legal declaration. |
| `remote_sensing_detection` | Detection product from remote sensing workflows. | Field confirmation by default. |
| `modeled_derivative` | Model output with methods and inputs. | Observation truth. |
| `resilience_analysis` | Planning-oriented interpretive derivative. | Damage truth/prediction certainty. |
| `local_context` | Reviewed local context sources. | Automatically publishable public truth. |
| `unknown_unclassified` | Unmapped role. | Publishable material. |

## Enforcement rules

- Role is required and single-valued for each primary hazard object.
- `unknown_unclassified` cannot promote.
- Role changes require explicit supersession/correction lineage.
- UI badge text must match role semantics.
