# AirNow Layer 2 Normalization

## Metadata
- Layer: 2 (offline normalization)
- Normalizer: `airnow_layer2` v1
- Scope: fixture-style Layer 1 AirNow records only

## Purpose
Deterministic offline canonicalization of Layer 1 AirNow observations/forecasts into KFM canonical JSONL, with strict provenance, quarantine, and normalization receipts.

## Why no API calls
Layer 2 is governance-constrained to offline processing only; no network calls, no API keys, and no bulk ZIP-code loops are allowed.

## Inputs/Outputs
- Inputs: Layer 1 manifest JSON + JSONL observation/forecast records.
- Outputs: `normalized_observations.jsonl`, `normalized_forecasts.jsonl`, `quarantine.jsonl`, `normalization_receipt.json`.

## Observation vs Forecast
Forecasts are never normalized as observations and observations are never normalized as forecasts.

## Time handling
If only a local timezone abbreviation exists (e.g. `CST`), UTC conversion is not attempted (`observed_at_utc=null`).

## Pollutant map
- OZONE/Ozone/O3 => O3 (ppb)
- PM2.5/PM25/PM_2_5/PM 2.5 => PM25 (ug/m3)
- PM10/PM 10 => PM10 (ug/m3)
- NO2/Nitrogen Dioxide => NO2 (ppb)
- SO2/Sulfur Dioxide => SO2 (ppb)
- CO/Carbon Monoxide => CO (ppm)

## AQI categories
1 Good (0-50), 2 Moderate (51-100), 3 Unhealthy for Sensitive Groups (101-150), 4 Unhealthy (151-200), 5 Very Unhealthy (201-300), 6 Hazardous (301-500).
Aliases: `USG`, `Unhealthy for Sensitive` => `Unhealthy for Sensitive Groups`.

## Quarantine reason codes
SCHEMA_INVALID, UNKNOWN_OBJECT_TYPE, UNKNOWN_POLLUTANT, AQI_OUT_OF_RANGE, AQI_CATEGORY_MISMATCH, MISSING_TIMESTAMP, MISSING_REPORTING_AREA, PRELIMINARY_DATA_FALSE, MISSING_PROVENANCE, NETWORK_FORBIDDEN, BULK_LOOP_DENIED, FORECAST_OBSERVATION_ROLE_CONFLICT, TIME_CONVERSION_AMBIGUOUS, EXACT_SENSITIVE_DENIED.

## CLI
`python tools/air_quality/airnow_normalize_batch.py --manifest tests/fixtures/air_quality/airnow/valid/intake_manifest_fixture_only.json --input tests/fixtures/air_quality/airnow/layer2/input/mixed_valid_invalid_batch.jsonl --out-dir /tmp/airnow_layer2_out --created-at 2026-01-01T00:00:00Z`

## Tests
- `pytest tests/air_quality/test_airnow_layer2_normalization.py`
- `pytest tests/air_quality/test_airnow_layer2_cli.py`

## Governance boundaries
References: https://docs.airnowapi.org/, https://docs.airnowapi.org/webservices, https://docs.airnowapi.org/faq . AirNow data are preliminary and subject to change.

## Next layer
Layer 3 should prioritize offline parsing of AirNow file products (e.g. reportingarea.dat/cityzipcodes.csv). Live selected-area web-service ingestion remains blocked pending explicit governance approval and rate-limit policy.
