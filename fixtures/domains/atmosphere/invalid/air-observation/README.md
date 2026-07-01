# Invalid air-observation fixtures

`fixtures/domains/atmosphere/invalid/air-observation/`

Status: draft / nested fixture lane.

This directory is for negative `AirObservation` fixture examples used by bounded tests or documentation examples. These files are examples only and are not authoritative project records.

## Expected failures

Use this lane for compact cases that should fail schema, validator, policy helper, evidence-closure, freshness, rights, source-role, unit, or safe-render checks.

Examples may include:

- missing station or source context
- missing observed time, retrieved time, units, or QA posture
- stale observations without an explicit freshness boundary
- AQI, PM2.5, ozone, smoke, model, or advisory values collapsed into a generic air observation without the required object boundary
- uncited health, exposure, regulatory, or action claims
- source-role, rights, or caveat gaps that should produce denial, abstention, or safe fallback

## Related fixture lanes

- `../README.md`
- `../../golden/README.md`
- `../../bundles/README.md`

## Related references

- `../../../../../contracts/domains/atmosphere/AirObservation.md`
- `../../../../../contracts/domains/atmosphere/air-observation.md`
- `../../../../../docs/runbooks/atmosphere/NO_NETWORK_TEST_RUNBOOK.md`
- `../../../../../docs/domains/atmosphere/MISSING_OR_PLANNED_FILES.md`
- `../../../../../docs/doctrine/directory-rules.md`

## Maintenance notes

- Keep examples synthetic, compact, deterministic, and reviewable.
- Pair each invalid input with expected error text, expected denial, expected abstention, or expected safe fallback when practical.
- Keep `AirObservation` distinct from PM2.5, ozone, AQI, model output, smoke context, and advisory context unless the fixture is explicitly testing that boundary.
- Do not treat a fixture as evidence, approval, release state, health guidance, or a published artifact.
- Update this README when payload files, validators, tests, or helper scripts are added.

## Verification status

- Target README: updated from placeholder content.
- Payload inventory: NEEDS VERIFICATION.
- Tests and validators: NOT RUN.
