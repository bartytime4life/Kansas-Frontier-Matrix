# Valid precipitation-observation fixtures

`fixtures/domains/atmosphere/valid/precipitation-observation/`

Status: draft / nested fixture lane.

This directory is for positive `PrecipitationObservation` fixture examples used by bounded tests, validators, no-network checks, helpers, or documentation examples. These files are examples only and are not authoritative precipitation records.

## Scope

Use this lane for compact synthetic precipitation-specific weather cases that are expected to pass a specific check while preserving KFM's precipitation-observation boundary. A valid `PrecipitationObservation` fixture may represent governed precipitation amount, rate, accumulation, intensity, type, trace state, weather-station context, source role, observed time, retrieval time, valid time, canonical units, QA posture, freshness, evidence references, or release dry-run fields required by the test.

A valid fixture here does not prove real-world precipitation, flood/drought truth, hazard impact, crop impact, infrastructure impact, climate baseline/anomaly truth, forecast truth, source-rights clearance, public release, or policy approval.

## Expected passes

Examples may include payloads that demonstrate:

- station, grid, source product, or network context is present when required
- source identity and source role are explicit, including whether the case is observed precipitation or meteorological context
- observed time, retrieved time, valid time, canonical units, QA posture, freshness, and correction fields are represented when required
- precipitation remains distinct from generic `WeatherObservation`, temperature observations, wind fields, forecast context, climate normals, climate anomalies, hazard impacts, and advisory context
- evidence references close within the fixture-only test boundary when required
- safe-render or release dry-run behavior is demonstrated without promoting anything to `data/published/`

## Related fixture lanes

- `../README.md`
- `../../golden/README.md`
- `../../invalid/README.md`
- `../../objects/README.md`
- `../../sources/README.md`

## Related references

- `../../../../../contracts/domains/atmosphere/PrecipitationObservation.md`
- `../../../../../contracts/domains/atmosphere/WeatherObservation.md`
- `../../../../../contracts/domains/atmosphere/TemperatureObservation.md`
- `../../../../../contracts/domains/atmosphere/WindField.md`
- `../../../../../contracts/domains/atmosphere/ForecastContext.md`
- `../../../../../contracts/domains/atmosphere/ClimateNormal.md`
- `../../../../../contracts/domains/atmosphere/ClimateAnomaly.md`
- `../../../../../docs/runbooks/atmosphere/NO_NETWORK_TEST_RUNBOOK.md`
- `../../../../../docs/domains/atmosphere/OBJECT_FAMILY_MAP.md`
- `../../../../../docs/domains/atmosphere/POLICY.md`
- `../../../../../schemas/contracts/v1/domains/atmosphere/PrecipitationObservation.schema.json`
- `../../../../../docs/doctrine/directory-rules.md`

## Maintenance notes

- Keep examples synthetic, compact, deterministic, and reviewable.
- Keep each valid fixture tied to a known test, validator, no-network check, helper, or documentation example.
- Record what the fixture is expected to pass; avoid broad claims of real-world correctness.
- Keep `PrecipitationObservation` distinct from generic weather observations, temperature observations, wind fields, model/forecast context, climate normal/anomaly claims, hazards or impact claims, advisory context, evidence proof, health guidance, life-safety guidance, and public layer release unless the fixture is explicitly testing that boundary.
- Pair inputs with expected outputs when practical.
- Do not treat a fixture as evidence, source admission, rights approval, policy approval, release state, precipitation truth, hazard proof, impact proof, forecast truth, health guidance, advisory output, or a published artifact.
- Update this README when precipitation-observation fixture payloads, validators, tests, or helper scripts are added.

## Verification status

- Target README: updated from placeholder content.
- Payload inventory: NEEDS VERIFICATION.
- Tests and validators: NOT RUN.
