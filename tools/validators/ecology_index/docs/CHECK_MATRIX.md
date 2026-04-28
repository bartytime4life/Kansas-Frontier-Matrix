# Ecology Index Validator Check Matrix

This matrix documents the checks implemented by the ecology index validator and the expected failure codes.

| Check | Description | Fails with |
|---|---|---|
| JSON parsing | Input must parse as a JSON object. | `invalid_json`, `input_not_object` |
| Schema validation | Input must satisfy the configured JSON schema. | `schema_validation_error` |
| `spec_hash` required | `spec_hash` must be present and non-empty. | `missing_spec_hash` |
| `domains` required | `domains` must be a non-empty array. | `domains_missing_or_empty` |
| Domain allowlist | Domains must be in validator allowlist. | `unknown_domain` |
| `evidence_refs` required | `evidence_refs` must be non-empty. | `evidence_refs_empty` |
| Join key conditional checks | Domain + geometry combinations must include required join keys. | `missing_watershed_id`, `missing_taxon_or_obs_id`, `missing_soil_pedon_id`, `missing_station_id`, `missing_grid_id_or_habitat_code` |

## Fixture coverage mapping

- `fixtures/valid/` provides passing examples for watershed, fauna/habitat grid, and air station/vegetation joins.
- `fixtures/invalid/` provides failure examples for unknown domain, empty evidence refs, missing spec hash, and missing conditional join keys.

## CI expectation

The validator CI workflow must run:

1. Unit tests under `tools/validators/ecology_index/tests/`
2. A direct sweep of valid fixtures (must pass)
3. A direct sweep of invalid fixtures (must fail)
