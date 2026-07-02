# Valid weather-station fixtures

`fixtures/domains/atmosphere/valid/weather-station/`

Status: draft / nested fixture lane.

This directory is for positive `WeatherStation` fixture examples used by bounded tests, validators, no-network checks, helpers, or documentation examples. These files are examples only and are not authoritative weather-station records.

## Scope

Use this lane for compact synthetic meteorological station or weather-network site cases that are expected to pass a specific check while preserving KFM's weather-station boundary. A valid `WeatherStation` fixture may represent governed station identity, network identity, source context, station class, site status, time span, siting class, relocation, decommissioning, correction lineage, public-safe station summary fields, evidence references, or release dry-run fields required by the test.

A valid fixture here does not prove the station exists in the real world, prove attached observations are true, authorize exact public siting, expose station ownership or access details, prove sensor quality, or approve release of controlled Atmosphere/Air station-site products.

## Expected passes

Examples may include payloads that demonstrate:

- station identity, network identity, source context, station class, site status, or time span is present when required
- siting class, generalized location, relocation, decommissioning, supersession, or correction fields are represented when required
- exact station coordinates, ownership, and access details are absent, generalized, or policy-safe when required by the test
- weather station metadata remains distinct from `WeatherObservation`, `TemperatureObservation`, `PrecipitationObservation`, `WindField`, forecast context, climate context, hazard impacts, and advisory context
- evidence references close within the fixture-only test boundary when required
- safe-render or release dry-run behavior is demonstrated without promoting anything to `data/published/`

## Related fixture lanes

- `../README.md`
- `../weather-observation/README.md`
- `../temperature-observation/README.md`
- `../precipitation-observation/README.md`
- `../../golden/README.md`
- `../../invalid/README.md`
- `../../objects/README.md`
- `../../sources/README.md`

## Related references

- `../../../../../contracts/domains/atmosphere/WeatherStation.md`
- `../../../../../contracts/domains/atmosphere/WeatherObservation.md`
- `../../../../../contracts/domains/atmosphere/TemperatureObservation.md`
- `../../../../../contracts/domains/atmosphere/PrecipitationObservation.md`
- `../../../../../contracts/domains/atmosphere/WindField.md`
- `../../../../../contracts/domains/atmosphere/ForecastContext.md`
- `../../../../../contracts/domains/atmosphere/ClimateNormal.md`
- `../../../../../contracts/domains/atmosphere/ClimateAnomaly.md`
- `../../../../../contracts/domains/atmosphere/AdvisoryContext.md`
- `../../../../../docs/runbooks/atmosphere/NO_NETWORK_TEST_RUNBOOK.md`
- `../../../../../docs/domains/atmosphere/OBJECT_FAMILY_MAP.md`
- `../../../../../docs/domains/atmosphere/POLICY.md`
- `../../../../../schemas/contracts/v1/domains/atmosphere/WeatherStation.schema.json`
- `../../../../../docs/doctrine/directory-rules.md`

## Maintenance notes

- Keep examples synthetic, compact, deterministic, and reviewable.
- Keep each valid fixture tied to a known test, validator, no-network check, helper, or documentation example.
- Record what the fixture is expected to pass; avoid broad claims of real-world correctness.
- Keep `WeatherStation` distinct from weather values, temperature observations, precipitation observations, wind fields, model/forecast context, climate context, hazards or impact claims, advisory context, evidence proof, health guidance, life-safety guidance, and public layer release unless the fixture is explicitly testing that boundary.
- Pair inputs with expected outputs when practical.
- Do not treat a fixture as evidence, source admission, rights approval, policy approval, release state, exact public siting approval, station access approval, station ownership approval, observation truth, health guidance, advisory output, or a published artifact.
- Update this README when weather-station fixture payloads, validators, tests, or helper scripts are added.

## Verification status

- Target README: updated from placeholder content.
- Payload inventory: NEEDS VERIFICATION.
- Tests and validators: NOT RUN.
