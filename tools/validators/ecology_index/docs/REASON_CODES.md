# Ecology Index Validator Reason Codes

Canonical reason codes emitted by the validator.

## Input and schema

- `invalid_json`: input could not be decoded as JSON.
- `input_not_object`: decoded JSON was not an object.
- `schema_validation_error`: JSON schema validation failed.

## Required fields

- `missing_spec_hash`: `spec_hash` absent or empty.
- `domains_missing_or_empty`: `domains` absent or empty.
- `evidence_refs_empty`: `evidence_refs` absent or empty.

## Domain and conditional join keys

- `unknown_domain`: one or more listed domains are unsupported.
- `missing_watershed_id`: required watershed join key missing for hydrology + `huc12` geometry.
- `missing_taxon_or_obs_id`: required `taxon_id` or `observation_id` missing for fauna rows.
- `missing_soil_pedon_id`: required `soil_pedon_id` missing for soil rows.
- `missing_station_id`: required `station_id` missing for air rows.
- `missing_grid_id_or_habitat_code`: required `grid_id` or `habitat_code` missing for vegetation rows.

## Notes

- A single record may emit multiple reason codes.
- CLI output deduplicates repeated reasons in user-facing output while preserving error count semantics in tests.
