# WBD HUC12 Material Change Validator

Deterministic, no-network validation for the fixture profile in:

- `contracts/domains/hydrology/wbd_huc12_material_change_assessment.md`
- `schemas/contracts/v1/domains/hydrology/wbd_huc12_material_change_assessment.schema.json`

The validator canonicalizes Polygon/MultiPolygon rings without geospatial network or native-library dependencies, checks coordinate bounds, recomputes geometry-plus-area fingerprints, ignores metadata-only churn, derives exact ADD/REMOVE/NO_CHANGE/MATERIAL_CHANGE outcomes, and verifies the assessment `spec_hash`.

It does not call the WBD service, activate the source descriptor, write lifecycle data, promote, or publish.
