# Invalid air-station fixtures

`fixtures/domains/atmosphere/invalid/air-station/`

Status: draft / nested fixture lane.

This directory is for negative `AirStation` fixture examples used by bounded tests or documentation examples. These files are examples only and are not authoritative project records.

## Expected failures

Use this lane for compact cases that should fail schema, validator, policy helper, evidence-closure, siting, rights, source-role, or safe-render checks.

Examples may include:

- missing station identity, network identity, source context, or station class
- missing time span, status, siting class, or QA posture when required by a test
- exact station coordinates or access details where public-safe generalization is required
- station ownership, private-land context, or infrastructure-sensitive siting exposed without an allowed release path
- air-quality observation values embedded as if the station itself were the observation
- PM2.5, ozone, AQI, model, smoke, weather, or advisory context collapsed into `AirStation`
- unsupported station quality, regulatory, exposure, health, or action claims
- rights, caveat, evidence, or source-role gaps that should produce denial, abstention, or safe fallback

## Related fixture lanes

- `../README.md`
- `../air-observation/README.md`
- `../../golden/README.md`
- `../../bundles/README.md`

## Related references

- `../../../../../contracts/domains/atmosphere/AirStation.md`
- `../../../../../contracts/domains/atmosphere/AirObservation.md`
- `../../../../../docs/runbooks/atmosphere/NO_NETWORK_TEST_RUNBOOK.md`
- `../../../../../docs/domains/atmosphere/MISSING_OR_PLANNED_FILES.md`
- `../../../../../docs/doctrine/directory-rules.md`

## Maintenance notes

- Keep examples synthetic, compact, deterministic, and reviewable.
- Pair each invalid input with expected error text, expected denial, expected abstention, or expected safe fallback when practical.
- Keep `AirStation` distinct from observation values, pollutant observations, AQI reports, model output, smoke context, weather context, and advisory context unless the fixture is explicitly testing that boundary.
- Do not treat a fixture as evidence, approval, release state, health guidance, exact public siting approval, or a published artifact.
- Update this README when payload files, validators, tests, or helper scripts are added.

## Verification status

- Target README: updated from placeholder content.
- Payload inventory: NEEDS VERIFICATION.
- Tests and validators: NOT RUN.
