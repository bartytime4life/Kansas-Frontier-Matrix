# Atmosphere object fixtures

`fixtures/domains/atmosphere/objects/`

Status: draft / fixture lane.

This directory is for object-shaped Atmosphere fixture examples used by bounded tests, validators, no-network checks, helpers, or documentation examples. These files are examples only and are not authoritative project records.

## Scope

Use this lane for compact fixtures that exercise the Atmosphere object-family roster without requiring live upstream access. Object fixtures should preserve object-family boundaries and avoid collapsing station context, observations, pollutant-specific records, remote-sensing context, weather context, climate context, forecast context, and advisory context into one generic shape.

Object families named by the Atmosphere object map and no-network runbook include:

- `AirStation`
- `AirObservation`
- PM2.5 and ozone observations
- `SmokeContext`
- `AODRaster`
- weather station and weather observation records
- wind, precipitation, and temperature observations
- climate normal and climate anomaly records
- forecast and advisory context records

## Related fixture lanes

- `../bundles/README.md`
- `../golden/README.md`
- `../invalid/README.md`
- `../invalid/air-observation/README.md`
- `../invalid/air-station/README.md`

## Related references

- `../../../docs/domains/atmosphere/OBJECT_FAMILY_MAP.md`
- `../../../docs/domains/atmosphere/MISSING_OR_PLANNED_FILES.md`
- `../../../docs/runbooks/atmosphere/NO_NETWORK_TEST_RUNBOOK.md`
- `../../../contracts/domains/atmosphere/`
- `../../../schemas/contracts/v1/domains/atmosphere/`
- `../../../docs/doctrine/directory-rules.md`

## Maintenance notes

- Keep examples synthetic, compact, deterministic, and reviewable.
- Keep each fixture tied to a known test, validator, no-network check, helper, or documentation example.
- Keep object-family boundaries explicit.
- Pair inputs with expected outputs, expected errors, expected denials, expected abstentions, or expected safe fallbacks when practical.
- Do not treat a fixture as evidence, approval, release state, health guidance, live advisory output, or a published artifact.
- Update this README when object fixture payloads, validators, tests, or helper scripts are added.

## Verification status

- Target README: updated from placeholder content.
- Payload inventory: NEEDS VERIFICATION.
- Tests and validators: NOT RUN.
