<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/NEEDS_VERIFICATION__airnow_layer1
title: AirNow Layer 1 Source Intake
type: standard
version: v1
status: draft
owners: NEEDS_VERIFICATION
created: 2026-05-02
updated: 2026-05-02
policy_label: public-safe
repo_path: docs/sources/airnow/README.md
related: [data/sources/airnow/source_descriptor.airnow.v1.json, schemas/air_quality/airnow/, tests/fixtures/air_quality/airnow/, tools/validators/air_quality/validate_airnow_layer1.py]
tags: [kfm, airnow, intake, fixtures, offline, air_quality]
notes: [Layer 1 is offline fixture-backed intake planning only; no live ingestion enabled.]
[/KFM_META_BLOCK_V2] -->

# AirNow Layer 1 (Offline Intake Foundation)

## Purpose
Establish a minimal, reversible, offline intake foundation for AirNow current-observation and forecast records using synthetic fixtures and fail-closed validation only.

## Lifecycle placement
RAW-source-intake planning only. This slice does not publish, tile, expose UI, or provide public API output.

## AirNow product summary
AirNow documentation identifies web services for selected-area queries and file products suitable for database population workflows. Layer 1 documents both as references only; no network execution is implemented.

## Web services vs file products
- Web services: selected-area candidate mode only.
- File products: database-population candidate mode only.
- Bulk ZIP/database loops via web services are prohibited.

## No-network Layer 1 boundary
- No live API calls.
- No API keys.
- Fixtures are synthetic and flagged `fixture_only: true`, `no_live_airnow_data: true`, `not_for_publication: true`.

## Public-safety cautions
- AirNow values are preliminary and subject to change.
- AirNow is not an emergency alert system.
- Outputs are public-health environmental observations/forecasts, not emergency notifications.

## Governance gates
Validator fails closed for missing provenance, unknown pollutant, invalid AQI/category, missing required timestamps, missing reporting area, preliminary flag violations, and bulk-loop manifest violations.

## Validation commands
- `python tools/validators/air_quality/validate_airnow_layer1.py tests/fixtures/air_quality/airnow/valid/observation_wichita_pm25.json`
- `python tools/validators/air_quality/validate_airnow_layer1.py tests/fixtures/air_quality/airnow/valid/forecast_wichita_ozone.json`
- `python tools/validators/air_quality/validate_airnow_layer1.py tests/fixtures/air_quality/airnow/valid/intake_manifest_fixture_only.json`
- `pytest tests/air_quality/test_airnow_layer1.py`

## Fixture map
- valid observation: `tests/fixtures/air_quality/airnow/valid/observation_wichita_pm25.json`
- valid forecast: `tests/fixtures/air_quality/airnow/valid/forecast_wichita_ozone.json`
- valid manifest: `tests/fixtures/air_quality/airnow/valid/intake_manifest_fixture_only.json`
- invalid unknown pollutant: `tests/fixtures/air_quality/airnow/invalid/observation_unknown_pollutant.json`
- invalid missing forecast date: `tests/fixtures/air_quality/airnow/invalid/forecast_missing_date_forecast.json`
- invalid bulk ZIP loop: `tests/fixtures/air_quality/airnow/invalid/intake_manifest_bulk_zip_loop.json`

## Next layers
Layer 2 may add governed ingestion orchestration and receipts against approved rights/provenance gates. Layer 1 intentionally stops at descriptor + schemas + fixtures + validator + tests.

## Source references
- https://docs.airnowapi.org/
- https://docs.airnowapi.org/webservices
- https://docs.airnowapi.org/faq

- [Layer 31 Closure Archive Index Audit](LAYER31_CLOSURE_ARCHIVE_INDEX_AUDIT.md)
