# Flora Source Registry Guide

## Goal
Define how flora sources are classified before they are eligible for processing or publication.

## Required descriptor fields
- Source ID and human-readable name
- Source role (authority vs support vs derived)
- Rights/license and redistribution posture
- Sensitivity/geoprivacy posture
- Cadence and freshness expectations
- Spatial/temporal support
- Steward owner and review requirements

## Source roles
| Role | Allowed use | Not allowed |
| --- | --- | --- |
| `official` | Authority-backed status or canonical program layer | Community observations as legal truth |
| `institutional` | Specimen/collection support with provenance | Public exact geometry without clearance |
| `steward_reviewed` | Curated and reviewed flora support | Automatic public publication |
| `community_observation` | Corroborative evidence with quality checks | Sole authority for legal status |
| `derived_model` | Condition/suitability context with uncertainty | Direct observation truth |
| `controlled_access` | Restricted internal analysis | Public exact publication by default |

## Admission rule
Unknown source role, unknown rights, or unresolved sensitivity blocks promotion.

## Minimum fixture expectation per source
- 1 valid descriptor fixture.
- 1 invalid rights fixture.
- 1 invalid sensitivity/publication fixture.
