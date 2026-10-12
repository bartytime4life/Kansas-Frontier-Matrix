# Valid wind-field fixtures

`fixtures/domains/atmosphere/valid/wind-field/`

Status: draft / nested fixture lane.

This directory is for positive `WindField` fixture examples used by bounded tests, validators, no-network checks, helpers, or documentation examples. These files are examples only and are not authoritative wind records.

## Scope

Use this lane for compact synthetic wind speed/direction, station wind observation, gridded wind analysis, or modeled wind context cases that are expected to pass a specific check while preserving KFM's wind-field boundary. A valid `WindField` fixture may represent governed wind speed, direction, gust, vector components, station or grid context, source role, observed time, model run time, valid time, retrieval time, units, QA posture, uncertainty, model-run receipt reference, evidence references, or release dry-run fields required by the test.

A valid fixture here does not prove real-world wind, forecast truth, smoke transport outcome, hazard causation, exposure, damage, health effect, station truth, source-rights clearance, public release, or policy approval.

## Expected passes

Examples may include payloads that demonstrate:

- station, grid, source product, model run, or network context is present when required
- source identity and source role are explicit, including whether the case is observed wind or atmospheric model field
- observed time, model run time, valid time, retrieved time, units, QA posture, uncertainty, and correction fields are represented when required
- wind remains distinct from generic `WeatherObservation`, `WeatherStation`, temperature observations, precipitation observations, forecast context, smoke context, climate context, hazards/impact claims, and advisory context
- evidence references close within the fixture-only test boundary when required
- safe-render or release dry-run behavior is demonstrated without promoting anything to `data/published/`

## Related fixture lanes

- `../README.md`
- `../weather-observation/README.md`
- `../weather-station/README.md`
- `../forecast-context/README.md`
- `../smoke-context/README.md`
- `../../golden/README.md`
- `../../invalid/README.md`
- `../../objects/README.md`
- `../../sources/README.md`

## Related references

- `../../../../../contracts/domains/atmosphere/WindField.md`
- `../../../../../contracts/domains/atmosphere/WeatherObservation.md`
- `../../../../../contracts/domains/atmosphere/WeatherStation.md`
- `../../../../../contracts/domains/atmosphere/ForecastContext.md`
- `../../../../../contracts/domains/atmosphere/SmokeContext.md`
- `../../../../../contracts/domains/atmosphere/TemperatureObservation.md`
- `../../../../../contracts/domains/atmosphere/PrecipitationObservation.md`
- `../../../../../contracts/domains/atmosphere/AdvisoryContext.md`
- `../../../../../docs/runbooks/atmosphere/NO_NETWORK_TEST_RUNBOOK.md`
- `../../../../../docs/domains/atmosphere/OBJECT_FAMILY_MAP.md`
- `../../../../../docs/domains/atmosphere/POLICY.md`
- `../../../../../schemas/contracts/v1/domains/atmosphere/WindField.schema.json`
- `../../../../../docs/doctrine/directory-rules.md`

## Maintenance notes

- Keep examples synthetic, compact, deterministic, and reviewable.
- Keep each valid fixture tied to a known test, validator, no-network check, helper, or documentation example.
- Record what the fixture is expected to pass; avoid broad claims of real-world correctness.
- Keep `WindField` distinct from generic weather observations, station metadata, temperature observations, precipitation observations, model/forecast context, smoke transport proof, climate context, hazards or impact claims, advisory context, evidence proof, health guidance, life-safety guidance, and public layer release unless the fixture is explicitly testing that boundary.
- Pair inputs with expected outputs when practical.
- Do not treat a fixture as evidence, source admission, rights approval, policy approval, release state, wind truth, forecast truth, hazards proof, impact proof, smoke transport proof, health guidance, advisory output, or a published artifact.
- Update this README when wind-field fixture payloads, validators, tests, or helper scripts are added.

## Verification status

- Target README: updated from placeholder content.
- Payload inventory: NEEDS VERIFICATION.
- Tests and validators: NOT RUN.
