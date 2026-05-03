# Archaeology Domain Model

## Core entities

- `archaeology_site`
- `archaeology_component`
- `archaeological_feature`
- `stratigraphic_unit`
- `provenience_context`
- `survey_project`
- `survey_transect`
- `survey_observation`
- `excavation_unit`
- `artifact_record`
- `assemblage`
- `sample_record`
- `lab_result`
- `chronometric_determination`
- `report_bibliographic_source`
- `historic_archival_source`
- `geophysical_observation`

## Relationship expectations

- Site -> many components/features/contexts.
- Survey and excavation objects support site-level claims.
- Artifact/lab/chronometric objects require provenance links.
- Candidate-feature objects cannot imply confirmed-site status without review.

## Public-safe representation

Public payloads must use approved generalized/suppressed geometry and include provenance and review context.
