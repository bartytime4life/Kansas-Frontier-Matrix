# Atmosphere / Air Knowledge Character

Taxonomy that prevents category collapse in atmosphere-air.

## Canonical characters

- `OBSERVED_SENSOR`
- `PUBLIC_AQI_REPORT`
- `REGULATORY_ARCHIVE`
- `LOW_COST_SENSOR`
- `ATMOSPHERIC_MODEL_FIELD`
- `REMOTE_SENSING_MASK`
- `DERIVED_FUSION`
- `CLIMATE_ANOMALY_CONTEXT`
- `METEOROLOGICAL_CONTEXT`
- `ALERT_AND_ADVISORY_CONTEXT`

## Anti-collapse rules

- Never present AQI as raw concentration.
- Never present AOD or smoke masks as PM2.5 exposure by default.
- Never present model fields as observed measurements.
- Never hide fused inputs behind a single opaque layer.
