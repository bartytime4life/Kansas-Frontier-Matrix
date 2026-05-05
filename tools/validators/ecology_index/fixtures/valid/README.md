# Ecology Index Valid Fixtures

This directory contains **known-good fixtures** for `tools/validators/ecology_index`.
Each JSON file in this directory is expected to return a `pass` decision when
validated by the module CLI.

## Fixture inventory

- `huc12_vegetation_soil_hydrology.json`
- `fauna_habitat_grid.json`
- `air_station_vegetation.json`

## Validation contract

Valid fixtures in this folder must satisfy both schema and semantic checks used
by the validator, including:

- required top-level keys such as `index_id`, `geom_id`, `geometry_type`,
  `time_bucket`, `spec_hash`, `domains`, `join_keys`, `evidence_refs`, `status`
- `spec_hash` formatted as 64-character lowercase hex
- non-empty `evidence_refs`
- supported `domains`
- geometry/domain conditional requirements (for example,
  `geometry_type: huc12` requires `join_keys.watershed_id`; fauna domain requires
  at least one of `join_keys.taxon_id` or `join_keys.obs_id`)

## Run locally

From the repository root:

```bash
python -m tools.validators.ecology_index tools/validators/ecology_index/fixtures/valid/huc12_vegetation_soil_hydrology.json
python -m tools.validators.ecology_index tools/validators/ecology_index/fixtures/valid/fauna_habitat_grid.json
python -m tools.validators.ecology_index tools/validators/ecology_index/fixtures/valid/air_station_vegetation.json
```

Or run fixture coverage tests:

```bash
pytest -q tools/validators/ecology_index/tests/test_validator_fixtures.py
```
