# Valid air-station fixtures

`fixtures/domains/atmosphere/valid/air-station/`

Status: draft / nested fixture lane.

This directory is for positive `AirStation` fixture examples used by bounded tests, validators, no-network checks, helpers, or documentation examples. These files are examples only and are not authoritative station records.

## Scope

Use this lane for compact synthetic station or network-site cases that are expected to pass a specific check while preserving KFM's station boundary. A valid `AirStation` fixture may represent governed station identity, network identity, source context, station class, time span, status, siting class, QA posture, correction lineage, or public-safe station summary fields required by the test.

A valid fixture here does not prove the station exists in the real world, prove attached observations are true, authorize exact public siting, expose station ownership or access details, or approve release of controlled Atmosphere/Air station-site products.

## Expected passes

Examples may include payloads that demonstrate:

- station identity, network identity, source context, or station class is present when required
- station status, time span, siting class, QA posture, or correction lineage is represented when required
- location is generalized, omitted, or policy-safe when exact siting is not allowed by the test
- station metadata remains distinct from `AirObservation`, PM2.5, ozone, AQI, model output, smoke context, weather context, and advisory context
- evidence references close within the fixture-only test boundary when required
- safe-render or release dry-run behavior is demonstrated without promoting anything to `data/published/`

## Related fixture lanes

- `../README.md`
- `../../invalid/air-station/README.md`
- `../../valid/air-observation/README.md`
- `../../invalid/README.md`
- `../../golden/README.md`
- `../../objects/README.md`
- `../../sources/README.md`

## Related references

- `../../../../../contracts/domains/atmosphere/AirStation.md`
- `../../../../../contracts/domains/atmosphere/AirObservation.md`
- `../../../../../docs/runbooks/atmosphere/NO_NETWORK_TEST_RUNBOOK.md`
- `../../../../../docs/domains/atmosphere/OBJECT_FAMILY_MAP.md`
- `../../../../../docs/domains/atmosphere/POLICY.md`
- `../../../../../schemas/contracts/v1/domains/atmosphere/AirStation.schema.json`
- `../../../../../docs/doctrine/directory-rules.md`

## Maintenance notes

- Keep examples synthetic, compact, deterministic, and reviewable.
- Keep each valid fixture tied to a known test, validator, no-network check, helper, or documentation example.
- Record what the fixture is expected to pass; avoid broad claims of real-world correctness.
- Keep `AirStation` distinct from observation values, pollutant-specific observations, AQI reports, model fields, smoke/AOD context, weather context, advisory context, health guidance, and regulatory proof unless the fixture is explicitly testing that boundary.
- Pair inputs with expected outputs when practical.
- Do not treat a fixture as evidence, source admission, rights approval, policy approval, release state, exact public siting approval, station access approval, observation truth, health guidance, or a published artifact.
- Update this README when air-station fixture payloads, validators, tests, or helper scripts are added.

## Verification status

- Target README: updated from placeholder content.
- Payload inventory: NEEDS VERIFICATION.
- Tests and validators: NOT RUN.
