# Ecology Source Roles

This document defines source roles used across ecology registries, contracts, and publication policy.

## Role Taxonomy

| Role | Meaning | May be used as direct claim evidence? |
|---|---|---|
| `authority` | Taxonomic/reference authority (backbone taxonomy, controlled vocabularies). | Yes, for naming/taxonomic alignment. |
| `observation` | Primary observed field/specimen/station records. | Yes, with rights and sensitivity checks. |
| `aggregator` | Repackaged records from upstream publishers (not original observer). | Yes, but provenance to upstream should be retained. |
| `model` | Predicted/interpolated/suitability outputs. | No direct occurrence claim; only supporting context. |
| `baseline` | Environmental baselines/time-window summaries. | Yes, for baseline context only. |
| `regulatory_context` | Legal/protected status or management boundaries. | Yes, as governance context (not occurrence evidence). |
| `render_descriptor` | Layer styling/renderer metadata. | No. Never counts as evidence. |

## Role Rules

1. `model` outputs cannot be emitted as observed occurrence claims unless explicitly paired with observed evidence.
2. `aggregator` records must preserve upstream source attribution whenever available.
3. `render_descriptor` references cannot satisfy evidence requirements.
4. `authority` records should include version and release date where possible.
5. Unknown role values are invalid and should fail validation.

## Practical Examples

- GBIF occurrence feed: `aggregator`
- Herbarium specimen export from custodian institution: `observation`
- NDVI anomaly surface: `model`
- US EPA ecoregion definitions: `regulatory_context`
